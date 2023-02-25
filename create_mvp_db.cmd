call ./env/Scripts/activate.bat

@REM python src/manage.py sqlclear
@REM python src/manage.py dbshell

python src/manage.py makemigrations
python src/manage.py migrate

@REM python src/manage.py runserver

echo exec(open("src/create_mvp_db.py").read()) | python src/manage.py shell