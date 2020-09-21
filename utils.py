# Utility file for the pokemon project

POKEMON_TYPE_MAP = {
    'Normal': 0,
    'Fire': 1,
    'Fighting': 2,
    'Water': 3,
    'Flying': 4,
    'Grass': 5,
    'Poison': 6,
    'Electric': 7,
    'Ground': 8,
    'Psychic': 9,
    'Rock': 10,
    'Ice': 11,
    'Bug': 12,
    'Dragon': 13,
    'Ghost': 14,
    'Dark': 15,
    'Steel': 16,
    'Fairy': 17,
}


def clean_types(df):
    df.loc[:, 'mapped_type_1'] = df['type_1'].map(POKEMON_TYPE_MAP)
    df.loc[:, 'mapped_type_2'] = df['type_2'].map(POKEMON_TYPE_MAP)
    df = df.fillna(18)
    df['mapped_type_1'] = df['mapped_type_1'].astype('int32')
    df['mapped_type_2'] = df['mapped_type_2'].astype('int32')
    return df


def print_prediction_errors(test_data, predictions):
    for index, value in enumerate(predictions):
        actual = str(test_data['is_legendary'].iloc[index])
        if actual != str(value):
            print('Index: ' + str(test_data.index[index]) + '   Actual status: ' + actual + '   Prediction: ' + str(value))