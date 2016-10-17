# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

args = sys.argv[1:]

if len(args) != 2:
    print('Invalid argumets.')
    print('md-to-jekyll-formatter.py [inputFilePath] [outputFilePath]')
    exit()

highlight_start = True
f = open(args[0], 'r')
fout = open(args[1], 'w')
lines = f.readlines()
for line in lines:
    if line.find('```') != -1:
        if highlight_start:
            line.strip()
            sp = line.split('```')
            sp[1] = sp[1].replace('\n', '')
            if len(sp[1]) > 0:
                fout.write('{% highlight ' + sp[1] + ' %}\n')
            else:
                fout.write('{% highlight %}\n')
            highlight_start = False
        else:
            fout.write('{% endhighlight %}\n')
            highlight_start = True
    else:
        fout.write(line)
f.close()
fout.close()
