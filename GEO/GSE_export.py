# pip3 install GEOparse

__author__ = 'd2jvkpn'
__version__ = '0.2'
__release__ = '2019-01-08'
__project__ = 'https://github.com/d2jvkpn/BioinformaticsAnalysis'
__license__ = 'GPLv3 (https://www.gnu.org/licenses/gpl-3.0.en.html)'

import GEOparse, os
import pandas as pd

USAGE = '''Extract GSE(GEO) table, usage:
  python3 GSE_export.py  <gse_id | gse_file>  <output_dir>'''

if len(os.sys.argv) != 3 or os.sys.argv[1] in ['-h', '--help']:
    print(USAGE)

    _ = '\nauthor: {}\nversion: {}\nrelease: {}\nproject: {}\nlisense: {}\n'
    __ = [__author__,  __version__, __release__, __project__, __license__]

    print (_.format (*__))
    os.sys.exit(2)

def ExprTable (gsms, samples):
    d = gsms[samples[0]].table

    if d.shape[0] == 0:
        return None

    d = d.iloc[:, [0, 1]]
    idxn = d.columns[0]

    for i in samples[1:]:
        t = GSE.gsms[i].table.iloc[:, [0, 1]]
        h = list(t.columns); h = [idxn, i]; t.columns = h
        d = pd.merge(d, t, how="left", left_on=idxn, right_on=idxn)

    return d

gse, outdir = os.sys.argv[1], os.sys.argv[2]

if not os.path.isdir(outdir):
    os.makedirs(outdir)

if gse.endswith(".gz"):
    GSE = GEOparse.get_GEO(filepath = gse)
else:
    GSE = GEOparse.get_GEO(geo=gse, destdir=outdir)

d = ExprTable(GSE.gsms, list(GSE.gsms))

if not isinstance(d, pd.DataFrame):
    os.sys.exit("Not GSMS available in " + gse)

gsms = outdir + "/gsms.tsv"
d.to_csv(gsms, sep="\t", index=False)
print("Saved", gsms)

for i in list(GSE.gpls):
    gpls = "{}/gpls.{}.tsv".format(outdir, i)
    GSE.gpls[i].table.to_csv(gpls, sep="\t", index=False)
    print("Saved", gpls)
