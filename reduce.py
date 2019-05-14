# coding=utf-8
import sys
# reduce程序接收map处理后的数据，默认按照key排序
current_word = None
count_pool = []
sum = 0
for line in sys.stdin:
    word, val = line.strip().split('\t')

    if current_word is None:
        current_word = word

    if current_word != word:
        for count in count_pool:
            sum += count
            print "%s\t%s" % (current_word, sum)
            current_word = word
            count_pool = []
            sum = 0

    count_pool.append(int(val))

for count in count_pool:
    sum += count
    print "%s\t%s" % (current_word, str(sum))
