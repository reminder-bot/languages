from os import listdir
import json

strings = {}
languages = {}

for fn in listdir('.'):
    if fn.startswith('strings_'):
        with open(fn, 'r', encoding='utf-8') as f:
            a = f.read()

            lang_strings = eval(a)

            strings[fn[8:10]] = lang_strings

            languages[fn[8:10]] = lang_strings['__full__']

strings_compiled = {}

for language, s in strings.items():
    out = {}
    for key, value in s.items():
        if isinstance(value, str) and not (key.startswith('__') and key.endswith('__')):
            out[key] = value

        elif isinstance(value, dict):
            for key2, value2 in value.items():
                out['{}/{}'.format(key, key2)] = value2

    strings_compiled[language] = out

compiled = {'languages': languages, 'strings': strings_compiled}

with open('out.json', 'w') as out_file:
    json.dump(compiled, out_file)
