config = {
    # 模型参数
    '--dropout': 0.1,
    '--lstm_units': 128,
    '--batch_size': 16,
    '--epoch': 4,
    '--lr': 5e-5,
    '--max_len': 70,

    # 训练参数
    '--seed': 233,

    # 预训练模型路径
    '--bert_config_path': './bertbase/chinese_L-12_H-768_A-12/bert_config.json',
    '--bert_checkpoint_path': './bertbase/chinese_L-12_H-768_A-12/bert_model.ckpt',
    '--vocab_path': './bertbase/chinese_L-12_H-768_A-12/vocab.txt',

    # 数据路径
    '--train_data': './data/train22.txt',
    '--test_data': './data/test2.txt',

    # 模型保存路径
    '--checkpoint_save_path': './checkpoint/bert_bilstm_crf-2.weights',
    '--crf_save_path': './checkpoint/crf_trans-2.pkl',

    # 输出路径
    '--demo': './data/beforeextract.txt',  # 供展示的用来构建知识图谱的数据
    '--input_path': './data/train22.txt',  # 正式的用来构建知识图谱的数据
    '--output_path': './result/kg.json',  # 供展示的知识图谱输出路径
    '--output_path1': './result/kg_extract.json',  # (待修改)正式的输出路径
    '--xlsx_ent_path': './result/entities_output.xlsx',
    '--xlsx_rel_path': './result/relations_output.xlsx'
}

# entity_labels = ['prov', 'city', 'district', 'devzone', 'town', 'community', 'village_group', 'road', \
#                  'roadno', 'poi', 'subpoi', 'houseno', 'cellno', 'floorno', 'roomno', 'detail', 'assist', \
#                  'distance', 'intersection', 'redundant', 'others']
entity_labels = ['R', 'P', 'G', 'E', 'F', 'Y']  # R:需求，P:对象，G:指标，E:事件，F:方法，Y:约束
