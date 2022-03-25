from django.shortcuts import render
from pixel_coord import settings
from calc_pixel.calculate import get_coordinates
import re



def index(request):
    """ The home page for Pixel Coordinates """

    return render(request, "index.html", {
        "MEDIA_URL": settings.STATIC_URL,
    })

def return_calculation(request):
    """ Returns grid to render on the home page """

    if request.method == "POST":
        query_dict = request.POST
        if is_valid(query_dict):
            solution = get_coordinates(query_dict)
        else:
            solution = [["Your input was not valid, please try again"]]
               
        return render(request, "index.html", {
            "MEDIA_URL": settings.STATIC_URL,
            "SOLUTION" : solution
        })

def is_valid(query_dict):
    """ Function to validate user input """

    vals = list(query_dict.values())[1:]
    num_coords = 4
    num_floats = 2
    for i in range(num_coords):
        arr = re.split('\(|\)|,', vals[i])
        if len(arr) == 4:
            num1 = re.split('\(|\)|,', vals[i])[1]
            num2 = re.split('\(|\)|,', vals[i])[2]
            if not is_number(num1) or not is_number(num2):
                return False
        else:
            return False

    for i in range(num_floats):
        num = vals[i + num_coords]
        if not is_number(num, 'int'):
            return False
    
    return True

def is_number(num, type="float"):
    if type == 'int':
        try:
            int(num)
            return True
        except ValueError:
            return False
    else:
        try:
            float(num)
            return True
        except ValueError:
            return False