
## get_datasets

**get_datasets.sh** Realiza o download dos datasets do IMDB

- Download
- Unzip
- Gera versão reduzida / base de testes
    

    ./get_datasets.sh

**get_datasets.sh**  usa wget para fazer o download dos datasets



```
wget https://datasets.imdbws.com/title.ratings.tsv.gz
```

Utiliza o gzip para descompatá-los



```
gzip -d  title.ratings.tsv.gz
```

Assim como gera uma versão reduzida dos arquivos para testes




```
head -100 title.akas.tsv > short.title.akas.tsv
```

## import

	python import.py

**import.py** lê linha por linha os arquivos de entrada, e faz uso do **pymongo** para importá-los no **MongoDB**


## run

Coloquei a execução dos dois scripts, além do comando para subir um container com MongoDb, instalar os requisitos e aguardar até que o banco esteja funcional em um script **run.sh**

	docker- compose up - d

	./get_datasets.sh

	pip install -r requirements.txt

	while ! nc -z 0.0.0.0 27017;
	          do
	            echo sleeping;
	            sleep 1;
	          done;
	          echo Connected!;


	python import.py


---

No arquivo **import.py** tambem encontram se versões iniciais das funções para busca pelos filmes e recuperação da sua nota.

