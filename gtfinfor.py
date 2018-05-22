#! /usr/bin/env python3

__author__ = 'd2jvkpn'
__version__ = '0.1'
__release__ = '2018-05-20'
__project__ = 'https://github.com/d2jvkpn/GenomicProcess'
__lisence__ = 'GPLv3 (https://www.gnu.org/licenses/gpl-3.0.en.html)'

import os, gzip
from collections import defaultdict

if len(os.sys.argv) != 4 or os.sys.argv[1] in ['-h', '--help']: 
    print ('Extract attribution(s) of feature(s) from gtf. Usage:')
    print ('   python3 gtfinfor.py <input.gtf> <feature1,feature2...> <attribution1,attribution2...>')

    _ = '\nauthor: {}\nversion: {}\nrelease: {}\nproject: {}\nlisence: {}\n'
    __ = [__author__,  __version__, __release__, __project__, __lisence__]
    print (_.format (*__))
    os.sys.exit(0)


gtf = os.sys.argv[1]
fea = os.sys.argv[2].split(',')
att = os.sys.argv[3].split(',')

# fea = ['transcript', 'CDS']
# att = ['transcript_id', 'transcript_name', 'gene_id', 'gene_name', 'product']

GTF = gzip.open(gtf, 'r') if gtf.endswith('gz') else open(gtf, 'r')

print ('\t'.join(att + ['feature', 'position']))

for _ in GTF:
    if gtf.endswith('gz'):
        fd = _.decode('utf8').strip(';\n').split('\t')
    else:
        fd = _.strip(';\n').split('\t')

    if fd[0].startswith('#') or len(fd) != 9 or fd[2] not in fea: continue

    d = defaultdict(str)

    __ = [ i.split(' ', 1) for i in fd[8].split('; ') ]

    for i in __: d[i[0]] = i[1].strip('"')

    __ = ':'.join([fd[0], fd[3], fd[4], fd[6]])

    print ('\t'.join ([d[i] for i in att] + [fd[2], __]))


GTF.close()