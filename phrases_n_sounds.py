abort_game_phrases = {
    'До свидания, ещё увидимся.': 9,
    'До скорой встречи, ещё услышимся.': 9,

    'Жаль, что вы не хотите продолжить. До скорой встречи, ещё услышимся.': 7,
    'Ничего, я не расстраиваюсь, это просто слёзы. До свидания': 7,

    'Прощай, я буду скучать. Надеюсь ещё раз вас услышать.': 6,
}

start_gen_question_phrases = {
    'Вы забыли сказать из какого поколения вы бы хотели угадывать. ' + \
    'Или может хотите из всех сразу? Кстати, их 8': 7,
    'Вы забыли сказать поколение. ' + \
    'Или может хотите все сразу? Кстати, их 8': 7,
    'Вы забыли про поколения. ' + \
    'Или может хотите играть по всем сразу? Кстати, их 8': 7,

    'Сперва выберете поколение. У нас целых 8': 9,
    'Какое поколение? Кстати, их 8': 9,

    'Если хотели начать игру со всеми поколениями, то следовало сказать: "Начать игру со всеми сразу". ' + \
    'Ну так, какое поколение из восьми выберете?': 6,

}

welcome_message_phrases_tts = {
    'Приветствуем вас в навыке "Силуэты Карманных Монстров". С чего бы вы хотели начать?': 7,
    'Приветствуем вас в навыке "Силуэты Карманных Монстров". Начнём?': 7,
    'Привет, на связи навык "Силуэты Карманных Монстров". Начнём?': 7,
    'П+ика п+ика, приветствуем вас в навыке "Силуэты Карманных Монстров". Начнём?': 7,
    'Й+оу, на связи навык "Силуэты Карманных Монстров". С чего бы вы хотели начать?': 7,

    'Здравствуйте, хотите стать лучшем тренером? Тогда вам необходимо играть в эту игру. ' + \
    'Она научит вас различать любого карманного монстра за секунду. Начнем?': 9,
    'Привет, хотите стать лучшем тренером? Тогда вам необходимо играть в эту игру. ' + \
    'Она научит вас различать любого карманного монстра за секунду. Начнем?': 9,
    'Й+оу, хотите стать лучшем тренером? Тогда вам необходимо играть в эту игру. ' + \
    'Она научит вас различать любого карманного монстра за секунду. Начнем?': 9,
    'Кчау, хотите стать лучшем тренером? Тогда вам необходимо играть в эту игру. ' + \
    'Она научит вас различать любого карманного монстра за секунду. Начнем?': 9,

    'Я вижу вы сильный тренер. Вам видимо и объяснять ничего и нин+адо. Начнём игру?': 5,
}

welcome_message_phrases_title = {
    'Приветствуем вас в навыке "Силуэты Карманных Монстров"': 9,
    'Добро пожаловать в навык "Силуэты Карманных Монстров"': 9,
    'Привет-привет это навык "Силуэты Карманных Монстров"': 9,
    'Пика-пика, добро пожаловать в навык "Силуэты Карманных Монстров"': 5,
    'Йоу, врата в навык "Силуэты Карманных Монстров" открыты': 5,
    'Йоу, швепс, рад видеть тебя в навыке "Силуэты Карманных Монстров"': 3,
}

right_choice_phrases_text = {
    'Молодец, ты отгадал, это был {}. Давай продолжим.': 9,
    'Правильно, это был {}. А это что за Карманный Монстр?': 9,
    'Да, это был {}. А это кто такой?': 7,
    'Конечно, это был {}. А это что за Карманный Монстр?': 7,
}

right_choice_phrases_tts = {
    '<speaker audio="dialogs-upload/b4eadf08-ca7d-4fba-a5d0-95415be3a3cb/67c21013-e418-4608-83ab-d1d684088d40.opus">.': 7,
    ' ': 9
}

