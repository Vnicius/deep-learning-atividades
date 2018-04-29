import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler


def remove_outliers(dataset, column, threshold=3):
    return dataset[np.abs(dataset[column] - dataset[column].mean()) <= (threshold * dataset[column].std())]


def plot_dist(dataset, column, kind='kde'):
    plt.figure(figsize=(10, 8))
    plt.subplot(211)
    plt.xlim(dataset[column].min(), dataset[column].max()*1.1)

    dataset[column].plot(kind=kind)


def titanic_drops(dataset):
    drop_set = ['name', 'ticket', 'body',
                'boat', 'cabin', 'home.dest', 'ticket']
    drop = []

    for _, column in enumerate(dataset):
        if column in drop_set:
            drop.append(column)

    return dataset.drop(drop, axis=1)


def fill_estimate(dataset, column):
    return dataset[column].fillna(np.rint(dataset[column].mean()))


def drop_nan_row(dataset, column):
    return dataset.dropna(subset=[column])


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


def drop_na_set(dataset):
    dataset = drop_nan_row(dataset, 'pclass')
    dataset = drop_nan_row(dataset, 'survived')
    dataset = drop_nan_row(dataset, 'sex')
    dataset = drop_nan_row(dataset, 'parch')
    dataset = drop_nan_row(dataset, 'fare')
    dataset = drop_nan_row(dataset, 'embarked')

    return dataset


def titanic_preprocessing_pipeline(dataset):
    dataset = drop_na_set(dataset)

    dataset['age'] = fill_estimate(dataset, 'age')

    dataset = titanic_drops(dataset)

    label_encoder(dataset, 'sex')
    label_encoder(dataset, 'embarked')

    minmax_scaler(dataset, 'age')
    minmax_scaler(dataset, 'fare')

    return dataset
