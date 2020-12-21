import json
import sys

strings = {}

lang = sys.argv[1]

with open('strings_{}.py'.format(lang.upper()), 'r', encoding='utf-8') as f:
    a = f.read()

    lang_strings = eval(a)

    for key, value in lang_strings.items():
        if isinstance(value, str) and not (key.startswith('__') and key.endswith('__')):
            strings[key] = value.strip()

        elif isinstance(value, dict):
            for key2, value2 in value.items():
                strings['{}/{}'.format(key, key2)] = value2.strip()


with open('{}.json'.format(lang.upper()), 'w') as out_file:
    json.dump(strings, out_file, indent=2)