incorrect_choice_phrases_tts = {
    "Вы не угадали. Это был {}" + \
    "sil <[500]> Не расстраивайтесь, даже +я ещё не всех выучила. " + \
    "sil <[600]> Хотите попробовать ещё раз? С обнулением счёта.": 9,

    '<speaker audio="dialogs-upload/b4eadf08-ca7d-4fba-a5d0-95415be3a3cb/30f0bf2b-4714-400c-b06d-ac19153bf021.opus">. ' + \
    "Вы не угадали. Это был {}" + \
    "sil <[600]> Хотите начать игру ещё раз, с обнулением счёта?": 7,

    '<speaker audio="dialogs-upload/b4eadf08-ca7d-4fba-a5d0-95415be3a3cb/9a3cdd4e-5d31-4999-86d4-5664934c80c7.opus">. ' + \
    "А вот и нет. Это был {}" + \
    "sil <[600]> Как насчёт того, чтобы попробовать ещё раз, с обнулением счёта?": 6,
}

incorrect_choice_phrases_title = {
    'К сожалению, вы не угдали.': 9,
    'Кажется, вы не угадали': 9,

    'Увы, но нет, это не тот карманный монстр.': 8,
    'К сожалению, нет, это не тот карманный монстр.': 8,

    'Неправильно, но не расстраивайтесь! Ведь всех не запомнить.': 7,

    'Человек учится на своих ошибках. К сожалению, это не ваш случай.': 1,
}

whos_the_pokemon_text_and_tts = {  # first - text, second - tts
    (
        '«Покемо́н» (от англ. Pocket Monster — «Карманный монстр») - существо, обладающее сверхъестественными способностями. \n' + \
        'Вообще "покемон" - это целая медиафраншиза, которая впервые появился как пара игр, ' + \
        'а на сегодняшний день она имеет аниме, мангу, коллекционную карточную игру и прочие сопутствующие товары. \n' + \
        'Ну как вам, хотите сыграть в игру "Силуэты Карманных Монстров"',

        '"Покем+он" от английского Pocket Monster — "Карманный монстр" - существо, обладающее сверхъестественными способностями. ' + \
        'Вообще покем+он - это целая медиафраншиза, которая впервые появился как пара игр, ' + \
        'а на сегодняшний день она имеет аниме, мангу, коллекционную карточную игру и прочие сопутствующие товары. ' + \
        'Ну как вам, xотите сыграть в игру "Силуэты Карманных Монстров"?'
    ): 9,
    (
        '«Покемон» (от англ. Pocket Monster — «Карманный монстр») - это замечательный мир, наполненный разнообразными существами, ' + \
        'каждое из которых обладает своими уникальными способностями. ' + \
        'Неудивительно, что эти игры и франшиза так популярны во всем мире. ' + \
        'Ну как вам, хотите сыграть в игру «Силуэты Карманных Монстров»',

        '"Покем+он" от английского Pocket Monster — "Карманный монстр" - это замечательный мир, наполненный разнообразными существами, ' + \
        'каждое из которых обладает своими уникальными способностями. ' + \
        'Неудивительно, что эти игры и франшиза так популярны во всем мире. ' + \
        'Ну как вам, хотите сыграть в игру "Силуэты Карманных Монстров"',
    ): 8,
    (
        '«Покемон» (от англ. Pocket Monster — «Карманный монстр») - это популярная японская франшиза, созданная компанией Nintendo. ' + \
        'Каждый покемон имеет свои уникальные способности и характеристики, ' + \
        'их можно ловить и тренировать, чтобы сражаться с другими тренерами. ' + \
        'Что скажите, хотите сыграть в игру «Силуэты Карманных Монстров»',

        '"Покем+он" от английского Pocket Monster — "Карманный монстр" - это популярная японская франшиза, созданная компанией Нинт+ендо. ' + \
        'Каждый покемон имеет свои уникальные способности и характеристики, ' + \
        'их можно ловить и тренировать, чтобы сражаться с другими тренерами. ' + \
        'Что скажите, хотите сыграть в игру "Силуэты Карманных Монстров"',
    ): 8,
}

