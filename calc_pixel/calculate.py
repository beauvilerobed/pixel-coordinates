import re
import numpy as np

def get_coordinates(query_dict):
    """
    Function to return  a two-dimensional surface given the dimensions 
    of the image and the corner points of the image as it is to be displayed.

    Assumption: 
    We can assume that the corner points will define a rectangle with sides 
    that are parallel to the x and y axes (the rectangle will not be rotated)

    Example

    Input: 
    Type: QueryDict
    {
        'csrfmiddlewaretoken': ['tockenvalue'], 
        'firstcoord': ['(1,1)'], 
        'secondcoord': ['(3,1)'], 
        'thirdcoord': ['(1,3)'], 
        'fourthcoord': ['(3,3)'], 
        'height': ['3'], 
        'width': ['3']
    }

    Output:
    Type: list[list[list]
    [

    [[1.0, 3.0], [2.0, 3.0], [3.0, 3.0]],
    [[1.0, 2.0], [2.0, 2.0], [3.0, 2.0]],
    [[1.0, 1.0], [2.0, 1.0], [3.0, 1.0]]
    
    ]
    """
    coords = process_query_dict(query_dict)
    dim = coords[-1]

    if dim[0] < 2 or dim[1] < 2:
        return [["Invalid height or width"]]

    point1, point2 = get_points(coords)
    new_coords = return_coords(point1, point2, dim)

    return new_coords

def process_query_dict(query_dict):
    """
    Function to return a list of 4 coordinates and dimensions

    Example

    Input:
    type: QueryDict
    {
        'csrfmiddlewaretoken': ['tockenvalue'], 
        'firstcoord': ['(1,1)'], 
        'secondcoord': ['(3,1)'], 
        'thirdcoord': ['(1,3)'], 
        'fourthcoord': ['(3,3)'], 
        'height': ['3'], 
        'width': ['3']
    }

    Output:
    Type: list[list[tuple]]

    [   
        # 4 coordinates
        [(1.0,1.0)],
        [(3.0,1.0)],
        [(1.0,3.0)],
        [(3.0,3.0)],

        # dim
        [(3,3)],

    ]

    """
    vals = list(query_dict.values())[1:]
    num_coords = 4
    coords = []
    height = int(vals[-2])
    width = int(vals[-1])
    dim = (height, width)

    for i in range(num_coords):
        x_coord = float(re.split('\(|\)|,', vals[i])[1])
        y_coord = float(re.split('\(|\)|,', vals[i])[2])
        coords.append((x_coord, y_coord))

    coords.append(dim)
    return coords

def return_coords(point1, point2, dim):
    """
    Function to generate the upper left corner point
    and return a solution preliferated from the upper 
    left corner point

    Example:

    Input:
    Type: list[list]
    [   
        # first point
        [1.0, 1.0],
        
        # point furthest away from first point
        [3.0, 3.0]
    ] 

    Output:
    Type:     list[list[list]]
    [

        [[1.0, 3.0], [2.0, 3.0], [3.0, 3.0]],
        [[1.0, 2.0], [2.0, 2.0], [3.0, 2.0]],
        [[1.0, 1.0], [2.0, 1.0], [3.0, 1.0]]
        
    ]

    """

    if point1[0] > point2[0]:
        point1, point2 = point2, point1

    if point1[1] < point2[1]:
        point1[1], point2[1] = point2[1], point1[1]

    solution  = prelif(point1, point2, dim)
    return solution
            
    
def prelif(point1, point2, dim):
    """
    Function to preliferate or generate a grid starting from the upper 
    left corner point;

    Example

    Input:
    Type: list[list]
        [   
        # upper left corner point
        [1.0, 3.0],
        
        # lower right corner point
        [3.0, 1.0]
    ] 

    Output:
    list[list[list]]
    [

        [[1.0, 3.0], [2.0, 3.0], [3.0, 3.0]],
        [[1.0, 2.0], [2.0, 2.0], [3.0, 2.0]],
        [[1.0, 1.0], [2.0, 1.0], [3.0, 1.0]]
        
    ]

    """
    width  = int(dim[1])
    height = int(dim[0])
    x_step = (point2[0] - point1[0])/(width-1)
    y_step = (point1[1] - point2[1])/(height-1)
    x_axis = [point1[0] + j*x_step for j in range(width)]
    y_axis = [point1[1] - j*y_step for j in range(height)]

    ans = []

    for y in y_axis:
        temp  = []
        for x in x_axis:
            temp.append([x,y])
        ans.append(temp)

    return ans

def get_points(coords):
    """
    Function to return the the first point and 
    the point furthest away from the first point

    Example:

    Input:
    Type: list[list[tuple]]
    [   
        # 4 coordinates
        [(1.0,1.0)],
        [(3.0,1.0)],
        [(1.0,3.0)],
        [(3.0,3.0)],

        # dim
        [(3,3)],

    ]


    Output:
    Type: list[list]
    [   
        # first point
        [1.0, 1.0],
        
        # point furthest away from first point
        [3.0, 3.0]
    ]

    """
    point = np.array(coords[0])
    diff_coord = coords[1:4]
    vals = {}

    for coord in diff_coord:
        dist = np.linalg.norm(coord-point)
        vals[coord] = dist
    
    max_dist = max(vals.values())

    for key in vals:
        if vals[key] == max_dist:
            
            return list(point), list(key)
