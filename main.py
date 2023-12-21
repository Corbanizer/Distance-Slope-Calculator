import math as m
import time as t

p = print
p(':3')
f = float
i = input
b = 'Enter ('
a = ') --> '
x1 = f(i(b + 'x1' + a))
y1 = f(i(b + 'y1' + a))
x2 = f(i(b + 'x2' + a))
y2 = f(i(b + 'y2' + a))
del a, b, f, i
p('')
s = 'Slope ='
st = t.time()
dif_x = x2 - x1
dif_y = y2 - y1
del y1, y2, x1, x2
p(s, dif_y, '/', dif_x)
if dif_x == 0 or dif_y == 0:
    p('You cant divide by 0')
    exit()
p(s, dif_y / dif_x)
del s
p('')
in_r = dif_x**2 + dif_y**2
d = 'Distance = sqrt of'
if in_r.is_integer():
    coef = 1
    r_num = in_r
    n = m.sqrt
    for i in range(int(in_r), 0, -1):
        coef = n(i)
        if coef.is_integer() and in_r % i == 0:
            r_num = in_r / i
            break
    if coef != 1:
        e = t.time()
        p(d, in_r, '=', coef, 'sqrt', r_num)
        del r_num, in_r, d, n
    else:
        e = t.time()
        p(d, in_r)
        del r_num, in_r, d, n
e = t.time()
p('')
if e - st < 0.0001:
    p('Too fast to display time')
else:
    p('Time to calculate =', e - st, 'seconds')
exit()
