import random
from difflib import SequenceMatcher

from image_work import delete_image
from phrases_n_sounds import abort_game_phrases, start_gen_question_phrases, welcome_message_phrases_tts, \
    right_choice_phrases_text, \
    incorrect_choice_phrases_tts, right_choice_phrases_tts, whos_the_pokemon_text_and_tts, \
    welcome_message_phrases_title, incorrect_choice_phrases_title, which_rules_text, what_is_the_game_text, \
    gen_question_fallback_text_tts, start_game_question_fallback_text_tts, no_img_to_repeat_text_tts, \
    help_in_start_text_tts
from pokemon_img import get_pokemon_closed_img
from pokemon_info import get_random_pokemon_info, get_random_poke_names, get_amount_pokemon
from ru_pokemon_names import ru_poke_names, new_edit_ru_poke_name

STATE_REQUEST_KEY = 'session'
STATE_RESPONSE_KEY = 'session_state'


def check_similarity(str1, str2):
    similarity = SequenceMatcher(None, str1, str2).ratio()
    return similarity >= 0.50


def make_response(text, tts: str = None, card: dict = None, buttons: list = None,
                  state: dict = None, user_state_update: dict = None, end_session: bool = False):
    response = {
        'text': text,
        'tts': tts if tts is not None else text,
        "end_session": end_session,
    }

    if card is not None:
        response['card'] = card

    if buttons is not None:
        response['buttons'] = buttons

    webhook_response = {
        'response': response,
        'version': '1.0'
    }

    if state is not None:
        webhook_response[STATE_RESPONSE_KEY] = state

    if user_state_update is not None:
        webhook_response['user_state_update'] = user_state_update

    return webhook_response

def pokemon_is_over(event, text):
    session = event.get('state').get(STATE_REQUEST_KEY, {})
    user = event.get('state').get('user', {})

    old_pokemon = session['current_pokemon']
    score = session['score']

    delete_image(
        oauth_code='y0_AgAAAAAU2kKeAAT7owAAAADez9M6baNM9fzIR32KsI4uBjYB3XZfmLo',
        dialog_id='b4eadf08-ca7d-4fba-a5d0-95415be3a3cb',
        image_id=old_pokemon['closed_img']['id'],
    )

    card = {
        "type": "ItemsList",
        "header": {
            "text": text,
        },
        "items": [
            {
                "image_id": "1533899/60b859d5fe86ac77a2da",
                "title": f"Вы победили.",
                "description": "Даже я так не могу. Вы настоящий поке-гуру",
            },
            {
                "image_id": "1521359/4aaeea7a6bf32a93c007",
                "title": f"Ваш счёт составил {score}.",
                "description": "Счёт обнуляется с каждой попыткой.",
            },
            {
                "image_id": "1540737/614dc01a14d807bf4b0e",
                "title": "Начать игру ещё раз",
                "description": 'Хотите начать ещё одну партию? Скажите "Начать игру с 1 поколения". Надеюсь вы не забыли, что их 8. ' + \
                               'Не забывайте использовать голосовой ввод.',
                "button": {
                    "text": "Начать игру",
                }
            },
        ],

    }

    buttons = [
        {
            "title": "Начать игру ещё раз",
            "hide": True
        },
        {
            "title": "Правила",
            "hide": True
        },
        {
            "title": "Начать игру со всеми поколениями",
            "hide": True
        },
        {
            "title": "Начать игру с 1 поколения",
            "hide": True
        },
        {
            "title": "Начать игру с 2 поколения",
            "hide": True
        },
        {
            "title": "Начать игру с 3 поколения",
            "hide": True
        },
        {
            "title": "Начать игру с 4 поколения",
            "hide": True
        },
        {
            "title": "Начать игру с 5 поколения",
            "hide": True
        },
        {
            "title": "Начать игру с 6 поколения",
            "hide": True
        },
        {
            "title": "Начать игру с 7 поколения",
            "hide": True
        },
        {
            "title": "Начать игру с 8 поколения",
            "hide": True
        },
    ]

    state = {
        'screen': 'incorrect_choice',
        'start_game_question': True,
        'game_running': False,
        'used_poke_ids': [],
        'generation': None,
        'buttons': buttons,
        'score': 0
    }

    user_state_update = {
        'start_gen_question': False,
        'incorrect_choice': True,
        'right_choice': False,
        'start_game': False,
        'current_pokemon': old_pokemon,
        'used_poke_ids': [],
        'old_pokemon': None,
        'current_card': None,
        'current_buttons': buttons,
        'score': score,
        'generation': None
    }

    return make_response(text, buttons=buttons, state=state, card=card, user_state_update=user_state_update)

