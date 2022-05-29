import sys
import torch
import random
import pathlib
sys.path.append(str(pathlib.Path(__file__).parent.resolve())+'/src')

import warnings
warnings.filterwarnings("ignore")

from const import ALPHABET, PATH_TEST_DIR, PATH_TEST_LABELS, WEIGHTS_PATH
from config import MODEL, N_HEADS, ENC_LAYERS, DEC_LAYERS,\
                  DEVICE, HIDDEN, BATCH_SIZE

from utils import generate_data, process_data 
from dataset import TextCollate, TextLoader
from utils import evaluate

char2idx = {char: idx for idx, char in enumerate(ALPHABET)}
idx2char = {idx: char for idx, char in enumerate(ALPHABET)}

img2label, _, all_words = process_data(PATH_TEST_DIR, PATH_TEST_LABELS) 
img_names, labels = list(img2label.keys()), list(img2label.values())
X_test = generate_data(img_names)
y_test = labels

test_dataset = TextLoader(X_test, y_test, char2idx ,idx2char, eval=False)
test_loader = torch.utils.data.DataLoader(test_dataset, shuffle=True,
                                           batch_size=BATCH_SIZE, pin_memory=True,
                                           drop_last=True, collate_fn=TextCollate())

if MODEL == 'model1':
  from models import model2
  model = model2.TransformerModel(len(ALPHABET), hidden=HIDDEN, enc_layers=ENC_LAYERS, dec_layers=DEC_LAYERS,   
                          nhead=N_HEADS, dropout=0.0).to(DEVICE)
if MODEL == 'model2':
  from models import model2
  model = model2.TransformerModel(len(ALPHABET), hidden=HIDDEN, enc_layers=ENC_LAYERS, dec_layers=DEC_LAYERS,   
                          nhead=N_HEADS, dropout=0.0).to(DEVICE)

if WEIGHTS_PATH != None:
  print(f'loading weights from {WEIGHTS_PATH}')
  model.load_state_dict(torch.load(WEIGHTS_PATH))

criterion = torch.nn.CrossEntropyLoss(ignore_index=char2idx['PAD'])
metrics = evaluate(model, criterion, test_loader)
print(metrics)