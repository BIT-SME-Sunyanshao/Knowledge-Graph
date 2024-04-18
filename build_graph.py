import json
import numpy as np
from utils import read_corpus
import pandas as pd


# 从文件中获取标签类型
def get_labels(file_path):
    with open(file_path, 'r', encoding='utf8') as f:
        labels_dict = json.load(f)
        labels_list = list(labels_dict['word2id'].keys())
        labels = []
        for i in labels_list:
            if i[0] == 'B':
                labels.append(i[-3:])
    return labels


# 获得P实体
def get_P_entities(sent, tags):
    # print(sent)
    P = []
    p = ''
    for i, (token, tag) in enumerate(zip(sent, tags)):
        if tag == 'B-P':
            p += token
            if i + 1 < len(sent):
                if tags[i + 1] == 'B-P':
                    P.append(p)
        if tag == 'I-P':
            p += token
            if i + 1 < len(sent):
                if tags[i + 1] != 'I-P':
                    P.append(p)
                    p = ''
        if tag not in ['I-P', 'B-P']:
            continue
    return P


# 获取W实体
def get_R_entities(sent, tags):
    R = []
    r = ''
    for i, (token, tag) in enumerate(zip(sent, tags)):
        if tag == 'B-R':
            r += token
            if i + 1 < len(sent):
                if tags[i + 1] == 'B-R':
                    R.append(r)
        if tag == 'I-R':
            r += token
            if i + 1 < len(sent):
                if tags[i + 1] != 'I-R':
                    R.append(r)
                    r = ''
        if tag not in ['I-R', 'B-R']:
            continue
    return R


# 获得L实体
def get_G_entities(sent, tags):
    G = []
    g = ''
    for i, (token, tag) in enumerate(zip(sent, tags)):
        if tag == 'B-G':
            g += token
            if i + 1 < len(sent):
                if tags[i + 1] == 'B-G':
                    G.append(g)
        if tag == 'I-G':
            g += token
            if i + 1 < len(sent):
                if tags[i + 1] != 'I-G':
                    G.append(g)
                    g = ''
        if tag not in ['I-G', 'B-G']:
            continue
    return G


# 获得E实体
def get_E_entities(sent, tags):
    E = []
    e = ''
    for i, (token, tag) in enumerate(zip(sent, tags)):
        if tag == 'B-E':
            e += token
            if i + 1 < len(sent):
                if tags[i + 1] == 'B-E':
                    E.append(e)
        if tag == 'I-E':
            e += token
            if i + 1 < len(sent):
                if tags[i + 1] != 'I-E':
                    E.append(e)
                    e = ''
        if tag not in ['I-E', 'B-E']:
            continue
    return E


# 获得F实体
def get_F_entities(sent, tags):
    F = []
    f = ''
    for i, (token, tag) in enumerate(zip(sent, tags)):
        if tag == 'B-F':
            f += token
            if i + 1 < len(sent):
                if tags[i + 1] == 'B-F':
                    F.append(f)
        if tag == 'I-F':
            f += token
            if i + 1 < len(sent):
                if tags[i + 1] != 'I-F':
                    F.append(f)
                    f = ''
        if tag not in ['I-F', 'B-F']:
            continue
    return F


# 获得Y实体
def get_Y_entities(sent, tags):
    Y = []
    y = ''
    for i, (token, tag) in enumerate(zip(sent, tags)):
        if tag == 'B-Y':
            y += token
            if i + 1 < len(sent):
                if tags[i + 1] == 'B-Y':
                    Y.append(y)
        if tag == 'I-Y':
            y += token
            if i + 1 < len(sent):
                if tags[i + 1] != 'I-Y':
                    Y.append(y)
                    y = ''
        if tag not in ['I-Y', 'B-Y']:
            continue
    return Y


# 合并重复节点
def fusion(entity_list):
    return np.unique(entity_list)


