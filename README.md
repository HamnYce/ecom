# eCOM
(E-Commerce Website written in Django For Learning Reasons)

## Request/Response Flow

- TO BE FINISHED ()

## Required Packages

- Django 4.2.4
- django-extensions 3.2.3
- djangorestframework 3.14.0
- drfpasswordless 1.5.8
- factory-boy 3.3.0
- Faker 19.3.0
- mysqlclient 2.2.0
- pip 23.2.1
- psycopg2 2.9.7
- PyMySQL 1.1.0

```bash
python -m venv .env
source .env
```

### Quick use command to install packages

```bash
pip install django==4.2.4 django-extensions==3.2.3 djangorestframework==3.14.0 drfpasswordless==1.5.8 factory-boy==3.3.0 Faker==19.3.0 mysqlclient==2.2.0 pyMySQL==1.1.0

```

### To see the list of available commands and to seed do

```bash
python manage.py
```

## _Api endpoints_ IN COMPLETE

### _users_ DONE

- authtoken verification (email, can add mobile) DONE
- signin

### _profiles_ DONE

- GET list (paginated) DONE
- POST create (to complete registration) DONE
- GET detail [specific user] DONE
- PUT update DONE

### _products_ (POST requires profile)

- GET list (paginated) DONE
- GET list [specific user’s products]
- GET list [user specific search]
- GET (filter page category) category table
- GET detail [specific user, specific name]
- POST create DONE
- PUT update

### Following

- TO BE CONFIRMED

## Current Models (Project models are not in sync as in testing phase)

## User

**Fields**:

- Email
- Has Profile

## User Profile

**Fields**:

- First name
- Last name
- Mobile
- Gender
- DoB
- Rating

## Category

**Fields**:

- Name

## Product

**Fields**:

- Name
- Price
- Category
- Status category (used new etc)
- Status (active / inactive)
- Desc
- User_ID
