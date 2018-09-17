python3 EnsemblGenome_v0.7.py search "Homo sapiens"
python3 EnsemblGenome_v0.7.py search Homo+sapiens
# http://asia.ensembl.org/Homo_sapiens/Info/Index

python3 EnsemblGenome_v0.7.py getftp http://asia.ensembl.org/Homo_sapiens/Info/Index
# created Ensembl-93__Homo_sapiens__GRCh38.p12/{download.sh,genome.infor.txt}

python3 EnsemblGenome_v0.7.py biomart http://asia.ensembl.org/Homo_sapiens/Info/Index
# Connected to Ensembl biomart...
# Saved gene2go.tsv to Ensembl-93__Homo_sapiens__GRCh38.p12/
# Saved gene2entrez.tsv to Ensembl-93__Homo_sapiens__GRCh38.p12/
# Saved gene2kegg.tsv to Ensembl-93__Homo_sapiens__GRCh38.p12/
# Saved gene.infor.tsv to Ensembl-93__Homo_sapiens__GRCh38.p12/

sh Ensembl-93__Homo_sapiens__GRCh38.p12/download.sh
# download Ensembl-93__Homo_sapiens__GRCh38.p12/cdna.fa.gz,genomic.fa.gz,genomic.gtf.gz,ncrna.fa.gz,pep.fa.gz