# 获取所有实体，并输出为表格
def get_entities(input_path):
    '''

    Args:
        input_path: 输入文件的路径
        output_path: 输出文件的路径

    '''
    sentences, tags = read_corpus(input_path)
    # print(len(sentences))
    sentences_list = []
    label_list = []
    for sent, tags in zip(sentences, tags):
        s = []
        t = []
        for token, tag in zip(sent, tags):
            for i, j in zip(token, tag):
                s.append(i)
                t.append(j)
        sentences_list.append(s)
        label_list.append(t)

    R_list = []
    P_list = []
    G_list = []
    E_list = []
    F_list = []
    Y_list = []
    for i, (line, tags) in enumerate(zip(sentences_list, label_list)):
        r = get_R_entities(line, tags)
        p = get_P_entities(line, tags)
        g = get_G_entities(line, tags)
        e = get_E_entities(line, tags)
        f = get_F_entities(line, tags)
        y = get_Y_entities(line, tags)

        for j in r:
            R_list.append(j)

        for j in p:
            P_list.append(j)

        for j in g:
            G_list.append(j)

        for j in e:
            E_list.append(j)

        for j in f:
            F_list.append(j)

        for j in y:
            Y_list.append(j)

        print("\r实体获取进度：{:.2%}".format((i + 1) / len(sentences_list)), end='')

    R_list = [x for x in R_list if x]  # 去掉列表中的空白元素
    R = []
    for line in R_list:
        save = ''
        for i in line:
            save += i
        R.append(save)
    R = np.array(R)[:, np.newaxis]
    # print(P)

    P_list = [x for x in P_list if x]
    P = []
    for line in P_list:
        save = ''
        for i in line:
            save += i
        P.append(save)
    P = np.array(P)[:, np.newaxis]
    # print(len(PER))

    G_list = [x for x in G_list if x]
    G = []
    for line in G_list:
        save = ''
        for i in line:
            save += i
        G.append(save)
    G = np.array(G)[:, np.newaxis]

    E_list = [x for x in E_list if x]
    E = []
    for line in E_list:
        save = ''
        for i in line:
            save += i
        E.append(save)
    E = np.array(E)[:, np.newaxis]

    F_list = [x for x in F_list if x]
    F = []
    for line in F_list:
        save = ''
        for i in line:
            save += i
        F.append(save)
    F = np.array(F)[:, np.newaxis]

    Y_list = [x for x in Y_list if x]
    Y = []
    for line in Y_list:
        save = ''
        for i in line:
            save += i
        Y.append(save)
    Y = np.array(Y)[:, np.newaxis]

    print('\n实体获取完成\n')

    # print(len(LOC))

    R = fusion(R)[:, np.newaxis]
    P = fusion(P)[:, np.newaxis]
    G = fusion(G)[:, np.newaxis]
    E = fusion(E)[:, np.newaxis]
    F = fusion(F)[:, np.newaxis]
    Y = fusion(Y)[:, np.newaxis]

    R_id = []
    R_label = []
    P_id = []
    P_label = []
    G_id = []
    G_label = []
    E_id = []
    E_label = []
    F_id = []
    F_label = []
    Y_id = []
    Y_label = []
    for i in range(len(R)):
        R_label.append('DecisionRequirementProblem')
        R_id.append('R' + str(i + 1))

    for i in range(len(P)):
        P_label.append('DecisonItemProblem')
        P_id.append('P' + str(i + 1))

    for i in range(len(G)):
        G_label.append('DecisionTargetProblem')
        G_id.append('G' + str(i + 1))

    for i in range(len(E)):
        E_label.append('DecisionEvent')
        E_id.append('E' + str(i + 1))

    for i in range(len(F)):
        F_label.append('ProblemSolvingMethod')
        F_id.append('F' + str(i + 1))

    for i in range(len(Y)):
        Y_label.append('DecisionConstraint')
        Y_id.append('Y' + str(i + 1))

    R_label = np.array(R_label)[:, np.newaxis]
    R_id = np.array(R_id)[:, np.newaxis]
    P_label = np.array(P_label)[:, np.newaxis]
    P_id = np.array(P_id)[:, np.newaxis]
    G_label = np.array(G_label)[:, np.newaxis]
    G_id = np.array(G_id)[:, np.newaxis]
    E_label = np.array(E_label)[:, np.newaxis]
    E_id = np.array(E_id)[:, np.newaxis]
    F_label = np.array(F_label)[:, np.newaxis]
    F_id = np.array(F_id)[:, np.newaxis]
    Y_label = np.array(Y_label)[:, np.newaxis]
    Y_id = np.array(Y_id)[:, np.newaxis]
    # print(label[:10])

    R_data = np.hstack((R_id, R, R_label))
    P_data = np.hstack((P_id, P, P_label))
    G_data = np.hstack((G_id, G, G_label))
    E_data = np.hstack((E_id, E, E_label))
    F_data = np.hstack((F_id, F, F_label))
    Y_data = np.hstack((Y_id, Y, Y_label))
    # print(data[:10])

    return R_data, P_data, G_data, E_data, F_data, Y_data


