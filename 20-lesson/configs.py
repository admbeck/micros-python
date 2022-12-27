LANGUAGES = {
    'ru': 'Русский',
    'en': 'Английский',
    'uz': 'Узбекский',
    'de': 'Немецкий',
    'fr': 'Француский',
    'it': 'Италиянский'
}


def get_keys(value):
    for k, v in LANGUAGES.items():
        if v == value:
            return k