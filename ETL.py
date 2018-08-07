#获取的评论可能有重复，为了最终统计的真实性，需做去重处理
def xie_zheng(infile, outfile):
    infopen = open(infile, 'r', encoding='utf-8')
    outopen = open(outfile, 'w', encoding='utf-8')
    lines = infopen.readlines()#读取的数据集
    list_1 = []#存储不重复的评论数据
    for line in lines:
        if line not in list_1:#评论不重复
            list_1.append(line)
            outopen.write(line)
    infopen.close()
    outopen.close()

if __name__ == '__main__':
    xie_zheng('xie_zheng.txt', 'xie_zheng_result.txt')