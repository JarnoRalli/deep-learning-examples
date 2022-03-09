from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Model
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tqdm import tqdm
import os
import numpy as np
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import itertools

def get_confusion_matrix(model : Model, generator : ImageDataGenerator, data_path : os.path, image_size, batch_size=32):
    '''
    Creates a confusion matrix based on an ImageDataGenerator with flow_from_directory.
    This method iterates through the images stored in directories (each sub-directory
    contains images from a particular class) and predicts, for each image, using the model,
    which class the input images belongs to. Generates a confusion matrix that can be
    used to assess how good the model is.
    '''
    print('Creating a confusion matrix')
    predictions = []
    targets = []
    i = 0
    generator_flow = generator.flow_from_directory(data_path, target_size=image_size, batch_size=batch_size, shuffle=False)
    nr_samples = generator_flow.samples
    nr_classes = generator_flow.classes

    for x, y in tqdm(generator_flow):
        i += x.shape[0]
        p = model.predict(x)
        p = np.argmax(p, axis=1)
        y = np.argmax(y, axis=1)
        predictions = np.concatenate((predictions, p))
        targets = np.concatenate((targets, y))

        if i >= nr_samples:
            break

    cm = confusion_matrix(targets, predictions)
    return cm, list(generator_flow.class_indices.keys())

# Plot confusion matrix
def plot_confusion_matrix(cm, classes,
                          title='Confusion matrix',
                          normalize=False,
                          cmap=plt.cm.Blues):
    '''
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    Source: https://github.com/lazyprogrammer/machine_learning_examples/blob/master/cnn_class2/util.py
    '''
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]

    plt.figure(figsize=(15, 15))
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=90)
    plt.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt), horizontalalignment="center", color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.show()

