# Coder House Final Project - Python

## Description
A website where people or organizations can share their thoughts, opinions, experiences or knowledge on various topics of interest.

## Features
| Feature         | Description|
| ----------------- | --------------------------------------------------------------- |
| **Users**         | Register, login, edit profiles, delete profiles, view profiles. |
| **Blogs**         | Create blogs, edit blogs, delete blogs, visit blogs.            |
| **Posts**         | Create posts, edit posts, delete posts, visit posts.            |
| **Messages**      | Send messages, view messages, delete messages.                  |
| **Search Engine** | Only to search for blogs.                                       |
| **Home Page**     | Page where the latest blogs are displayed.                      |


## Dependencies
To run this project, you'll need `Python 3.x`, `Django 3.x` and `Willow`

## How to run the page
Do these steps in terminal

### 1. Clone the repository
```
git clone https://github.com/CampoLucas/django_blog.git
```

### 2. Create a virtual environment
Inside the project folder (where `manage.py` is):
```
python -m venv venv
```
Activate it:
#### For Windows
```
venv\Scripts\activate
```

#### For Linux / macOS
```
source venv/bin/activate
```

You should see `(venv)` in the terminal.

### 3. Install Django
Inside the `venv`:
```
pip install django
``` 

### 4. Run migrations
```
python manage.py migrate
```

### 5. Start the server
```
python manage.py runserver
```

Once the server is running, in the browser visit the website
```
http://localhost:8000
```

## Used Technologies
- Front-End:
    - CSS
    - Bootstrap
    - HTML
- Back-End:
    - Python
    - Django

## Test cases
Click [here](Test%20cases.xlsx) to see the document

## Demo Video in Spanish
Click [here](https://youtu.be/SrfbtL3Fac8) to see the video