def incorrect_choice(event):
    session = event.get('state').get(STATE_REQUEST_KEY, {})
    user = event.get('state').get('user', {})

    old_pokemon = session['current_pokemon']
    score = session['score']

    delete_image(
        oauth_code='y0_AgAAAAAU2kKeAAT7owAAAADez9M6baNM9fzIR32KsI4uBjYB3XZfmLo',
        dialog_id='b4eadf08-ca7d-4fba-a5d0-95415be3a3cb',
        image_id=old_pokemon['closed_img']['id'],
    )

    text = ' '

    tts = random.choices(
        list(incorrect_choice_phrases_tts.keys()),
        weights=list(incorrect_choice_phrases_tts.values())
    )[0]

    tts = tts.replace('{}', str(ru_poke_names[old_pokemon['ID']]))

    card = {
        "type": "ItemsList",
        "header": {
            "text": random.choices(
                list(incorrect_choice_phrases_title.keys()),
                weights=list(incorrect_choice_phrases_title.values())
            )[0]
        },
        "items": [
            {
                "image_id": "997614/7c9fb54de3b3976140f4",
                "title": f"Это был {old_pokemon['RUName']}",
                "description": "Не расстраивайтесь, даже я ещё не всех выучила.",
            },
            {
                "image_id": "1521359/4aaeea7a6bf32a93c007",
                "title": f"Ваш счёт составил {score}.",
                "description": "Счёт обнуляется с каждой попыткой.",
            },
            {
                "image_id": "1540737/614dc01a14d807bf4b0e",
                "title": "Начать игру ещё раз",
                "description": 'Хотите начать ещё одну партию? Скажите "Начать игру с 1 поколения". Надеюсь вы не забыли, что их 8. ' + \
                               'Не забывайте использовать голосовой ввод.',
                "button": {
                    "text": "Начать игру",
                }
            },
        ],

    }

    buttons = [
        {
            "title": "Начать игру ещё раз",
            "hide": True
        },
        {
            "title": "Правила",
            "hide": True
        },
        {
            "title": "Начать игру со всеми поколениями",
            "hide": True
        },
        {
            "title": "Начать игру с 1 поколения",
            "hide": True
        },
        {
            "title": "Начать игру с 2 поколения",
            "hide": True
        },
        {
            "title": "Начать игру с 3 поколения",
            "hide": True
        },
        {
            "title": "Начать игру с 4 поколения",
            "hide": True
        },
        {
            "title": "Начать игру с 5 поколения",
            "hide": True
        },
        {
            "title": "Начать игру с 6 поколения",
            "hide": True
        },
        {
            "title": "Начать игру с 7 поколения",
            "hide": True
        },
        {
            "title": "Начать игру с 8 поколения",
            "hide": True
        },
    ]

    state = {
        'screen': 'incorrect_choice',
        'start_game_question': True,
        'game_running': False,
        'used_poke_ids': [],
        'generation': None,
        'buttons': buttons,
        'score': 0
    }

    user_state_update = {
        'start_gen_question': False,
        'incorrect_choice': True,
        'right_choice': False,
        'start_game': False,
        'current_pokemon': old_pokemon,
        'used_poke_ids': [],
        'old_pokemon': None,
        'current_card': None,
        'current_buttons': buttons,
        'score': score,
        'generation': None
    }

    return make_response(text, tts=tts, buttons=buttons, state=state, card=card, user_state_update=user_state_update)


def repeat_incorrect_choice(event):
    session = event.get('state').get(STATE_REQUEST_KEY, {})
    user = event.get('state').get('user', {})

    old_pokemon = user['current_pokemon']
    score = user['score']

    delete_image(
        oauth_code='y0_AgAAAAAU2kKeAAT7owAAAADez9M6baNM9fzIR32KsI4uBjYB3XZfmLo',
        dialog_id='b4eadf08-ca7d-4fba-a5d0-95415be3a3cb',
        image_id=old_pokemon['closed_img']['id'],
    )

    text = ' '

    tts = random.choices(
        list(incorrect_choice_phrases_tts.keys()),
        weights=list(incorrect_choice_phrases_tts.values())
    )[0]

    tts = tts.replace('{}', str(ru_poke_names[old_pokemon['ID']]))

    card = {
        "type": "ItemsList",
        "header": {
            "text": f"К сожалению вы не угдали.",
        },
        "items": [
            {
                "image_id": "1652229/229f75d11c8268eade81",
                "title": f"Это был {old_pokemon['RUName']}",
                "description": 'Если вам нужна подсказка, то скажите "Я не знаю такого"',
            },
            {
                "image_id": "1521359/4aaeea7a6bf32a93c007",
                "title": f"Ваш счёт составил {score}.",
                "description": "Счёт обнуляется с каждой попыткой.",
            },
            {
                "image_id": "1540737/614dc01a14d807bf4b0e",
                "title": "Начать игру ещё раз",
                "description": 'Хотите начать ещё одну партию? Скажите "Начать игру с 1 поколения". Надеюсь вы не забыли, что их 8. ' + \
                               'Не забывайте использовать голосовой ввод.',
                "button": {
                    "text": "Начать игру",
                }
            },
        ],

    }

    buttons = [
        {
            "title": "Начать игру ещё раз",
            "hide": True
        },
        {
            "title": "Правила",
            "hide": True
        },
        {
            "title": "Начать игру со всеми поколениями",
            "hide": True
        },
        {
            "title": "Начать игру с 1 поколения",
            "hide": True
        },
        {
            "title": "Начать игру с 2 поколения",
            "hide": True
        },
        {
            "title": "Начать игру с 3 поколения",
            "hide": True
        },
        {
            "title": "Начать игру с 4 поколения",
            "hide": True
        },
        {
            "title": "Начать игру с 5 поколения",
            "hide": True
        },
        {
            "title": "Начать игру с 6 поколения",
            "hide": True
        },
        {
            "title": "Начать игру с 7 поколения",
            "hide": True
        },
        {
            "title": "Начать игру с 8 поколения",
            "hide": True
        },
    ]

    state = {
        'screen': 'repeat_incorrect_choice',
        'start_game_question': True,
        'game_running': False,
        'generation': None,
        'buttons': buttons,
        'used_poke_ids': [],
        'score': 0
    }

    return make_response(text, buttons=buttons, tts=tts, state=state, card=card)


