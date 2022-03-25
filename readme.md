# Take home project

#### Prerequisites
Ensure the following is installed to your system:

- Python >= 3.7 or greater
- Python `Pip` the package manager.
- Docker

#### Getting Started

#### Installing requirements through a virtual environment

```
$ python -m pip install --user virtualenv
$ python3 -m venv env
$ source env/bin/activate
(env)$ pip install -r requirements.txt
```
#### Running Project

```
(env)$ python3 manage.py runserver
```

#### Running Project Tests

```
(env)$ python3 manage.py test
```

#### Building and Running the Container
The following command will look for your Dockerfile and download 
all the necessary layers required to get your container image running. 
Afterwards, it will run the instructions in the Dockerfile and leave 
you with a container that is ready to start.

```
(env)$ docker build -t python-django-app .
```

To run:
```
(env)$ docker run -it -p 8000:8000 python-django-app
```