def get_relations(input_path):
    '''

    Args:
        input_path: 输入文件的路径 ———— './data/test.txt'
        output_path: 输出文件的路径 ———— './result/output.xlsx'

    '''
    sentences, tags = read_corpus(input_path)
    # print(len(sentences))
    sentences_list = []
    label_list = []
    for sent, tags in zip(sentences, tags):
        s = []
        t = []
        for token, tag in zip(sent, tags):
            for i, j in zip(token, tag):
                s.append(i)
                t.append(j)
        sentences_list.append(s)
        label_list.append(t)

    r_p_relation = []
    p_g_relation = []
    e_f_relation = []
    y_f_relation = []
    r_r_relation = []
    p_p_relation = []
    g_g_relation = []
    e_e_relation = []
    e_r_relation = []
    e_p_relation = []
    e_g_relation = []
    y_p_relation = []
    for i, (line, tags) in enumerate(zip(sentences_list, label_list)):
        r_p = []
        p_g = []
        e_f = []
        y_f = []
        r_r = []
        p_p = []
        g_g = []
        e_e = []
        e_r = []
        e_p = []
        e_g = []
        y_p = []
        r = get_R_entities(line, tags)
        p = get_P_entities(line, tags)
        g = get_G_entities(line, tags)
        e = get_E_entities(line, tags)
        f = get_F_entities(line, tags)
        y = get_Y_entities(line, tags)
        r = np.unique(r)
        p = np.unique(p)
        g = np.unique(g)
        e = np.unique(e)
        f = np.unique(f)
        y = np.unique(y)
        if len(r) != 0:
            for j in range(len(r) - 1):
                r_r.append(r[0])
                r_r.append('related')
                r_r.append(r[j + 1])
                r_r_relation.append(r_r)
                r_r = []

        if len(p) != 0:
            for j in range(len(p) - 1):
                p_p.append(p[0])
                p_p.append('related')
                p_p.append(p[j + 1])
                p_p_relation.append(p_p)
                p_p = []

        if len(g) != 0:
            for j in range(len(g) - 1):
                g_g.append(g[0])
                g_g.append('related')
                g_g.append(g[j + 1])
                g_g_relation.append(g_g)
                g_g = []

        if len(e) != 0:
            for j in range(len(e) - 1):
                e_e.append(e[0])
                e_e.append('related')
                e_e.append(e[j + 1])
                e_e_relation.append(e_e)
                e_e = []

        if len(r) != 0 and len(p) != 0:
            for j in r:
                for k in p:
                    r_p.append(j)
                    r_p.append('reasoning')
                    r_p.append(k)
                    r_p_relation.append(r_p)
                    r_p = []

        if len(p) != 0 and len(g) != 0:
            for j in p:
                for k in g:
                    p_g.append(j)
                    p_g.append('reasoning')
                    p_g.append(k)
                    p_g_relation.append(p_g)
                    p_g = []

        if len(e) != 0 and len(f) != 0:
            for j in e:
                for k in f:
                    e_f.append(j)
                    e_f.append('apply')
                    e_f.append(k)
                    e_f_relation.append(e_f)
                    e_f = []

        if len(y) != 0 and len(f) != 0:
            for j in y:
                for k in f:
                    y_f.append(j)
                    y_f.append('constrain')
                    y_f.append(k)
                    y_f_relation.append(e_f)
                    y_f = []

        if len(e) != 0 and len(r) != 0:
            for j in e:
                for k in r:
                    e_r.append(j)
                    e_r.append('support')
                    e_r.append(k)
                    e_r_relation.append(e_r)
                    e_r = []

        if len(e) != 0 and len(p) != 0:
            for j in e:
                for k in p:
                    e_p.append(j)
                    e_p.append('support')
                    e_p.append(k)
                    e_p_relation.append(e_p)
                    e_p = []

        if len(e) != 0 and len(g) != 0:
            for j in e:
                for k in g:
                    e_g.append(j)
                    e_g.append('support')
                    e_g.append(k)
                    e_g_relation.append(e_g)
                    e_g = []

        if len(y) != 0 and len(p) != 0:
            for j in y:
                for k in p:
                    y_p.append(j)
                    y_p.append('constraint')
                    y_p.append(k)
                    y_p_relation.append(y_p)
                    y_p = []

        print("\r关系获取进度：{:.2%}".format((i + 1) / len(sentences_list)), end='')

    r_p_relation = np.unique(r_p_relation, axis=0)
    p_g_relation = np.unique(p_g_relation, axis=0)
    e_f_relation = np.unique(e_f_relation, axis=0)
    y_f_relation = np.unique(y_f_relation, axis=0)
    r_r_relation = np.unique(r_r_relation, axis=0)
    p_p_relation = np.unique(p_p_relation, axis=0)
    g_g_relation = np.unique(g_g_relation, axis=0)
    e_e_relation = np.unique(e_e_relation, axis=0)
    e_r_relation = np.unique(e_r_relation, axis=0)
    e_p_relation = np.unique(e_p_relation, axis=0)
    e_g_relation = np.unique(e_g_relation, axis=0)
    y_p_relation = np.unique(y_p_relation, axis=0)

    print('\n关系获取完成\n')

    return r_p_relation, p_g_relation, e_f_relation, \
           y_f_relation, r_r_relation, p_p_relation, \
           g_g_relation, e_e_relation, e_r_relation, \
           e_p_relation, e_g_relation, y_p_relation


