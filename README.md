Hi! 
This is Ankietowo project

# Run

1. clone repo
2. spawn venv
3. cd Ankietowo
4. make sure that you have only __init.py__ in migrations directory.
5. If there are others files, you must delete it, also make sure you don't have 
db.sqlite3 file(if yes, delete it)
6. Install requirements.txt
7. in shell use commands:
    - ```python manage.py makemigrations polls```
    - ```python manage.py migrate```

8. now, you can run the local server by command:
    - ```python manage.py runserver```