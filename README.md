# OCR Transformer

This is a transformer approach to OCR task. The architecture is composed of three parts: a feature extractor, encoder and decoder. The feature extractor transforms the input image into vectors of features; then temporal encoding is used to encode the order of vectors in a sequence. After that, the encoder transforms a sequence of vectors using the self-attention mechanism to get a context for the second sequence, which is target strings. The target strings also get temporal encoding and passed to the decoder that takes the context as well.

![](https://github.com/constantin50/ocr-transformer/blob/master/arch.png)


# Example: Recognition of Cyrillic Words

# Pretraining

Prior to training on real data, the model is pretrained on synthetic data. Crops are generated in real time using different fonts, backgrounds and Russian words; as fonts as backgrounds were created specifically for this task.

# Training

The training is done on the Cyrillic Handwriting Dataset, which was collected by us. It is composed of 33122 segments of handwriting texts (crops) in Russian and splited into train, and test sets with a split of 95%, 5%, respectively.

For training we used SGD and the increasing dropout from 0.1 to 0.6; the learning rate is constant and equals to 0.001, whereas the batch size is increased starting with 16.