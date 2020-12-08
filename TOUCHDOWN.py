import pathlib
from pathlib import Path
import json
from nltk.tokenize import sent_tokenize
import string
import collections


def load_TOUCHDOWN():
    cwd = pathlib.Path().absolute()
    base_TOUCHDOWN = Path('TOUCHDOWN')
    concat_path = cwd / base_TOUCHDOWN

    filenames = list(concat_path.glob('*.json'))
    exs_jsons = []  # LIST OF JSON OBJECTS OF EXISTING UMRF NODES IN GRAPH
    for filename in filenames:
        with open(filename) as infile:
            for jsonObj in infile:
                jsonDict = json.loads(jsonObj)
                exs_jsons.append(jsonDict)

    instructions = []
    for ex in exs_jsons:
        sents = ex['full_text']
        sents = sents.replace('%', '')
        sents = sents.replace('-', '')
        list_of_sentences = sent_tokenize(sents)
        instructions += list_of_sentences
    # full_text = " ".join(instructions)
    # full_text = full_text.translate(str.maketrans('', '', string.punctuation))
    # c = dict(collections.Counter(full_text.split()))
    # vocab = {key:val for key, val in c.items() if val > 100}
    # vocab_list = list(vocab.keys())
    #
    # with open('TOUCHDOWN_vocab.txt', 'w') as file:
    #     for word in vocab_list:
    #         file.write('%s\n' % word)
    return instructions
