import wikipedia


def main(string_input, **keyword_password):
    lang = keyword_password.get('lang')
    wikipedia.set_lang(lang)

    limit = keyword_password.get('limit')
    if limit is not None:
        try:
            x = wikipedia.search(string_input)[:limit]
        except IndexError:
            print('Not found.')
    else:
        x = wikipedia.search(string_input)[0]
 
    for a in x:
        i = wikipedia.page(a)
        url = i.url
        print(f'{""*25}\n{a}:\n{wikipedia.summary(a, sentences=1)}\n{url}')


if __name__ == '__main__':
    x = input('search: ')
    y = input('lang: ')
    z = int(input('limit: '))
    a = main(x, lang=y, limit=z)

