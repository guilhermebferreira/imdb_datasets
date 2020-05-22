
cd data

echo 'download dos arquivos'
#download dos datasets
wget https://datasets.imdbws.com/title.ratings.tsv.gz
wget https://datasets.imdbws.com/title.akas.tsv.gz
wget https://datasets.imdbws.com/title.basics.tsv.gz


echo 'descompactando'
#unzip
gzip -d  title.ratings.tsv.gz
gzip -d  title.akas.tsv.gz
gzip -d  title.basics.tsv.gz
rm -f *.tsv.gz


echo 'gerando versão reduzida dos arquivos'
#gerando versão reduzida dos arquivos, para testes
head -100 title.akas.tsv > short.title.akas.tsv
head -100 title.ratings.tsv > short.title.ratings.tsv
head -100 title.basics.tsv > short.title.basics.tsv


