import sys
import math
a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

x1 = int((-1*b - math.sqrt(b**2 - 4*a*c)) / 2*a)
x2 = int((-1*b + math.sqrt(b ** 2 - 4 * a * c)) / 2*a)
print(x1, x2, sep='\n')

