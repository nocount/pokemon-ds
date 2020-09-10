# Creating dataset by scraping from pokemondb

import pandas as pd

from urllib.request import urlopen, Request
from bs4 import BeautifulSoup


def scrape_single_pokemon(url):
	req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
	page = urlopen(req).read()
	soup = BeautifulSoup(page, 'html.parser')

	name = soup.h1.text
	# print(name)

	vital_tables = soup.find_all('table', class_='vitals-table')

	pokedex_data = vital_tables[0]
	national_id = int(pokedex_data.find('strong').text)

	types = pokedex_data.find_all('a', class_='type-icon')
	type_1 = types[0].text
	if len(types) == 2:
		type_2 = types[1].text
	else:
		type_2 = 'N/A'

	pokemon_stats = vital_tables[3]
	ind_stats = pokemon_stats.tbody.find_all('tr')
	hp = ind_stats[0].td.text
	attack = ind_stats[1].td.text
	defense = ind_stats[2].td.text
	sp_attack = ind_stats[3].td.text
	sp_defense = ind_stats[4].td.text
	speed = ind_stats[5].td.text
	total = pokemon_stats.find('td', class_='cell-total').b.text

	legendary_pokemon = [ 'Moltres', 'Articuno', 'Zapdos', 'Mew', 'Mewtwo', 'Entei', 'Raioku', 'Suicune', 'Ho-Oh', 'Lugia', 'Celebi', 'Regirock', 'Regice', 'Registeel', 'Latias', 'Latios', 'Kyogre', 'Groudon', 'Rayquaza', 'Jirachi', 'Deoxys', 'Azelf', 'Mespirit', 'Uxie', 'Dialga', 'Palkia', 'Giratina', 'Cresselia', 'Darkai', 'Manaphy', 'Phione', 'Heatran', 'Regigigas', 'Shaymin', 'Arceus', 'Victini', 'Cobalion', 'Terrakion', 'Virizion', 'Keldeo', 'Tornadus', 'Thundurus', 'Landorus', 'Reshiram', 'Zekrom', 'Kyurem', 'Meloetta', 'Genesect', 'Xerneas', 'Yveltal', 'Zygarde', 'Diancie', 'Volcanion', 'Hoopa', 'Type: Null', 'Silvally', 'Tapu Koko', 'Tapu Lele', 'Tapu Bulu', 'Tapu Fini', 'Cosmog', 'Cosmoem', 'Solgaleo', 'Lunala', 'Nihilego', 'Buzzwole', 'Pheromosa', 'Kartana', 'Celesteela', 'Guzzlord', 'Xurkitree', 'Poipole', 'Naganadel', 'Stakataka', 'Blacephalon', 'Necrozma', 'Magearna', 'Marshadow', 'Zeraora', 'Meltan', 'Melmetal', 'Zacian', 'Zamazenta', 'Eternatus', 'Kubfu', 'Urshifu', 'Calyrex', 'Regieleki', 'Regidrago', 'Zarude']
	is_legendary = 0
	if name in legendary_pokemon:
		is_legendary = 1

	df = pd.DataFrame([[national_id, name, type_1, type_2, hp, attack, defense, sp_attack, sp_defense, speed, total, is_legendary]], columns=['id', 'name', 'type_1', 'type_2', 'hp', 'attack', 'defense', 'sp_attack', 'sp_defense', 'speed', 'total', 'is_legendary'])
	print(df)
	return df


def scrape_pokemon_data(url):
	req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
	page = urlopen(req).read()
	soup = BeautifulSoup(page, 'html.parser')

	pokemon_df = pd.DataFrame(columns=['id', 'name', 'type_1', 'type_2', 'hp', 'attack', 'defense', 'sp_attack', 'sp_defense', 'speed', 'total', 'is_legendary'])
	
	index = 0
	for p in soup.find_all('span', class_='infocard-lg-data'):
		entity = p.find('a', class_='ent-name').get('href')
		link = 'https://pokemondb.net' + entity
		
		single_pokemon_df = scrape_single_pokemon(link)
		pokemon_df = pokemon_df.append(single_pokemon_df, ignore_index=True)
		# index += 1
		# if index == 10:
		# 	break

	return pokemon_df


if __name__ == '__main__':

	pokemon = scrape_pokemon_data('https://pokemondb.net/pokedex/national')
	pokemon.to_csv('pokemon_data.csv', index=False)

	print(sum(pokemon['is_legendary']))
	# print(pokemon)

	print('Praise the Sun')
