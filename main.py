import math
import time as t

p = print
p(":3")
f = float
i = input
x1 = f(i('Enter (x1) --> '))
y1 = f(i('Enter (y1) --> '))
x2 = f(i('Enter (x2) --> '))
y2 = f(i('Enter (y2) --> '))
p(" ")
start = t.time()
dif_x = x2 - x1
dif_y = y2 - y1
_s = 'Slope ='
p(_s, dif_y, '/', dif_x)
p(_s, dif_y / dif_x)
p(" ")
in_r = dif_x**2 + dif_y**2
_d = 'Distance = sqrt of'
if in_r.is_integer():
  coef = 1
  r_num = in_r
  for i in range(int(in_r), 0, -1):
    coef = math.sqrt(i)
    if coef.is_integer() and in_r % i == 0:
      r_num = in_r / i
      break
  if coef != 1:
    p(_d, in_r, '=', coef, 'sqrt', r_num)
  else:
    p(_d, in_r)
end = t.time()
p(" ")
p("Time to calculate =",end-start,"seconds")
