# AIID Demos
This repository contains demonstrations used for work with AIID.
# Getting Started
### Starting the server
`cd backend`
`python manage.py runserver`

### Starting Jupyter Lab
`cd backend`
`python manage.py shell_plus --lab`

### Using django models in Jupyter
`from <app name>.models import <model name>`

***NOTE: make sure that `DJANGO_ALLOW_ASYNC_UNSAFE=True` is set in the `.env` file***

# Resources
* ~~[Real Python - Get Started with Django](https://realpython.com/get-started-with-django-1/)~~
    * Not too helpful when it comes to making the actual connection. 
    * Use this instead: [(DEV.to) How to connect Django to React.js](https://dev.to/nagatodev/how-to-connect-django-to-reactjs-1a71)
* [Django (Backend) + React (Frontend) Basic Tutorial](https://medium.com/@gazzaazhari/django-backend-react-frontend-basic-tutorial-6249af7964e4)
* [React.dev - Add React To An Existing Project](https://react.dev/learn/add-react-to-an-existing-project)
* [Getting Jupyter to work with Django](https://gist.github.com/EtsuNDmA/dd8949061783bf593706559374c8f635)
* [How to structure React files](https://blog.webdevsimplified.com/2022-07/react-folder-structure/)]
* [Full Stack with Django and React](https://medium.com/swlh/full-stack-with-django-and-react-react-afae36017852)
    * Useful for setting up the data connections and hooks between React and Django