def right_choice(event):
    session = event.get('state').get(STATE_REQUEST_KEY, {})
    score = session['score']
    gen = session['generation']
    user = event.get('state').get('user', {})

    old_pokemon = session['current_pokemon']

    delete_image(
        oauth_code='y0_AgAAAAAU2kKeAAT7owAAAADez9M6baNM9fzIR32KsI4uBjYB3XZfmLo',
        dialog_id='b4eadf08-ca7d-4fba-a5d0-95415be3a3cb',
        image_id=old_pokemon['closed_img']['id'],
    )

    used_poke_ids = session.get('used_poke_ids', [])

    pokemon = get_random_pokemon_info(gen=gen)

    if len(used_poke_ids) < get_amount_pokemon(gen=gen):
        while pokemon['ID'] in used_poke_ids:
            pokemon = get_random_pokemon_info(gen=gen)

    else:
        if not gen is None:
            text = 'Упс, кажется, что покемоны из этого поколения закончились.'
        else:
            text = 'Вот это да, кажется, что покемоны закончились.'
        return pokemon_is_over(event, text)

    used_poke_ids.append(pokemon['ID'])

    pokemon['closed_img'] = get_pokemon_closed_img(pokemon['image_url'])

    tts = random.choices(
        list(right_choice_phrases_tts.keys()),
        weights=list(right_choice_phrases_tts.values())
    )[0]

    text = random.choices(
        list(right_choice_phrases_text.keys()),
        weights=list(right_choice_phrases_text.values())
    )[0]

    tts += text.replace('{}', str(ru_poke_names[old_pokemon['ID']]))

    text = text.replace('{}', str(new_edit_ru_poke_name[old_pokemon['ID']]))

    card = {
        "type": "BigImage",
        "image_id": pokemon['closed_img']['id'],
        "title": text,
    }

    names_pokemon, pokemon_ids = get_random_poke_names(num_of_names=2, gen=gen)

    while pokemon['RUName'] in names_pokemon:
        names_pokemon, pokemon_ids = get_random_poke_names(num_of_names=2, gen=gen)

    names_pokemon.append(pokemon['RUName'])
    random.shuffle(names_pokemon)

    buttons = [
        {
            "title": names_pokemon[0],
            "hide": False
        },
        {
            "title": names_pokemon[1],
            "hide": False
        },
        {
            "title": names_pokemon[2],
            "hide": False
        },
        {
            "title": 'Подсказка',
            "hide": True
        },
        {
            "title": "Правила",
            "hide": True
        },
        {
            "title": 'Покажи картинку ещё раз',
            "hide": True
        },
        {
            "title": 'Начать заново',
            "hide": True
        },
        {
            "title": 'Закончить игру',
            "hide": True
        },
    ]

    score += 1



    state = {
        'screen': 'right_choice',
        'start_game_question': False,
        'game_running': True,
        'current_pokemon': pokemon,
        'score': score,
        'current_pokemon_ids': pokemon_ids,
        'used_poke_ids': used_poke_ids,
        'generation': gen,
        'buttons': buttons
    }

    user_state_update = {
        'start_gen_question': False,
        'incorrect_choice': False,
        'right_choice': True,
        'start_game': False,
        'current_pokemon': pokemon,
        'old_pokemon': old_pokemon,
        'current_card': card,
        'current_pokemon_ids': pokemon_ids,
        'used_poke_ids': used_poke_ids,
        'current_buttons': buttons,
        'score': score,
        'generation': gen
    }

    return make_response(text, tts=tts, state=state, card=card, buttons=buttons, user_state_update=user_state_update)


