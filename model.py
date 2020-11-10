# Creating basic model for predicting legendaries
import pandas as pd
import numpy as np
import pickle
import utils

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split



if __name__ == '__main__':

    # Read data
    df = pd.read_csv('data/pokemon_data.csv')

    # Limiting the training data to seven generations so we can use the 8th for testing inference later
    seven_gen_df = df[0:809]
    clean_df = utils.clean_types(seven_gen_df)

    # Split data
    train, test = train_test_split(clean_df, test_size=0.30, random_state=42)

    # print(sum(train[train['is_legendary'] == 1]['is_legendary']))
    # print(sum(test[test['is_legendary'] == 1]['is_legendary']))
    # print(train.head())
    # print(test.head())

    # Clean data
    train_X = train.drop(['type_1', 'type_2', 'name', 'id', 'is_legendary'], axis=1)
    train_y = train['is_legendary']

    test_X = test.drop(['type_1', 'type_2', 'name', 'id', 'is_legendary'], axis=1)
    test_y = test['is_legendary']

    # Train/fit Model
    model = LogisticRegression(max_iter=1000, random_state=42).fit(train_X, train_y)

    predictions = model.predict(test_X)

    utils.print_prediction_errors(test, predictions)
    # for index, value in enumerate(predictions):
    #     actual = str(test['is_legendary'].iloc[index])
    #     if actual != str(value):
    #         print('Index: ' + str(test_X.index[index]) + '   Actual status: ' + actual + '   Prediction: ' + str(value))

    score = model.score(test_X, test_y)
    print(score)

    # Save model
    with open('checkpoints/model_chkpt1.pickle', 'wb') as checkpoint_file:
        pickle.dump(model, checkpoint_file)

    print('Praise the Sun')