## Required Packages:
- Django              4.2.4
- django-extensions   3.2.3
- djangorestframework 3.14.0
- drfpasswordless     1.5.8
- factory-boy         3.3.0
- Faker               19.3.0
- mysqlclient         2.2.0
- pip                 23.2.1
- psycopg2            2.9.7
- PyMySQL             1.1.0

- Creating and setting the environment 
```python
python -m venv .env
source .env
```

- Quick use command to install packages
```python
pip install django==4.2.4 django-extensions==3.2.3 djangorestframework==3.14.0 drfpasswordless==1.5.8 factory-boy==3.3.0 Faker==19.3.0 mysqlclient==2.2.0 pyMySQL==1.1.0

```

## *Api endpoints*:

### _users_ DONE:
- authtoken verification (email, can add mobile)
- signin
  
### _profiles_:
- GET list (paginated) DONE
- POST create (to complete registration)
- GET detail [specific user]
- PUT update
  
### _products_ (POST requires profile):
- GET list (paginated)
- GET list[specific user’s products]
- GET list[user specific search]
- GET (filter page category) category table
- GET detail [specific name]
- POST create
  
Following (maybe later)

