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

