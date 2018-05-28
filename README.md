# GenomicProcess
Tools for Genomic Data Analysis

<br></br>

**[ncbi_gff3_to_ensembl_gtf.py]**

  Convert ncbi gff3 format to ensembl gtf (be compatible with softwares like stringtie), usage:

    python3  ncbi_gff3_to_ensembl_gtf.py  <input.gff3>  <outputPrefi>

<br></br>

**[gff3infor.sh]**

Gff3 file statistic and information extraction, usage:

    sh  gff3infor  <input.gff3>  [feature-type]  [attribution1,attribution2...]

Note: gawk4.0 or higher is required to support urldecode

<br></br>

**[gffinfor.py]**

Extract attribution(s) of feature(s) from gtf or gff3, usage:

    python3  gtfinfor.py  <input.gtf/input.gff3>  <feature1,feature2...>  <attribution1,attribution2...>

Output: stdout, tsv format.
   
