import pathlib
from pathlib import Path
import json
from nltk.tokenize import sent_tokenize
import collections
import string


def load_CHAI():
    cwd = pathlib.Path().absolute()
    base_CHAI_path = Path('CHAI')
    concat_path = cwd / base_CHAI_path

    filenames = list(concat_path.glob('*.txt'))
    contents = []  # LIST OF JSON OBJECTS OF EXISTING UMRF NODES IN GRAPH
    for filename in filenames:
        with open(filename) as infile:
            contents.append(infile.read())

    sentences = []
    for instructions in contents:
        instructions = instructions.replace('%', '')
        instructions = instructions.replace('-', '')
        sentences += sent_tokenize(instructions)

    full_text = " ".join(sentences)
    full_text = full_text.translate(str.maketrans('', '', string.punctuation))
    c = dict(collections.Counter(full_text.split()))
    vocab = {key:val for key, val in c.items() if val > 100}
    vocab_list = list(vocab.keys())

    with open('CHAI_vocab.txt', 'w') as file:
        for word in vocab_list:
            file.write('%s\n' % word)
    return sentences