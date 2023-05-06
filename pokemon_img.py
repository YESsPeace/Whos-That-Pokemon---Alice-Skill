import datetime
import requests
from io import BytesIO
from PIL import Image
from image_work import upload_image


def get_pokemon_closed_img(poke_img_url):
    response = requests.get(poke_img_url)
    poke_img = Image.open(BytesIO(response.content)).convert('RGBA')
    poke_img.thumbnail(size=(118, 118))

    response = requests.get('https://i.imgur.com/Va7N775.png')
    back = Image.open(BytesIO(response.content)).convert('RGBA')

    red, green, blue, alpha = poke_img.split()

    zeroed_band = red.point(lambda _: 0)

    silhouette = Image.merge(
        "RGBA", (zeroed_band, zeroed_band, zeroed_band, alpha)
    )

    back.paste(silhouette, (24, 40), mask=poke_img.convert('RGBA'))

    buf = BytesIO()
    back.save(buf, format='PNG')
    image = buf.getvalue()
    buf.close()

    data = upload_image(oauth_code='y0_AgAAAAAU2kKeAAT7owAAAADez9M6baNM9fzIR32KsI4uBjYB3XZfmLo',
                        dialog_id='b4eadf08-ca7d-4fba-a5d0-95415be3a3cb',
                        image=image,
                        )

    if type(data) is dict:
        return data['image']

    else:
        return {
            "id": '1656841/9e4545e3447193c00119',
            "size": 73475,
            "createdAt": '2023-03-20T05:53:46.262Z'
        }


def get_pokemon_opened_img(poke_img_url):
    response = requests.get(poke_img_url)
    poke_img = Image.open(BytesIO(response.content)).convert('RGBA')

    poke_img.thumbnail(size=(118, 118))

    response = requests.get('https://i.imgur.com/Va7N775.png')
    back = Image.open(BytesIO(response.content)).convert('RGBA')

    back.paste(poke_img, (24, 40), mask=poke_img.convert('RGBA'))

    buf = BytesIO()
    back.save(buf, format='PNG')
    image = buf.getvalue()
    buf.close()

    data = upload_image(oauth_code='y0_AgAAAAAU2kKeAAT7owAAAADez9M6baNM9fzIR32KsI4uBjYB3XZfmLo',
                        dialog_id='b4eadf08-ca7d-4fba-a5d0-95415be3a3cb',
                        image=image,
                        )

    if type(data) is dict:
        return data['image']

    else:
        return {
            "id": '1656841/9e4545e3447193c00119',
            "size": 73475,
            "createdAt": '2023-03-20T05:53:46.262Z'
        }

if __name__ == '__main__':
    from pokemon_info import get_random_pokemon_info

    start = datetime.datetime.now()
    print('# getting random pokemon info')
    pokemon = get_random_pokemon_info()

    print(*get_pokemon_closed_img(pokemon['image_url']).items(), sep='\n')
    print('# PokeClosed Work time:', datetime.datetime.now() - start)

    start = datetime.datetime.now()
    print(*get_pokemon_opened_img(pokemon['image_url']).items(), sep='\n')
    print('# PokeOpened Work time:', datetime.datetime.now() - start)
