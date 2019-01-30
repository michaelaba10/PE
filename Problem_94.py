

#It is easily proved that no equilateral triangle exists with integral length sides and integral area.
# However, the almost equilateral triangle 5-5-6 has an area of 12 square units.

#We shall define an almost equilateral triangle to be a triangle for which two sides are equal and the third differs by no more than one unit.

#Find the sum of the perimeters of all almost equilateral triangles with integral side lengths and area and whose
# perimeters do not exceed one billion (1,000,000,000).

from tictoc import tic,toc
from  eulerlib import is_square

def is_area_square(a,b):
    p = (2*a+b)*(0.5)
    p1 = p*(p-a)*(p-b)*(p-a)
    return is_square(p1)



perimeter_almost_equilateral_integral_sides_area = []
tic()
for a in range(5,1000000):#333333333):
    for b in range(a-1,a+2):
        if is_area_square(a,b) and (2*a+b<=1000000000):
            perimeter_almost_equilateral_integral_sides_area.append(2*a+b)
    print a
print(sum(perimeter_almost_equilateral_integral_sides_area))
toc()