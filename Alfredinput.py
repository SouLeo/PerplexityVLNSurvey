import pathlib
from pathlib import Path
import json
import string
from nltk.tokenize import sent_tokenize
import collections

def load_Alfred():
    cwd = pathlib.Path().absolute()
    base_alfred = Path('Alfred')
    alfred_data_dir = cwd / base_alfred

    split_list = [x for x in alfred_data_dir.iterdir() if x.is_dir()]
    trial_list = []
    for split in split_list:
        trial_list += [x for x in split.iterdir() if x.is_dir()]

    examples = []
    for trial in trial_list:
        filenames = list(trial.glob('*.json'))
        for file in filenames:
            with open(file) as infile:
                examples.append(json.load(infile))

    annotation_list = []
    for example in examples:
        annotation_list += example['turk_annotations']['anns']

    sentences = []
    for annotation in annotation_list:
        sentences.append(annotation['task_desc'])
        high_descs = annotation['high_descs']
        for desc in high_descs:
            sentences.append(desc)

    sentences_tokenized = []
    for sentence in sentences:
        sentences_tokenized += sent_tokenize(sentence)

    # full_text = " ".join(sentences_tokenized)
    # full_text = full_text.translate(str.maketrans('', '', string.punctuation))
    # c = dict(collections.Counter(full_text.split()))
    # vocab = {key:val for key, val in c.items() if val > 100}
    # vocab_list = list(vocab.keys())
    #
    # with open('ALFRED_vocab.txt', 'w') as file:
    #     for word in vocab_list:
    #         file.write('%s\n' % word)

    return sentences_tokenized
