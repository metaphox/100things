#!/usr/bin/env python

l100 = []

with open('100.txt', 'r') as f100:
    lines = f100.readlines()
    i = 0
    for line in lines:
        own = True
        if line.strip().find('#') == 0:
            l100.append(line)
            continue
        if line.strip().find('*') == 0:
            own = False
        try:
            int(line[2:4])
            item = line[5:].strip()
        except:
            item = line.strip()
        if len(item.strip()) == 0: continue
        index = '%02d' % i
        index = '  ' + index if own else ' *' + index
        l100.append(index + ' ' + item + '\n')
        i = i + 1

with open('100.txt', 'w') as f100:
    f100.writelines(l100)

