SD_SmartUMa

Clone the file
Delete all migrates inside each folder (delete migrations/0001_initial.....)
go inside ../SD_SMARTUMA/smartUMa/smartUMa
pip install django
pip install pymysql
pip install django-tastypie
go to database create a new database named smartUMa then rep this one to smartUMarep
python manage.py makemigrations
pythong manage.py migrate
python manage.py createsuperuser --username=XX --email= XXX
Website preparation is complete, but we need to have all tables completed, so fill all tables except weather 
To fill weather tables, open 2 consoles and type "python ./Listen_Insert.py" in one and "python ./Rotina.py" in another 
python manage.py runserver

DONEEE