which_rules_text = {
    'Правила весьма просты.': 8,
    'Правила очень простые.': 8,

    'Вот правила для игры "Силуэты Карманных Монстров"': 9,

    'Вот положение о правилах игры "Силуэты Карманных Монстров"': 9,
}

what_is_the_game_text = {
    '"Силуэты Карманных Монстров" — игра-викторина по карманным монстрам. \n' + \
    'Вам будет предложено угадывать их по силуэтам. \n' + \
    'Вы можете отвечать, говоря имена или нажимая на кнопки. \n' + \
    'Вы можете выбрать поколение — их 8. Хотите сыграть?': 9,

    '"Силуэты Карманных Монстров" — игра-викторина по карманным монстрам. \n' + \
    'Вы будете угадывать монстров по их силуэтам, используя их имена или нажимая на кнопки. \n' + \
    'Не забывайте, что в игре 8 поколений монстров. Готовы начать игру?': 9,

    '"Силуэты Карманных Монстров" — игра-викторина по карманным монстрам, где вам нужно угадывать карманных монстров по их силуэтам. \n' + \
    'Не забудьте, что вы можете называть их имена или нажимать на соответствующие кнопки. \n' + \
    'В игре 8 поколений монстров. Готовы попробовать?"': 9,

}

gen_question_fallback_text_tts = {
    (
        'Выберете поколение из промежутка от 1 до 8',
        'Выберете поколение из промежутка от одного до восьми'
    ): 9,
    (
        'Кажется, что такого поколения я не знаю. Выберете поколение из промежутка от 1 до 8',
        'Кажется, что такого поколения я не знаю. Выберете поколение из промежутка от одного до восьми'
    ): 8,
    (
        'Ой-ой, я такого поколения не знаю. Выберете поколение из промежутка от 1 до 8',
        'Ой ёй, я такого поколения не знаю. Выберете поколение из промежутка от одного до восьми'
    ): 7,
    (
        'Не похоже, что это поколение из промежутка от 1 до 8',
        'Не похоже, что это поколение из промежутка от одного до восьми'
    ): 8,
}

start_game_question_fallback_text_tts = {
    (
        'Извините, я вас не поняла, если хотите сыграть скажите "Начать игру".',
        'Извините, я вас не поняла, если хотите сыграть скажите "Начать игру".'
    ): 10,
    (
        'Что-что? Хотите сыграть? Тогда скажите, например, "Начать игру с 1 поколение".',
        'Что-что? Хотите сыграть? Тогда скажите, например, "Начать игру с перовго поколение".'
    ): 10,
    (
        'Что-что? Хотите сыграть? Тогда скажите, например, "Начать игру по всем поколениеям".',
        'Что-что? Хотите сыграть? Тогда скажите, например, "Начать игру по всем поколениеям".'
    ): 10,
    (
        '@пвы#24#лн@?: - Что-то понял? Говори нормально.',
        'Собака пых решётка 24 решётка лена собака?. Чё-то понял? Говори нормально.'
    ): 1,
    (
        '@пвы#24#лн@?: - Понятно? Базарь нормально.',
        'Собака пых решётка 24 решётка лена собака?. Понятно? Базарь нормально.'
    ): 1,
}

no_img_to_repeat_text_tts = {
    (
        'Кажется, что никакой картинки для повторной отправки нет.',
        'Кажется, что никакой картинки для повторной отправки нет.'
    ): 10,
    (
        'Извините, я не могу найти картинку для повторной отправки.',
        'Извините, я не могу найти картинку для повторной отправки.'
    ): 9,
    (
        'Я, конечно, пика-пика, но никакой картинки для повторной отправки не вижу',
        'Я, конечно, п+ика п+ика, но никакой картинки для повторной отправки не вижу'
    ): 5,
    (
        'Кажется, я не могу найти картинку для повторной отправки.',
        'Кажется, я не могу найти картинку для повторной отправки.'
    ): 8,
}