def repeat_right_choice(event):
    session = event.get('state').get(STATE_REQUEST_KEY, {})
    user = event.get('state').get('user', {})

    score = user['score']
    gen = user.get('generation')
    pokemon = user['current_pokemon']
    old_pokemon = user['old_pokemon']
    used_poke_ids = user.get('used_poke_ids', [])

    tts = random.choices(
        list(right_choice_phrases_tts.keys()),
        weights=list(right_choice_phrases_tts.values())
    )[0]

    text = random.choices(
        list(right_choice_phrases_text.keys()),
        weights=list(right_choice_phrases_text.values())
    )[0]

    tts += text.replace('{}', str(ru_poke_names[old_pokemon['ID']]))

    text = text.replace('{}', str(new_edit_ru_poke_name[old_pokemon['ID']]))

    card = user['current_card']
    buttons = user['current_buttons']
    pokemon_ids = user.get('current_pokemon_ids')

    state = {
        'screen': 'repeat_right_choice()',
        'start_game_question': False,
        'game_running': True,
        'current_pokemon': pokemon,
        'used_poke_ids': used_poke_ids,
        'score': score,
        'current_pokemon_ids': pokemon_ids,
        'generation': gen,
        'buttons': buttons
    }

    return make_response(text, tts=tts, state=state, card=card, buttons=buttons, user_state_update=user)


def start_gen_question(event):
    text = random.choices(
        list(start_gen_question_phrases.keys()),
        weights=list(start_gen_question_phrases.values())
    )[0]

    buttons = [
        {
            "title": "Все сразу",
            "hide": True
        },
        {
            "title": "Поколение 1",
            "hide": True
        },
        {
            "title": "Поколение 2",
            "hide": True
        },
        {
            "title": "Поколение 3",
            "hide": True
        },
        {
            "title": "Поколение 4",
            "hide": True
        },
        {
            "title": "Поколение 5",
            "hide": True
        },
        {
            "title": "Поколение 6",
            "hide": True
        },
        {
            "title": "Поколение 7",
            "hide": True
        },
        {
            "title": "Поколение 8",
            "hide": True
        },
    ]

    state = {
        'screen': 'start_gen_question',
        'start_game_question': False,
        'game_running': False,
        'start_gen_question': True,
        'buttons': buttons,
        'score': 0,
        'generation': None
    }

    user_state_update = {
        'start_gen_question': True,
        'incorrect_choice': False,
        'right_choice': False,
        'start_game': False,
        'current_pokemon': None,
        'old_pokemon': None,
        'current_card': None,
        'current_buttons': buttons,
        'score': 0,
        'generation': None
    }

    return make_response(text=text, buttons=buttons, state=state, user_state_update=user_state_update)


def start_game(event):
    entites = event['request'].get('nlu', {}).get('entities')
    message = str(event.get('request', {}).get('command', '')).lower()

    gen = None

    text, tts = random.choices(
        list(gen_question_fallback_text_tts.keys()),
        weights=list(gen_question_fallback_text_tts.values())
    )[0]

    if len(entites) != 0:
        gen = entites[0]['value']
        if not (1 <= gen <= 8):
            return fallback(event, text=text, tts=tts)

    elif len(message) != 0:
        message = message.split()
        for word in message:
            if word.isnumeric() is True:
                try:
                    gen = int(word)
                    if not (1 <= gen <= 8):
                        return fallback(event, text=text, tts=tts)

                except:
                    return fallback(event, text=text, tts=tts)

    session = event.get('state').get(STATE_REQUEST_KEY, {})

    text = 'А вот и первый <3'

    tts = '<speaker audio="dialogs-upload/b4eadf08-ca7d-4fba-a5d0-95415be3a3cb/72e343ef-3276-48f6-90d1-7f39e7262325.opus"> ' + \
          'А вот и первый покем+ончик'

    pokemon = get_random_pokemon_info(gen=gen)
    pokemon['closed_img'] = get_pokemon_closed_img(pokemon['image_url'])

    card = {
        "type": "BigImage",
        "image_id": pokemon['closed_img']['id'],
        "title": f"Это что за карманный монстр?! Поколение {gen}" if not gen is None else f"Это что за карманный монстр?!",
    }

    names_pokemon, pokemon_ids = get_random_poke_names(num_of_names=2, gen=gen)

    while pokemon['RUName'] in names_pokemon:
        names_pokemon, pokemon_ids = get_random_poke_names(num_of_names=2, gen=gen)

    names_pokemon.append(pokemon['RUName'])
    random.shuffle(names_pokemon)

    buttons = [
        {
            "title": names_pokemon[0],
            "hide": False
        },
        {
            "title": names_pokemon[1],
            "hide": False
        },
        {
            "title": names_pokemon[2],
            "hide": False
        },
        {
            "title": 'Подсказка',
            "hide": True
        },
        {
            "title": "Правила",
            "hide": True
        },
        {
            "title": 'Покажи картинку ещё раз',
            "hide": True
        },
        {
            "title": 'Начать заново',
            "hide": True
        },
        {
            "title": 'Закончить игру',
            "hide": True
        },
    ]

    state = {
        'screen': 'start_game',
        'start_game_questions': False,
        'game_running': True,
        'current_pokemon': pokemon,
        'used_poke_ids': [pokemon['ID'], ],
        'current_pokemon_ids': pokemon_ids,
        'score': 0,
        'generation': gen,
        'buttons': buttons
    }

    user_state_update = {
        'start_gen_question': False,
        'incorrect_choice': False,
        'right_choice': False,
        'start_game': True,
        'current_pokemon': pokemon,
        'used_poke_ids': [pokemon['ID'], ],
        'current_pokemon_ids': pokemon_ids,
        'old_pokemon': pokemon,
        'current_card': card,
        'current_buttons': buttons,
        'score': 0,
        'generation': gen
    }

    return make_response(text, tts, card, buttons, state, user_state_update)


