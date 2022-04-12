# Pixel Coordinates

Objective: The objective in this challenge is to write a program that calculates pixel coordinate values for an image that is to be displayed on a two dimensional surface given the dimensions of the image and the corner points of the image as it is to be displayed.

For example, if an image is defined by a 3x3 grid of pixel values, and the (x, y) coordinates of the four corner points to display the image at are: (1, 1), (3, 1), (1, 3), and (3, 3) then the program should calculate and return the coordinates: (1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (3, 1), (3, 2), (3, 3) which are the coordinates at which to place the 9 pixels in the image such that they’re evenly spaced within the corner points.

#### Prerequisites
Ensure the following is installed to your system:

- Python >= 3.7
- Python `Pip` the package manager.
- Docker

#### Getting Started

#### Installing requirements through a virtual environment

```
$ python3 -m pip install --user virtualenv
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
