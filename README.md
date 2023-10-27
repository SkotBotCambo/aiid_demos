# web_stack_template
This repository contains a template for building common data-driven web applications from.

# Steps to recreate
### 1. Setup `pipenv` and install `django`
```pipenv install django```

### 2. Create Django Project
```
pipenv shell
django-admin startproject <project_name> .
```

### 3. Create `Pages` App
```python manage.py startapp pages```

### 4. "Install" `Pages` App in Project
In `<project_name>/settings.py`, add:
```
INSTALLED_APPS = [
    "pages.apps.PagesConfig",
    ...
]
```

### 5. Create a *View* for the *Pages* App
In `pages/views.py`, add:
```
from django.shortcuts import render

def home(request):
    return render(request, "pages/home.html", {})
```

### 6. Create a `/templates` directory for *Pages* App
```
mkdir -p pages/templates/pages
touch pages/templates/pages/home.html
```

In `pages/templates/pages/home.html`, add:
```<h1>Hello, World!</h1>```

### 7. Add a *Route* to the *Project*
In `<project_name>/urls.py`, add:



# Resources
* [Real Python - Get Started with Django](https://realpython.com/get-started-with-django-1/)
* [Django (Backend) + React (Frontend) Basic Tutorial](https://medium.com/@gazzaazhari/django-backend-react-frontend-basic-tutorial-6249af7964e4)
* [React.dev - Add React To An Existing Project](https://react.dev/learn/add-react-to-an-existing-project)