def repeat_start_game(event):
    entites = event['request'].get('nlu', {}).get('entities')
    if len(entites) != 0:
        gen = entites[0]['value']
        if not (1 <= gen <= 8):
            return fallback(event,
                            text='Выберете поколение из промежутка от 1 до 8',
                            tts='Выберете поколение из промежутка от одного до восьми')
    else:
        gen = None

    session = event.get('state').get(STATE_REQUEST_KEY, {})
    user = event.get('state').get('user', {})

    text = ' '
    tts = '<speaker audio="dialogs-upload/b4eadf08-ca7d-4fba-a5d0-95415be3a3cb/72e343ef-3276-48f6-90d1-7f39e7262325.opus">'

    pokemon = user['current_pokemon']
    pokemon_ids = user.get('current_pokemon_ids')

    card = user['current_card']
    buttons = user['current_buttons']

    state = {
        'screen': 'repeat_start_game',
        'start_game_questions': False,
        'game_running': True,
        'current_pokemon': pokemon,
        'used_poke_ids': [pokemon['ID'], ],
        'score': 0,
        'current_pokemon_ids': pokemon_ids,
        'generation': user.get('generation'),
        'buttons': buttons
    }

    return make_response(text=text, tts=tts, card=card, buttons=buttons, state=state, user_state_update=user)


def check_response(event):
    session = event.get('state').get(STATE_REQUEST_KEY, {})
    message = str(event.get('request', {})['original_utterance']).lower().split()

    intents = event['request'].get('nlu', {}).get('intents')

    pokemon = session['current_pokemon']

    current_pokemon_name = ru_poke_names[pokemon['ID']]

    pokemon_ids = session.get('current_pokemon_ids')  # not right pokemons

    check_poke_name = False
    check_else_poke_names = False

    for i in range(len(message)):
        if pokemon['RUName'].lower() in ' '.join(message):
            check_poke_name = True
            break

        if check_similarity(current_pokemon_name.lower(), message[i]) is True:
            check_poke_name = True
            break

        if i < (len(message) - 1):
            if check_similarity(current_pokemon_name.lower(), f'{message[i]} {message[i + 1]}') is True:
                check_poke_name = True
                break

        if not pokemon_ids is None:
            for poke_id in pokemon_ids:

                if new_edit_ru_poke_name[poke_id].lower() in ' '.join(message):
                    check_else_poke_names = True
                    break

                if check_similarity(ru_poke_names[poke_id].lower(), message[i]) is True:
                    check_else_poke_names = True
                    break

                if i < (len(message) - 1):
                    if check_similarity(ru_poke_names[poke_id].lower(), f'{message[i]} {message[i + 1]}') is True:
                        check_else_poke_names = True
                        break
        else:
            check_else_poke_names = True

    if 'help_in_game' in intents:
        return help_in_game(event)

    elif 'YANDEX.HELP' in intents:
        return fallback(event,
                        text='Ответьте что это за карманный монстр, сказав имя или нажав на кнопку.',
                        card_title='Ответьте что это за карманный монстр, сказав имя или нажав на кнопку. \n' + \
                                   'Если вам сложно ответить, то воспользуйтесь подсказкой.'
                        )

    elif (check_poke_name is True) and (check_else_poke_names is False):
        return right_choice(event)

    elif (check_poke_name is False) and (check_else_poke_names is True):
        return incorrect_choice(event)

    else:
        return fallback(event,
                        text='Кажется это не соответсвует ни одному из предложенных имён.',
                        card_title='Кажется это не соответсвует ни одному из предложенных имён.'
                        )


def help_in_game(event):
    session = event['state'][STATE_REQUEST_KEY]
    user = event.get('state').get('user', {})

    pokemon = session['current_pokemon']
    current_pokemon_name = ru_poke_names[pokemon['ID']]

    card = {
        "type": "BigImage",
        "image_id": pokemon['closed_img']['id'],
        "title": f'Подскажу, первая буква "{current_pokemon_name[0].upper()}"',
    }

    buttons = session.get('buttons')

    text = f'Подскажу, первая буква "{current_pokemon_name[0]}"'
    tts = f'Подскажу, первая буква. {current_pokemon_name[0]}'

    return make_response(text, card=card, buttons=buttons, tts=tts, state=session, user_state_update=user)


