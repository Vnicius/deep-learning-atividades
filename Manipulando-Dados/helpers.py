import re

import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler


def remove_outliers(dataset, column, threshold=3):
    return dataset[np.abs(dataset[column] - dataset[column].mean()) <= (threshold * dataset[column].std())]


def plot_dist(dataset, column, kind='kde'):
    plt.figure(figsize=(10, 8))
    plt.subplot(211)
    plt.xlim(dataset[column].min(), dataset[column].max()*1.1)

    dataset[column].plot(kind=kind)


def titanic_drops(dataset):
    drop_set = ['ticket', 'body',
                'boat', 'cabin', 'home.dest', 'ticket', 'passengerid']
    drop = []

    for _, column in enumerate(dataset):
        if column.lower() in drop_set:
            drop.append(column)

    return dataset.drop(drop, axis=1)


def fill_estimate(dataset, column):
    return dataset[column].fillna(np.rint(dataset[column].mean()))


def drop_nan_row(dataset, column):
    return dataset.dropna(subset=[column])

def name_replace(dataset):
    name = re.compile(" (\w+\.)")
    names = []

    for n in dataset['name']:
        names.append(name.search(n).group(1))

    return np.array(names);


def label_encoder(dataset, column):
    encoder = LabelEncoder()
    try:
        encoded = encoder.fit_transform(dataset[column]).reshape(-1, 1)
    except:
        values = dataset[column].get_values()
        values = np.expand_dims(values, axis=2)
        values = np.reshape(values, -1)
        encoded = np.empty(values.shape, dtype='str_')

        for i, emb in enumerate(values):
            encoded[i] = emb

        encoded.reshape(-1, 1)
        encoded = encoder.fit_transform(encoded)

    dataset[column] = encoded


def minmax_scaler(dataset, column):
    minmax = MinMaxScaler()

    scaled = minmax.fit_transform(dataset[column].values.reshape(-1, 1))

    dataset[column] = scaled

def standard_scaler(dataset, column):
    standardScaler = StandardScaler()

    scaled = standardScaler.fit_transform(dataset[column].values.reshape(-1, 1))

    dataset[column] = scaled


def drop_na_set(dataset):
    dataset = drop_nan_row(dataset, 'pclass')
    dataset = drop_nan_row(dataset, 'survived')
    dataset = drop_nan_row(dataset, 'sex')
    dataset = drop_nan_row(dataset, 'parch')
    dataset = drop_nan_row(dataset, 'fare')
    dataset = drop_nan_row(dataset, 'embarked')

    return dataset


def titanic_preprocessing_pipeline(dataset, scaler='minmax'):
    dataset = drop_na_set(dataset)

    dataset.loc[:, 'age'] = fill_estimate(dataset, 'age')
    dataset['name'] = name_replace(dataset)

    dataset = titanic_drops(dataset)

    label_encoder(dataset, 'sex')
    label_encoder(dataset, 'embarked')
    label_encoder(dataset, 'name')

    if scaler == 'minmax':
        minmax_scaler(dataset, 'age')
        minmax_scaler(dataset, 'fare')
        minmax_scaler(dataset, 'sibsp')
        minmax_scaler(dataset, 'parch')
        minmax_scaler(dataset, 'pclass')
        minmax_scaler(dataset, 'sex')
        minmax_scaler(dataset, 'embarked')
        minmax_scaler(dataset, 'name') 
    
    elif scaler == 'standard':
        standard_scaler(dataset, 'age')
        standard_scaler(dataset, 'fare')
        standard_scaler(dataset, 'sibsp')
        standard_scaler(dataset, 'parch')
        standard_scaler(dataset, 'pclass')
        standard_scaler(dataset, 'sex')
        standard_scaler(dataset, 'embarked')
        standard_scaler(dataset, 'name')        


    return dataset

def plot_acc_loss(acc, loss):
    plt.figure(figsize=(16,6))
    plt.subplot(1,2,1)
    plt.plot(acc)
    plt.title('model accuracy')
    plt.ylabel('accuracy')
    plt.xlabel('epoch')
    plt.subplot(1,2,2)
    plt.plot(loss)
    plt.title('model loss')
    plt.ylabel('loss')
    plt.xlabel('epoch')
    plt.show()