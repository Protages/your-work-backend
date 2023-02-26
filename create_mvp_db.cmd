call ./env/Scripts/activate.bat

cd src
del /f db.sqlite3
cd ..
@REM cd app
@REM rmdir migrations /s /q
@REM cd ..
@REM cd user
@REM rmdir migrations /s /q
@REM cd ../..

python src/manage.py makemigrations
python src/manage.py migrate

start cmd /c python src/manage.py runserver

echo exec(open("src/create_mvp_db.py").read()) | python src/manage.py shell