def what_is_the_game(event):
    text = random.choices(
        list(what_is_the_game_text.keys()),
        weights=list(what_is_the_game_text.values())
    )[0]

    buttons = [
        {
            "title": "Начать игру",
            "hide": True
        },
        {
            "title": "Правила",
            "hide": True
        },
        {
            "title": "Я не хочу играть",
            "hide": True
        },
        {
            "title": "Что такое покемон?",
            "hide": True
        },
        {
            "title": "Начать игру со всеми поколениями",
            "hide": True
        },
        {
            "title": "Начать игру с 1 поколения",
            "hide": True
        },
        {
            "title": "Начать игру с 2 поколения",
            "hide": True
        },
        {
            "title": "Начать игру с 3 поколения",
            "hide": True
        },
        {
            "title": "Начать игру с 4 поколения",
            "hide": True
        },
        {
            "title": "Начать игру с 5 поколения",
            "hide": True
        },
        {
            "title": "Начать игру с 6 поколения",
            "hide": True
        },
        {
            "title": "Начать игру с 7 поколения",
            "hide": True
        },
        {
            "title": "Начать игру с 8 поколения",
            "hide": True
        },
    ]

    session = event['state'][STATE_REQUEST_KEY]
    if session.get('game_running') is True:
        buttons.insert(1,
                       {
                           "title": "Покажи картинку ещё раз",
                           "hide": True
                       }
                       )

    state = {
        'screen': 'what_is_the_game',
        'start_game_question': True,
        'game_running': False,
        'buttons': buttons,
        'generation': None
    }

    return make_response(text, buttons=buttons, state=state)


def which_rules(event):
    text = random.choices(
        list(which_rules_text.keys()),
        weights=list(which_rules_text.values())
    )[0]

    card = {
        "type": "ItemsList",
        "header": {
            "text": text,
        },
        "items": [
            {
                "image_id": "1652229/229f75d11c8268eade81",
                "title": 'Угадывайте',
                "description": 'Вам будет предложено угадывать карманных монстров по их силуэтам.',
            },
            {
                "image_id": "1521359/4aaeea7a6bf32a93c007",
                "title": 'Давайте ответы и получайти очки',
                "description": 'Вы можете давать ответы, называя имена монстров или нажимая на соответствующие кнопки. \n' + \
                               'За каждый правильный ответ вы будете получать очки.',
            },
            {
                "image_id": "1656841/407dffdcb4283f85ae7e",
                "title": 'Выбор поколения',
                "description": 'Перед началом игры вы сможете выбрать поколение карманных монстров. \n' +
                               'Всего в игре есть 8 поколений.',
            },
            {
                "image_id": "937455/69c74f3d7c5f71631974",
                "title": 'Вы не угадали?',
                "description": 'В конце игры, вы сможете увидеть свой итоговый счет и узнать, ' +
                               'насколько хорошо вы знаете карманных монстров.',
            },
            {
                "image_id": "1540737/614dc01a14d807bf4b0e",
                "title": "Начать игру",
                "description": "Хотите начать? Удачи! Не забывайте, что можно назвывать имена голосом.",
                "button": {
                    "text": "Начать игру",
                }
            },
        ],
    }

    buttons = [
        {
            "title": "Начать игру",
            "hide": True
        },
        {
            "title": "Правила",
            "hide": True
        },
        {
            "title": "Я не хочу играть",
            "hide": True
        },
        {
            "title": "Что такое покемон?",
            "hide": True
        },
        {
            "title": "Начать игру со всеми поколениями",
            "hide": True
        },
        {
            "title": "Начать игру с 1 поколения",
            "hide": True
        },
        {
            "title": "Начать игру с 2 поколения",
            "hide": True
        },
        {
            "title": "Начать игру с 3 поколения",
            "hide": True
        },
        {
            "title": "Начать игру с 4 поколения",
            "hide": True
        },
        {
            "title": "Начать игру с 5 поколения",
            "hide": True
        },
        {
            "title": "Начать игру с 6 поколения",
            "hide": True
        },
        {
            "title": "Начать игру с 7 поколения",
            "hide": True
        },
        {
            "title": "Начать игру с 8 поколения",
            "hide": True
        },
    ]

    session = event['state'][STATE_REQUEST_KEY]
    if session.get('game_running') is True:
        buttons.insert(1,
                       {
                           "title": "Покажи картинку ещё раз",
                           "hide": True
                       }
                       )

    state = {
        'screen': 'what_is_the_game',
        'start_game_question': True,
        'game_running': False,
        'buttons': buttons,
        'generation': None
    }

    return make_response(text, card=card, buttons=buttons, state=state)


def whos_the_pokemon(event):
    text, tts = random.choices(
        list(whos_the_pokemon_text_and_tts.keys()),
        weights=list(whos_the_pokemon_text_and_tts.values())
    )[0]

    buttons = [
        {
            "title": "Да, начать игру",
            "hide": True
        },
        {
            "title": "Нет, я не хочу играть",
            "hide": True
        },
        {
            "title": "Правила",
            "hide": True
        },
        {
            "title": "Начать игру со всеми поколениями",
            "hide": True
        },
        {
            "title": "Начать игру с 1 поколения",
            "hide": True
        },
        {
            "title": "Начать игру с 2 поколения",
            "hide": True
        },
        {
            "title": "Начать игру с 3 поколения",
            "hide": True
        },
        {
            "title": "Начать игру с 4 поколения",
            "hide": True
        },
        {
            "title": "Начать игру с 5 поколения",
            "hide": True
        },
        {
            "title": "Начать игру с 6 поколения",
            "hide": True
        },
        {
            "title": "Начать игру с 7 поколения",
            "hide": True
        },
        {
            "title": "Начать игру с 8 поколения",
            "hide": True
        },
    ]

    state = {
        'screen': 'what_is_the_game',
        'start_game_question': True,
        'game_running': False,
        'buttons': buttons,
        'generation': None
    }

    return make_response(text, buttons=buttons, tts=tts, state=state)


