#!/usr/bin/python

# run like this, with the identifier for a commit:
# python ./303score.py aa1d31eef6ec5a4670c65169de1a841cb6d4822a

import sys
import urllib
import json
import re

url = 'https://api.github.com/repos/fkh/nomic/commits/' + sys.argv[1]
f = urllib.urlopen(url)
data = json.loads(f.read())
date = data['commit']['author']['date']
proposer = data['commit']['author']['name'].decode()
match = re.match('^\d\d\d\d-\d\d-(\d\d)', date)
day = int(match.group(1))
composites = [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30]

As = 0
commas = 0

if day in composites:
    for line in data['files'][0]['patch'].decode().split('\n'):
        if re.match('^\+', line):
            As = As + line.lower().count('a')
            commas = commas + line.count(',')
    print('As: ' + str(As))
    print('commas: ' + str(commas))
    if As - commas > 0:
        print('Each eligible voter receives ' + str(As - commas) + ' points, in addition to points scored through rules other than 303.')
    else:
        print('No one gets points.  ' + proposer + ' shall be shamed.')
else:
    print('This rule was not proposed on a composite day.')
