"""
Write a program to **find surface area and volume of a cylinder using function
"""
def surface_area(radius):
    print('The surface area of the Cylinder is..')
    print(3.14*(radius**2))
def volume(radius,height):
    print('The Volume of the cylinder..')
    print(3.14*(radius**2)*height)
r=(float(input('Enter the Radius of the cylinder')))
h=float(input('Enter the height of the cylinder'))
surface_area(r),volume(r,h)