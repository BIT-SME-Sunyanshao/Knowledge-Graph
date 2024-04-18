with open("./data/process/pdf2txt.txt", "r", encoding='utf-8') as f:
    data = f.readlines()
    # print(data)
sent = []
for line in data:
    for i in range(len(line)):
        if line[i].isdigit():
            continue
        elif ('\u0041' <= line[i] <= '\u005a') or ('\u0061' <= line[i] <= '\u007a'):
            continue
        if line[i] == ' ':
            continue
        elif line[i] == '\n':
            continue
        elif line[i] == '\t':
            continue
        elif line[i] == '[':
            continue
        elif line[i] == ']':
            continue
        elif line[i] == '/':
            continue
        elif line[i] == '　':
            continue
        else:
            sent.append(line[i])

print(sent)
with open("./data/process/one_column.txt", "w", encoding='utf-8') as f:
    for i in range(len(sent)):
        f.write(sent[i])  # 自带文件关闭功能，不需要再写f.close()
        if sent[i] == '。':
            f.write(' O')
            f.write('\n')
            f.write('\n')
        else:
            f.write(' O')
            f.write('\n')
