import argparse
from data_utils import load_data, data_generator, tokenizer
import tensorflow as tf
import numpy as np
import os
import random
from config import config
import sys
import json
import pickle
from tqdm import tqdm
from bert4keras.backend import K, keras
from utils import model, CRF, NER, predict_label, read_sents
from metrics import classification_report, f1_score, precision_score, recall_score, accuracy_score
from build_graph import get_entities, get_relations, build_json, build_kg

parser = argparse.ArgumentParser()
parser.add_argument('--mode', type=str, default='demo', help='train/eval/output/BuildGraph/demo')
args = parser.parse_args()

# 训练数据
if args.mode == 'train':
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

    train_data, _ = load_data(config['--train_data'], max_len)
    valid_data, _ = load_data(config['--test_data'], max_len)

    train_generator = data_generator(train_data, batch_size)
    valid_generator = data_generator(valid_data, batch_size * 5)

    checkpoint = keras.callbacks.ModelCheckpoint(checkpoint_save_path,
                                                 monitor='val_sparse_accuracy',
                                                 verbose=1,
                                                 save_best_only=True,
                                                 mode='max')

    model.fit(train_generator.forfit(),
              steps_per_epoch=len(train_generator),
              validation_data=valid_generator.forfit(),
              validation_steps=len(valid_generator),
              epochs=epochs,
              callbacks=[checkpoint])

    print(K.eval(CRF.trans))
    print(K.eval(CRF.trans).shape)
    pickle.dump(K.eval(CRF.trans), open(config['--crf_save_path'], 'wb'))

# 评估
if args.mode == 'eval':
    model.load_weights(config['--checkpoint_save_path'])
    NER.trans = pickle.load(open(config['--crf_save_path'], 'rb'))
    test_data, y_true = load_data(config['--test_data'], config['--max_len'])
    y_pred = predict_label(test_data)

    f1 = f1_score(y_true, y_pred, suffix=False)
    p = precision_score(y_true, y_pred, suffix=False)
    r = recall_score(y_true, y_pred, suffix=False)
    acc = accuracy_score(y_true, y_pred)

    print("f1_score: {:.4f}, "
          "precision_score: {:.4f}, "
          "recall_score: {:.4f}, "
          "accuracy_score: {:.4f}".format(f1, p, r, acc))
    print(classification_report(y_true, y_pred, digits=4, suffix=False))

# 输出抽取好的实体
if args.mode == 'output':
    input_path = config['--input_path']  # 此处用于示例，直接用dev.conll来输出，抽取新文件时，需再config里改成相应新路径
    output_path = config['--output_path1']
    max_len = config['--max_len']
    model.load_weights(config['--checkpoint_save_path'])
    NER.trans = pickle.load(open(config['--crf_save_path'], 'rb'))
    sents = read_sents(input_path)

    JSON_node_list = []
    idx = 0
    for line in sents:
        sent = ''
        for i in line:
            sent += i[0]
        entity = NER.recognize(sent)
        for ent in entity:
            JSON_node = {"type": "node",
                         "id": "{}".format(idx),
                         "labels": "{}".format(ent[-1]),
                         "properties": {"name": "{}".format(ent[0])}}
            JSON_node_list.append(JSON_node)
            idx += 1
    # print(JSON_node_list)
    json.dump(JSON_node_list, open(output_path, 'w', encoding='utf-8'), ensure_ascii=False)

# 构建图谱
if args.mode == 'BuildGraph':
    input_path = config['--demo']  # 此处用于示例，用于处理标注好的数据，对于未标注新数据，需采用output部分来做
    output_path = config['--output']

    # excel输出路径
    entities_output_path = config['--xlsx_ent_path']
    relations_output_path = config['--xlsx_rel_path']

    entity = get_entities(input_path)
    p_w_relation, w_l_relation, p_l_relation, w_p_relation, l_w_relation, l_p_relation = get_relations(input_path)

    # 输出为xlsx文件
    # entity_df = pd.DataFrame(entity, columns=['id', 'name', 'label'])
    # entity_df.to_excel(entities_output_path, sheet_name="nodes", index=None)
    #
    # relation_data = np.vstack((p_w_relation, w_l_relation, p_l_relation, w_p_relation, l_w_relation, l_p_relation))
    # relation_df = pd.DataFrame(relation_data, columns=['start_name', 'relation', 'end_name'])
    # relation_df.to_excel(relations_output_path, sheet_name="relations", index=None)

    # 输出为json文件
    JSON_node_list, JSON_relation_list = build_json(entity,
                                                    p_w_relation,
                                                    w_l_relation,
                                                    p_l_relation,
                                                    w_p_relation,
                                                    l_w_relation,
                                                    l_p_relation)
    kg = build_kg(JSON_node_list, JSON_relation_list)
    json.dump(kg, open(output_path, 'w', encoding='utf-8'), ensure_ascii=False)

# 简单例子，用于演示
if args.mode == 'demo':
    model.load_weights(config['--checkpoint_save_path'])
    NER.trans = pickle.load(open(config['--crf_save_path'], 'rb'))
    # pred = NER.recognize('柴油机汽缸盖装配技术涉及温度传感器、曲轴、气缸等多个部件')
    pred = NER.recognize('一二级分离系统的架构权衡是级间热分离问题，需要进行动态仿真，保证质量，爆炸螺栓与分离火箭不同时使用，采用约束满足问题方法')
    print(pred)
