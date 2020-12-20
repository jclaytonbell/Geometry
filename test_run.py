from math import pi
from polygons import make_polygon as mp

"""Let's make some polygons!"""

p0 = mp.Polygon()
p0.set_name = 'p0'
p0.set_n_sides(4)
p0.set_side_length(10)
p0.info()

p1 = mp.Polygon()
p1.set_name = 'p1'
p1.set_n_sides(17)
p1.set_radius(10)
p1.info()

p2 = mp.Polygon()
p2.set_name = 'p2'
p2.set_n_sides(10000)
p2.set_radius(10)
p2.info()

# How does the area of Polygon p2 compare to that of a circle with the same radius?

area_circle = pi * (10 ** 2)
print('area of circle, radius 10 = ', area_circle)
print(' ')

p3 = mp.Polygon()
p3.set_name = 'p3'
p3.set_n_sides(4)
p3.set_side_length(10)
p3.info()
p3.set_n_sides(5)
p3.info()