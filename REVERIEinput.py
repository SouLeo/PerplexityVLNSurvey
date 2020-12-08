import pathlib
from pathlib import Path
import json
from nltk.tokenize import sent_tokenize
import collections
import string


def load_REVERIE():
    cwd = pathlib.Path().absolute()
    base_REVERIE = Path('REVERIE')
    concat_path = cwd / base_REVERIE

    filenames = list(concat_path.glob('*.json'))
    exs_jsons = []  # LIST OF JSON OBJECTS OF EXISTING UMRF NODES IN GRAPH
    for filename in filenames:
        with open(filename) as infile:
            exs_jsons.append(json.load(infile))

    instructions = []
    for ex in exs_jsons:
        for task in ex:
            for dialogue_entries in task['instructions']:
                sents = dialogue_entries.replace('%', '')
                sents = sents.replace('-', '')
                list_of_sentences = sent_tokenize(sents)
                instructions += list_of_sentences

    # full_text = " ".join(instructions)
    # full_text = full_text.translate(str.maketrans('', '', string.punctuation))
    # c = dict(collections.Counter(full_text.split()))
    # vocab = {key:val for key, val in c.items() if val > 100}
    # vocab_list = list(vocab.keys())
    #
    # with open('REVERIE_vocab.txt', 'w') as file:
    #     for word in vocab_list:
    #         file.write('%s\n' % word)
    return instructions