def entity2id(entity, relation):
    for line in relation:
        for node in entity:
            if line[0] == node[1]:
                line[0] = node[0]
            if line[-1] == node[1]:
                line[-1] = node[0]
    return relation


# def build_json(entity, p_w_relation, w_l_relation, p_l_relation, w_p_relation, l_w_relation, l_p_relation):
#     p_w_relation = entity2id(entity, p_w_relation)
#     w_l_relation = entity2id(entity, w_l_relation)
#     p_l_relation = entity2id(entity, p_l_relation)
#     w_p_relation = entity2id(entity, w_p_relation)
#     l_w_relation = entity2id(entity, l_w_relation)
#     l_p_relation = entity2id(entity, l_p_relation)
#
#     JSON_node_list = []
#     for line in entity:
#         JSON_node = {"type": "node",
#                      "id": "{}".format(line[0]),
#                      "labels": "{}".format(line[-1]),
#                      "properties": {"name": "{}".format(line[1])}}
#         JSON_node_list.append(JSON_node)
#
#     JSON_relation_list = []
#     for i in p_w_relation:
#         a = 0
#         JSON_relation = {"type": "relationship",
#                          "id": "{}".format('p_w' + str(a)),
#                          "label": "包含",
#                          "start": {"id": "{}".format(i[0]),
#                                    "labels": "产品"},
#                          "end": {"id": "{}".format(i[-1]),
#                                  "labels": "部件"}}
#         JSON_relation_list.append(JSON_relation)
#
#     for i in w_l_relation:
#         a = 0
#         JSON_relation = {"type": "relationship",
#                          "id": "{}".format('w_l' + str(a)),
#                          "label": "包含",
#                          "start": {"id": "{}".format(i[0]),
#                                    "labels": "部件"},
#                          "end": {"id": "{}".format(i[-1]),
#                                  "labels": "部零件"}}
#         JSON_relation_list.append(JSON_relation)
#
#     for i in p_l_relation:
#         a = 0
#         JSON_relation = {"type": "relationship",
#                          "id": "{}".format('p_l' + str(a)),
#                          "label": "包含",
#                          "start": {"id": "{}".format(i[0]),
#                                    "labels": "产品"},
#                          "end": {"id": "{}".format(i[-1]),
#                                  "labels": "零件"}}
#         JSON_relation_list.append(JSON_relation)
#
#     for i in w_p_relation:
#         a = 0
#         JSON_relation = {"type": "relationship",
#                          "id": "{}".format('w_l' + str(a)),
#                          "label": "构成",
#                          "start": {"id": "{}".format(i[0]),
#                                    "labels": "部件"},
#                          "end": {"id": "{}".format(i[-1]),
#                                  "labels": "产品"}}
#         JSON_relation_list.append(JSON_relation)
#
#     for i in l_w_relation:
#         a = 0
#         JSON_relation = {"type": "relationship",
#                          "id": "{}".format('l_w' + str(a)),
#                          "label": "构成",
#                          "start": {"id": "{}".format(i[0]),
#                                    "labels": "零件"},
#                          "end": {"id": "{}".format(i[-1]),
#                                  "labels": "部件"}}
#         JSON_relation_list.append(JSON_relation)
#
#     for i in l_p_relation:
#         a = 0
#         JSON_relation = {"type": "relationship",
#                          "id": "{}".format('l_p' + str(a)),
#                          "label": "构成",
#                          "start": {"id": "{}".format(i[0]),
#                                    "labels": "零件"},
#                          "end": {"id": "{}".format(i[-1]),
#                                  "labels": "产品"}}
#         JSON_relation_list.append(JSON_relation)
#
#     return JSON_node_list, JSON_relation_list
#
#
# def build_kg(JSON_node_list, JSON_relation_list):
#     kg = {"type": "柴油机构成结构知识图谱",
#           "node": JSON_node_list,
#           "relationship": JSON_relation_list}
#
#     return kg


