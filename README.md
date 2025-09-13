# Forums For All
![Image of the site interface](/public/images/TellMe.PNG)

## Introduction
This is my 4th and final project in the Software Engineering Bootcamp by General Assembly, and it's a reddit clone where you can ask questions and answer. It features categories portraying subreddits in reddit, and it also accepts media such as images.

## Technologies Used
- PostgresSQL
- Django
- Python
- CSS3
- JavaScript

## Get Started

### Clone Repository

Clone the repository in a directory of your liking:

```
git clone https://github.com/yousifj129/forums-for-all.git
```

### Setup and Install Python/Django

Download python
- [Download Python](https://www.python.org/downloads/)

## Setup your Virtual Environment

In the project directory lets setup a virtual environment:

```
python -m venv my-env
```

my-env can be anything

and then run the environment:

Windows:
```
source name-of-venv/scripts/activate
```
Mac:
```
source name-of-venv/bin/activate
```

## Install Django and packages

```
pip install -r requirements.txt
```
## Setup your PostgresSQL database
- create a .env file
- add the following in the .env:
  ```
  DB_PASSWORD=your_pgadmin_password
  ```
- create a database in pgadmin called ```forums-for-all```

## now you can run the app:
```
python manage.py runserver
```


