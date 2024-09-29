# avec_amour_vendas
Sistema em Django para gerenciamento de vendas

mkdir venv

sudo apt-get install pkg-config python3-dev default-libmysqlclient-dev libmysqlclient-dev build-essential

source venv/bin/activate


pip install -r requirements.txt 


pip list

ls

python3 manage.py makemigrations

python3 manage.py check

python3 manage.py migrate --fake

python manage.py migrate --fake avec_amour_vendas zero

python manage.py showmigrations avec_amour_vendas

python manage.py makemigrations avec_amour_vendas

python manage.py migrate --verbosity 2

python3 manage.py migrate

python manage.py runserver

deactivate
