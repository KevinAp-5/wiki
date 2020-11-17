import wikipedia as wiki


def main(string_input, **keyword_password):
    lang = keyword_password.get('lang')
    wiki.set_lang(lang)

    limit = keyword_password.get('limit')
    if limit is not None:
        try:
            results = wiki.search(string_input)[:limit]
        except IndexError:
            print('Not found.')
    else:
        results = wiki.search(string_input)[0]

    for result in results:
        i = wiki.page(result)
        url = i.url
        print(f'{result}:\n{wiki.summary(result, sentences=2)}\n{url}')


if __name__ == '__main__':
    x = input('search: ')
    y = input('lang: ')
    z = int(input('limit: '))
    a = main(x, lang=y, limit=z)