help_in_start_text_tts = {
    (
        'Слушайте внимательно. \n' + \
        'Это игровой навык "Силуэты Карманных Монстров". \n' + \
        'Вы можете сказать "Давай сыграем по 1 поколению", чтобы начать игру. \n' + \
        'Чтобы узнать правила игры скажите "Какие правила". \n' + \
        'Если вы не знаете что это за игра, то спросите "что это за игра?"\n' + \
        'Если вы не знаете что такое "карманный монстр", то спросите "Что такое карманный монстр".',

        'Слушайте внимательно. \n' + \
        'Это игровой навык "Силуэты Карманных Монстров". \n' + \
        'Вы можете сказать "Давай сыграем по первому поколению", чтобы начать игру. \n' + \
        'Чтобы узнать правила игры скажите "Какие правила". \n' + \
        'Если вы не знаете что это за игра, то спросите "Что это за игра?"\n' + \
        'Если вы не знаете что такое "карманный монстр", то спросите "Что такое карманный монстр".',
    ): 10,
    (
        'Сейчас объясню. \n' + \
        'Это игровой навык "Силуэты Карманных Монстров". \n' + \
        'Вы можете сказать "Давай сыграем по 1 поколению", чтобы начать игру. \n' + \
        'Чтобы узнать правила игры скажите "Какие правила". \n' + \
        'Если вы не знаете что это за игра, то спросите "что это за игра?"\n' + \
        'Если вы не знаете что такое "карманный монстр", то спросите "Что такое карманный монстр".',

        'Сейчас объясню. \n' + \
        'Это игровой навык "Силуэты Карманных Монстров". \n' + \
        'Вы можете сказать "Давай сыграем по первому поколению", чтобы начать игру. \n' + \
        'Чтобы узнать правила игры скажите "Какие правила". \n' + \
        'Если вы не знаете что это за игра, то спросите "Что это за игра?"\n' + \
        'Если вы не знаете что такое "карманный монстр", то спросите "Что такое карманный монстр".',
    ): 10,
    (
        'Слушайте внимательно. \n' + \
        'Это навык-игра "Силуэты Карманных Монстров". \n' + \
        'Вы можете сказать "Давай сыграем по всем поколениям", чтобы начать игру по всем поколениям. \n' + \
        'Чтобы узнать правила игры скажите "А какие правила игры". \n' + \
        'Если вы не знаете что это за игра, то спросите "Что это за игра?"\n' + \
        'Если вы не знаете что такое "карманный монстр", то спросите "Что такое карманный монстр".',

        'Слушайте внимательно. \n' + \
        'Это навык игра "Силуэты Карманных Монстров". \n' + \
        'Вы можете сказать "Давай сыграем по всем поколениям", чтобы начать игру по всем поколениям. \n' + \
        'Чтобы узнать правила игры скажите "А какие правила игры". \n' + \
        'Если вы не знаете что это за игра, то спросите "Что это за игра?"\n' + \
        'Если вы не знаете что такое "карманный монстр", то спросите "Что такое карманный монстр".',
    ): 10,
    (
        'Сейчас объясню. \n' + \
        'Это навык-игра "Силуэты Карманных Монстров". \n' + \
        'Вы можете сказать "Давай сыграем по всем поколениям", чтобы начать игру по всем поколениям. \n' + \
        'Чтобы узнать правила игры скажите "А какие правила игры". \n' + \
        'Если вы не знаете что это за игра, то спросите "Что это за игра?"\n' + \
        'Если вы не знаете что такое "карманный монстр", то спросите "Что такое карманный монстр".',

        'Сейчас объясню. \n' + \
        'Это навык игра "Силуэты Карманных Монстров". \n' + \
        'Вы можете сказать "Давай сыграем по всем поколениям", чтобы начать игру по всем поколениям. \n' + \
        'Чтобы узнать правила игры скажите "А какие правила игры". \n' + \
        'Если вы не знаете что это за игра, то спросите "Что это за игра?"\n' + \
        'Если вы не знаете что такое "карманный монстр", то спросите "Что такое карманный монстр".',
    ): 10,
}
