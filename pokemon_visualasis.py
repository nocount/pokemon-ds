# Doing some quick visualization of the pokemon dataset

''' 
Qs:
What are the most common types among legendaries (and in general I guess)
Something else...
'''

import pandas as pd

from matplotlib import pyplot as plt

if __name__ == '__main__':
	# Grouping
	pokemon_df = pd.read_csv('data/pokemon_data.csv')
	legendary_df = pokemon_df[pokemon_df['is_legendary']==1]

	legendary_primary_type = legendary_df.groupby(['type_1']).count()['is_legendary']
	legendary_secondary_type = legendary_df.groupby(['type_2']).count()['is_legendary']

	non_legendary_primary_type = pokemon_df[pokemon_df['is_legendary']==0].groupby(['type_1']).count()['total']
	non_legendary_secondary_type = pokemon_df[pokemon_df['is_legendary']==0].groupby(['type_2']).count()['total']

	# Graphing

	fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(18.0, 6.0))

	ax[0][0].set_title('Legendary Primary Type')
	legendary_primary_type.plot(ax=ax[0][0], kind='bar', color='red')

	ax[0][1].set_title('Legendary Secondary Type')
	legendary_secondary_type.plot(ax=ax[0][1], kind='bar', color='red')


	ax[1][0].set_title('Non Legendary Primary Type')
	non_legendary_primary_type.plot(ax=ax[1][0], kind='bar')

	ax[1][1].set_title('Non Legendary Secondary Type')
	non_legendary_secondary_type.plot(ax=ax[1][1], kind='bar')
	plt.show()

	print('Praise the Sun')