def welcome_message(event):
    text = ' '

    tts = random.choices(
        list(welcome_message_phrases_tts.keys()),
        weights=list(welcome_message_phrases_tts.values())
    )[0]

    card = {
        "type": "ItemsList",
        "header": {
            "text": random.choices(
                list(welcome_message_phrases_title.keys()),
                weights=list(welcome_message_phrases_title.values())
            )[0]
        },
        "items": [
            {
                "image_id": "1540737/614dc01a14d807bf4b0e",
                "title": "Начать игру",
                "description": "Хотите начать? Не забудьте выбрать поколение. Напомню их 8. " + \
                               "А также не забывайте, что можно назвывать имена голосом",
                "button": {
                    "text": "Начать игру",
                }
            },
            {
                "image_id": "1652229/229f75d11c8268eade81",
                "title": "Что это за игра?",
                "description": "Если не знаете как играть, я всё объясню.",
                "button": {
                    "text": "Что это за игра?",
                }
            },
            {
                "image_id": "937455/69c74f3d7c5f71631974",
                "title": "Какие правила?",
                "description": "Если не знаете правил, я всё объясню.",
                "button": {
                    "text": "Правила",
                }
            },
            {
                "image_id": "1652229/adc1006870e990462dab",
                "title": "Ваши права были нарушены?!",
                "description": "Вы Nintendo и ваши права были нарушены? Какой ужас, мы всё исправим.",
                "button": {
                    "text": "Мы Nintendo и наши права были нарушены.",
                }
            },
        ],
    }

    buttons = [
        {
            "title": "Начать игру",
            "hide": True
        },
        {
            "title": "Что это за игра?",
            "hide": True
        },
        {
            "title": "Правила",
            "hide": True
        },
        {
            "title": "Нет, я не хочу играть",
            "hide": True
        },
        {
            "title": "Начать игру со всеми поколениями",
            "hide": True
        },
        {
            "title": "Начать игру с 1 поколения",
            "hide": True
        },
        {
            "title": "Начать игру с 2 поколения",
            "hide": True
        },
        {
            "title": "Начать игру с 3 поколения",
            "hide": True
        },
        {
            "title": "Начать игру с 4 поколения",
            "hide": True
        },
        {
            "title": "Начать игру с 5 поколения",
            "hide": True
        },
        {
            "title": "Начать игру с 6 поколения",
            "hide": True
        },
        {
            "title": "Начать игру с 7 поколения",
            "hide": True
        },
        {
            "title": "Начать игру с 8 поколения",
            "hide": True
        },
    ]

    state = {
        'screen': 'welcome_message',
        'start_game_question': True,
        'game_running': False,
        'generation': None,
        'buttons': buttons
    }

    user_state_update = {
        'start_gen_question': False,
        'incorrect_choice': False,
        'right_choice': False,
        'start_game': False,
        'current_pokemon': None,
        'old_pokemon': None,
        'current_card': None,
        'current_buttons': buttons,
        'score': 0,
        'generation': None
    }

    return make_response(text, tts=tts, buttons=buttons, card=card, state=state,
                         user_state_update=user_state_update)


def abort_game(event):
    text = random.choices(
        list(abort_game_phrases.keys()),
        weights=list(abort_game_phrases.values())
    )[0]

    tts = None

    if text == 'Прощай, я буду скучать. Надеюсь ещё раз вас услышать.':
        tts = '<speaker audio="dialogs-upload/b4eadf08-ca7d-4fba-a5d0-95415be3a3cb/9b376eb1-8f08-4817-b4e3-331d7e20fa5f.opus">. ' + \
              'Надеюсь ещё раз вас услышать.'

    state = event['state'][STATE_REQUEST_KEY]
    user = event.get('state', {}).get('user', {})

    if not state.get('current_pokemon') is None:
        old_pokemon = user['current_pokemon']

        delete_image(
            oauth_code='y0_AgAAAAAU2kKeAAT7owAAAADez9M6baNM9fzIR32KsI4uBjYB3XZfmLo',
            dialog_id='b4eadf08-ca7d-4fba-a5d0-95415be3a3cb',
            image_id=old_pokemon['closed_img']['id'],
        )

    user_state_update = {
        'start_gen_question': False,
        'incorrect_choice': False,
        'right_choice': False,
        'start_game': False,
        'current_pokemon': None,
        'old_pokemon': None,
        'current_card': None,
        'current_buttons': None,
        'score': 0,
        'generation': None
    }

    return make_response(text, tts=tts, state=state, user_state_update=user_state_update, end_session=True)


