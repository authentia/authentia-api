#Authentia API

Here is an amazing REST API built at Startupbus for Authentia project. :sparkles:

---

### Stack

- Python 3.4.3
- Django 2.0.3
- Django REST Framework
- PostgressSQL
- Kairos API

---

###Installation

Make your own virtualenv using python 3

```
mkvirtualenv -p python3 <your_virtual_env_name>
```

Create a `.env` file following `/authentia/.env.sample` template and type ```source .env```


Install all dependencies running the next command under `/authentia/` dir:

```
pip install -r requirements.txt
```


Run migrations

```
python manage.py migrate
```

Run project

```
python manage.py runserver
```



### Contributors
- Sebastían González
- Sebastían González
- Tania Chizon
- Sergio Malvaez 