if __name__ == "__main__":
    input_path = './data/train2.txt'
    R_entities_output_path = './result/knowledgegraph/r_entities.xlsx'
    P_entities_output_path = './result/knowledgegraph/p_entities.xlsx'
    G_entities_output_path = './result/knowledgegraph/g_entities.xlsx'
    E_entities_output_path = './result/knowledgegraph/e_entities.xlsx'
    F_entities_output_path = './result/knowledgegraph/f_entities.xlsx'
    Y_entities_output_path = './result/knowledgegraph/y_entities.xlsx'
    r_p_relation_output_path = './result/knowledgegraph/r_p_relations.xlsx'
    p_g_relation_output_path = './result/knowledgegraph/p_g_relations.xlsx'
    e_f_relation_output_path = './result/knowledgegraph/e_f_relations.xlsx'
    y_f_relation_output_path = './result/knowledgegraph/y_f_relations.xlsx'
    r_r_relation_output_path = './result/knowledgegraph/r_r_relations.xlsx'
    p_p_relation_output_path = './result/knowledgegraph/p_p_relations.xlsx'
    g_g_relation_output_path = './result/knowledgegraph/g_g_relations.xlsx'
    e_e_relation_output_path = './result/knowledgegraph/e_e_relations.xlsx'
    e_r_relation_output_path = './result/knowledgegraph/e_r_relations.xlsx'
    e_p_relation_output_path = './result/knowledgegraph/e_p_relations.xlsx'
    e_g_relation_output_path = './result/knowledgegraph/e_g_relations.xlsx'
    y_p_relation_output_path = './result/knowledgegraph/y_p_relations.xlsx'

    R, P, G, E, F, Y = get_entities(input_path)
    entity = np.vstack((R, P, G, E, F, Y))
    print(len(entity))
    r_p_relation, p_g_relation, e_f_relation, \
    y_f_relation, r_r_relation, p_p_relation, \
    g_g_relation, e_e_relation, e_r_relation, \
    e_p_relation, e_g_relation, y_p_relation = get_relations(input_path)

    r_p_relation_id = entity2id(entity, r_p_relation)
    p_g_relation_id = entity2id(entity, p_g_relation)
    e_f_relation_id = entity2id(entity, e_f_relation)
    y_f_relation_id = entity2id(entity, y_f_relation)
    r_r_relation_id = entity2id(entity, r_r_relation)
    p_p_relation_id = entity2id(entity, p_p_relation)
    g_g_relation_id = entity2id(entity, g_g_relation)
    e_e_relation_id = entity2id(entity, e_e_relation)
    e_r_relation_id = entity2id(entity, e_r_relation)
    e_p_relation_id = entity2id(entity, e_p_relation)
    e_g_relation_id = entity2id(entity, e_g_relation)
    y_p_relation_id = entity2id(entity, y_p_relation)

    df1 = pd.DataFrame(R, index=None, columns=None)
    df1.to_excel(R_entities_output_path)

    df2 = pd.DataFrame(P)
    df2.to_excel(P_entities_output_path)

    df3 = pd.DataFrame(G)
    df3.to_excel(G_entities_output_path)

    df4 = pd.DataFrame(E)
    df4.to_excel(E_entities_output_path)

    df5 = pd.DataFrame(F)
    df5.to_excel(F_entities_output_path)

    df6 = pd.DataFrame(Y)
    df6.to_excel(Y_entities_output_path)

    df7 = pd.DataFrame(r_p_relation_id)
    df7.to_excel(r_p_relation_output_path)

    df8 = pd.DataFrame(p_g_relation)
    df8.to_excel(p_g_relation_output_path)

    df9 = pd.DataFrame(e_f_relation_id)
    df9.to_excel(e_f_relation_output_path)

    df10 = pd.DataFrame(y_f_relation_id)
    df10.to_excel(y_f_relation_output_path)

    df11 = pd.DataFrame(r_r_relation_id)
    df11.to_excel(r_r_relation_output_path)

    df12 = pd.DataFrame(p_p_relation_id)
    df12.to_excel(p_p_relation_output_path)

    df13 = pd.DataFrame(g_g_relation_id)
    df13.to_excel(g_g_relation_output_path)

    df14 = pd.DataFrame(e_e_relation_id)
    df14.to_excel(e_e_relation_output_path)

    df15 = pd.DataFrame(e_r_relation_id)
    df15.to_excel(e_r_relation_output_path)

    df16 = pd.DataFrame(e_p_relation_id)
    df16.to_excel(e_p_relation_output_path)

    df17 = pd.DataFrame(e_g_relation_id)
    df17.to_excel(e_g_relation_output_path)

    df18 = pd.DataFrame(y_p_relation_id)
    df18.to_excel(y_p_relation_output_path)
