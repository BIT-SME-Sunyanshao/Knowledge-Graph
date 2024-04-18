from tqdm import tqdm
from metrics import *
from data_utils import tokenizer, id2label, num_labels
import tensorflow as tf
from bert4keras.backend import K, keras, search_layer
from bert4keras.snippets import ViterbiDecoder, to_array
from build_model import bert_bilstm_crf
from config import config
import os
import random

seed = config['--seed']
tf.random.set_seed(seed)
np.random.seed(seed)
random.seed(seed)
os.environ['PYTHONHASHSEED'] = str(seed)

epochs = config['--epoch']
max_len = config['--max_len']
batch_size = config['--batch_size']
lstm_units = config['--lstm_units']
drop_rate = config['--dropout']
leraning_rate = config['--lr']
config_path = config['--bert_config_path']
checkpoint_path = config['--bert_checkpoint_path']
checkpoint_save_path = config['--checkpoint_save_path']
crt_save_path = config['--crf_save_path']


class NamedEntityRecognizer(ViterbiDecoder):
    """命名实体识别器
    """

    def recognize(self, text):
        tokens = tokenizer.tokenize(text)
        while len(tokens) > max_len:
            tokens.pop(-2)
        mapping = tokenizer.rematch(text, tokens)
        token_ids = tokenizer.tokens_to_ids(tokens)
        segment_ids = [0] * len(token_ids)
        token_ids, segment_ids = to_array([token_ids], [segment_ids])  # ndarray
        nodes = model.predict([token_ids, segment_ids])[0]  # [sqe_len,23]
        labels = self.decode(nodes)  # id [sqe_len,], [0 0 0 0 0 7 8 8 0 0 0 0 0 0 0]
        entities, starting = [], False
        for i, label in enumerate(labels):
            if label > 0:
                if label % 2 == 1:
                    starting = True
                    entities.append([[i], id2label[(label - 1) // 2]])
                elif starting:
                    entities[-1][0].append(i)
                else:
                    starting = False
            else:
                starting = False
        return [(text[mapping[w[0]][0]:mapping[w[-1]][-1] + 1], l) for w, l in entities]


model, CRF = bert_bilstm_crf(config_path, checkpoint_path, num_labels, lstm_units, drop_rate, leraning_rate)
NER = NamedEntityRecognizer(trans=K.eval(CRF.trans), starts=[0], ends=[0])


# 预测标签
def predict_label(data):
    y_pred = []
    for d in tqdm(data):
        text = ''.join([i[0] for i in d])
        pred = NER.recognize(text)

        label = ['O' for _ in range(len(text))]
        b = 0
        for item in pred:
            word, typ = item[0], item[1]
            start = text.find(word, b)
            end = start + len(word)
            label[start] = 'B-' + typ
            for i in range(start + 1, end):
                label[i] = 'I-' + typ
            b += len(word)

        y_pred.append(label)

    return y_pred


def read_corpus(filepath):
    """ Read corpus from the given file path.
    Args:
        filepath: file path of the corpus
    Returns:
        sentences: a list of sentences, each sentence is a list of str
        tags: corresponding tags
    """
    sentences, tags = [], []
    sent, tag = [], []
    with open(filepath, 'r', encoding='utf8') as f:
        for line in f:
            if line == '\n':
                if len(sent) > 1:
                    sentences.append(sent)
                    tags.append(tag)
                sent, tag = [], []
            else:
                line = line.split()
                sent.append(line[:1])
                tag.append(line[1:])
    return sentences, tags

def read_sents(filepath):
    """ Read corpus from the given file path.
    Args:
        filepath: file path of the corpus
    Returns:
        sentences: a list of sentences, each sentence is a list of str
        tags: corresponding tags
    """
    sentences = []
    sent = []
    with open(filepath, 'r', encoding='utf8') as f:
        for line in f:
            if line == '\n':
                if len(sent) > 1:
                    sentences.append(sent)
                sent = []
            else:
                line = line.split()
                sent.append(line[:1])
    return sentences