def fallback(event, text='Извините, я вас не поняла.', tts=None,
             card_title=None):
    state = event['state'].get(STATE_REQUEST_KEY, {})
    buttons = state.get('buttons')
    user = event.get('state', {}).get('user', {})
    card = user.get('current_card')

    if (not card_title is None) and (not card is None):
        if card['type'] == 'BigImage':
            card['title'] = card_title

        elif card['type'] == 'ItemsList':
            card['header']['text'] = card_title

    return make_response(text, tts=tts, card=card, buttons=buttons,
                         state=state, user_state_update=user)


def nintendo_alert(event):
    state = event['state'][STATE_REQUEST_KEY]
    user = event.get('state').get('user', {})
    buttons = state.get('buttons')

    text = 'Мы сожалеем, что такая ситуация произошла.\n' + \
           'Сообщите о нарушении на нашу почту "damir.ernazarov.yesspeace@gmail.com" и мы тут же всё исправим.'

    return make_response(text, state=state, buttons=buttons, user_state_update=user)


def handler(event, context):
    intents = event['request'].get('nlu', {}).get('intents')
    session = event.get('state', {f'{STATE_REQUEST_KEY}': {}}).get(STATE_REQUEST_KEY, {})
    user = event.get('state').get('user', {})
    message = str(event.get('request', {})['original_utterance']).lower()

    if event['session']['new'] is True:

        if 'start_over' in intents:
            if not session.get('current_pokemon') is None:
                old_pokemon = user['current_pokemon']

                delete_image(
                    oauth_code='y0_AgAAAAAU2kKeAAT7owAAAADez9M6baNM9fzIR32KsI4uBjYB3XZfmLo',
                    dialog_id='b4eadf08-ca7d-4fba-a5d0-95415be3a3cb',
                    image_id=old_pokemon['closed_img']['id'],
                )

            return welcome_message(event)

        elif 'start_gen_question' in user and user.get('start_gen_question') is True:
            return start_gen_question(event)

        elif 'start_game' in user and user.get('start_game') is True:
            return repeat_start_game(event)

        elif 'incorrect_choice' in user and user.get('incorrect_choice') is True:
            return repeat_incorrect_choice(event)

        elif 'right_choice' in user and user.get('right_choice') is True:
            return repeat_right_choice(event)

        else:
            return welcome_message(event)

    if 'what_is_the_game' in intents:
        return what_is_the_game(event)

    elif 'which_rules' in intents:
        return which_rules(event)

    elif 'start_over' in intents:
        if not session.get('current_pokemon') is None:
            old_pokemon = user['current_pokemon']

            delete_image(
                oauth_code='y0_AgAAAAAU2kKeAAT7owAAAADez9M6baNM9fzIR32KsI4uBjYB3XZfmLo',
                dialog_id='b4eadf08-ca7d-4fba-a5d0-95415be3a3cb',
                image_id=old_pokemon['closed_img']['id'],
            )

        return welcome_message(event)

    elif "Мы Nintendo и наши права были нарушены.".lower() in message:
        return nintendo_alert(event)

    elif 'abort_game' in intents:
        return abort_game(event)

    elif 'start_game' in intents:
        return start_gen_question(event)

    elif 'start_game_gen_selected' in intents:
        return start_game(event)

    elif 'whos_the_pokemon' in intents:
        return whos_the_pokemon(event)

    elif 'repeat_pokemon' in intents:
        if 'start_game' in user and user.get('start_game') is True:
            return repeat_start_game(event)

        elif 'incorrect_choice' in user and user.get('incorrect_choice') is True:
            return repeat_incorrect_choice(event)

        elif 'right_choice' in user and user.get('right_choice') is True:
            return repeat_right_choice(event)

        else:
            text, tts = random.choices(
                list(no_img_to_repeat_text_tts.keys()),
                weights=list(no_img_to_repeat_text_tts.values())
            )[0]

            return fallback(event, text=text, tts=tts)

    elif session.get('start_game_question') is True:
        if 'YANDEX.CONFIRM' in intents:
            return start_gen_question(event)

        elif 'YANDEX.REJECT' in intents:
            return abort_game(event)

        elif 'YANDEX.HELP' in intents:
            text, tts = random.choices(
                list(help_in_start_text_tts.keys()),
                weights=list(help_in_start_text_tts.values())
            )[0]
            return fallback(event, text=text, tts=tts)

        elif 'start_game' in intents:
            return start_gen_question(event)

        else:
            text, tts = random.choices(
                list(start_game_question_fallback_text_tts.keys()),
                weights=list(start_game_question_fallback_text_tts.values())
            )[0]

            return fallback(event, text=text, tts=tts)

    elif session.get('start_gen_question') is True:
        entities = event['request'].get('nlu', {}).get('entities', [{"type": None}])

        if (len(entities) != 0) and (entities[0]['type'] == 'YANDEX.NUMBER'):
            return start_game(event)

        elif ('YANDEX.REJECT' in intents) or ('abort_game' in intents):
            return abort_game(event)

        else:
            text, tts = random.choices(
                list(gen_question_fallback_text_tts.keys()),
                weights=list(gen_question_fallback_text_tts.values())
            )[0]
            return fallback(event, text=text, tts=tts)


    elif session.get('game_running') is True:
        return check_response(event)

    else:
        return fallback(event)
