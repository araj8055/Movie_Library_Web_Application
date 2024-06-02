echo " BUILD START"
# python3.9 -m pip install -r requirements.txt
# python3.9 manage.py collectstatic --noinput --clear

pip install -r requirements.txt
python manage.py collectstatic --noinput
echo " BUILD END"
