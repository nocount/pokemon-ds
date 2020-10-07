# Writing a simple game to practice using model inference/prediction
import pandas as pd
import numpy as np
import pickle
import utils

pd.set_option('display.max_columns', None)

"""
This will simulate a simple guessing game where both the user and model will guess if the pokemon is legendary 
"""
def run_game():
    print('Starting game')

    # Load data for guessing with inference
    df = pd.read_csv('pokemon_data.csv')
    eigth_gen_df = df[809:]
    eigth_gen_df = utils.clean_types(eigth_gen_df)
    user_df = eigth_gen_df.drop(['name', 'id'], axis=1)

    test_X = eigth_gen_df.drop(['type_1', 'type_2', 'name', 'id', 'is_legendary'], axis=1)
    test_y = eigth_gen_df['is_legendary']

    # Load saved logreg model
    model = pickle.load(open('model_chkpt1.pickle', 'rb'))

    for i in range(10):

        index = np.random.randint(84)
        is_legendary = eigth_gen_df['is_legendary'].iloc[index]
        user_out = eigth_gen_df.drop(['name', 'id', 'is_legendary'], axis=1).iloc[[index]]

        print(user_out)
        user_in = input('Guess whether it is legendary... 1 for yes 0 for no. \n')

        if int(user_in) == is_legendary:
            print('Correct hooray!!!!\n')
        else:
            print('Oh I dont think so...\n')

        model_pred = model.predict(test_X.iloc[[index]])
        print('\n\nRobo guess:' + str(model_pred))


if __name__ == '__main__':
    run_game()
