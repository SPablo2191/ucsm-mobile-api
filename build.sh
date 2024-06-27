pip install -r requirements/dev.txt
python src/manage.py collectstatic --no-input
python src/manage.py migrate