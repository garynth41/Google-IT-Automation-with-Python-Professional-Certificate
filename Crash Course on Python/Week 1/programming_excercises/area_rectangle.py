"""
This function to calculate the area of a rectangle is not very readable. Can you refactor it, and then call the function to
calculate the area with base of 5 and height of 6? Tip: a function that calculates the area of a rectangle should probably
be called rectangle_area, and if it's receiving base and height,
that's what the parameters should be called.
"""
def rectangle_area(base, height):
    area = base * height  # the area is base*height
    print("The area is " + str(area))
    
    
rectangle_area(5, 6)