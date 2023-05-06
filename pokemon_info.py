import datetime
import requests
import random

from ru_pokemon_names import ru_poke_names, new_edit_ru_poke_name

poke_gen = {
    1: (1, 151),
    2: (152, 251),
    3: (252, 386),
    4: (387, 493),
    5: (494, 649),
    6: (650, 721),
    7: (722, 809),
    8: (810, 898)
}

def get_amount_pokemon(gen=None):
    if gen is None:
        return 898

    else:
        a, b = poke_gen[gen]
        return (b - a) + 1

def get_random_poke_names(num_of_names=1, gen: int = None):
    names = []
    ids = []

    a, b = 1, 898
    if not gen is None:
        a, b = poke_gen[gen]

    for _ in range(num_of_names):
        pokemon_id = random.randint(a, b)
        poke_name = new_edit_ru_poke_name[pokemon_id]

        while poke_name in names:
            pokemon_id = random.randint(a, b)
            poke_name = new_edit_ru_poke_name[pokemon_id]

        names.append(poke_name)
        ids.append(pokemon_id)

    return names, ids

def get_random_pokemon_info(gen=None):
    if not gen is None:
        a, b = poke_gen[gen]
    else:
        a, b = 1, 898

    pokemon_id = random.randint(a, b)

    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    response = requests.get(url)

    if response.status_code in [200, 201]:
        response = response.json()

        data = {
            'ENGName': response["name"],
            'RUName': new_edit_ru_poke_name[pokemon_id],
            'ID': response["id"],
            'image_url': f'{response["sprites"]["other"]["official-artwork"]["front_default"]}'
        }

        return data

    else:
        data = {
            'ENGName': '`Error`',
            'RUName': f'HTTP ошибка: {response.status_code}, {response.reason}',
            'ID': 0,
            'image_url': 'https://res.cloudinary.com/teepublic/image/private/s--NkspL6KL--/t_Preview/b_rgb:ffffff,c_lpad,f_jpg,h_630,q_90,w_1200/v1527296869/production/designs/2723988_2.jpg',
        }
        return data


if __name__ == '__main__':
    start = datetime.datetime.now()

    pokemon = get_random_pokemon_info(gen=1)
    print(*pokemon.items(), sep='\n')

    print(datetime.datetime.now() - start)