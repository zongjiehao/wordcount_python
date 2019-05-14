import sys

for lines in sys.stdin:
    for ss in lines.strip().split(''):
        for s in ss:
            if s.strip() != "":
                print "%s\t%s" % (s, 1)
