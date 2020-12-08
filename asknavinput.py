import pathlib
from pathlib import Path
import json
import collections
import string
from nltk.tokenize import sent_tokenize


def load_asknav():
    cwd = pathlib.Path().absolute()
    base_asknav = Path('asknav')
    concat_path = cwd / base_asknav

    filenames = list(concat_path.glob('*.json'))
    exs_jsons = []  # LIST OF JSON OBJECTS OF EXISTING UMRF NODES IN GRAPH
    for filename in filenames:
        with open(filename) as infile:
            exs_jsons.append(json.load(infile))

    instructions = []
    for ex in exs_jsons:
        for task in ex:
            instructions += task['instructions']

    # full_text = " ".join(instructions)
    # full_text = full_text.translate(str.maketrans('', '', string.punctuation))
    # c = dict(collections.Counter(full_text.split()))
    # vocab = {key:val for key, val in c.items() if val > 100}
    # vocab_list = list(vocab.keys())
    #
    # with open('asknav_vocab.txt', 'w') as file:
    #     for word in vocab_list:
    #         file.write('%s\n' % word)
    return instructions
