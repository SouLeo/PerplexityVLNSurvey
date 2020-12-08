import pathlib
from pathlib import Path
import json
from nltk.tokenize import sent_tokenize
import string
import collections


def load_R2R():
    cwd = pathlib.Path().absolute()
    base_R2R_path_R2R = Path('R2R')
    base_R2R_path_data = Path('data')
    concat_path = cwd / base_R2R_path_R2R / base_R2R_path_data

    filenames = list(concat_path.glob('*.json'))
    exs_jsons = []  # LIST OF JSON OBJECTS OF EXISTING UMRF NODES IN GRAPH
    for filename in filenames:
        with open(filename) as infile:
            contents = exs_jsons.append(json.load(infile))

    instruction_list = []
    for instructions in exs_jsons:  # gather list of json objects from single training data
        for instruction in instructions:
            instruction_list.append(instruction['instructions'])

    sentences = []
    for ex in instruction_list:
        for user_response in ex:
            sentences += sent_tokenize(user_response)

    # full_text = " ".join(sentences)
    # full_text = full_text.translate(str.maketrans('', '', string.punctuation))
    # c = dict(collections.Counter(full_text.split()))
    # vocab = {key:val for key, val in c.items() if val > 100}
    # vocab_list = list(vocab.keys())
    #
    # with open('R2R_vocab.txt', 'w') as file:
    #     for word in vocab_list:
    #         file.write('%s\n' % word)

    return sentences
