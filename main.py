import math
p=print
p(":3")
f=float
i=input
x1= f(i('Enter (x1) --> '))
y1= f(i('Enter (y1) --> '))
x2= f(i('Enter (x2) --> '))
y2= f(i('Enter (y2) --> '))
dif_x= x2-x1
dif_y= y2-y1
p('Slope =',dif_y,'/',dif_x)
p('Slope =',dif_y/dif_x)
in_r = dif_x ** 2 + dif_y ** 2
if in_r.is_integer():
    coef = 1           
    r_num = in_r 
    for i in range(int(in_r), 0, -1): 
        coef = math.sqrt(i)
        if coef.is_integer() and in_r % i == 0:
                r_num = in_r / i
                break
    if coef != 1:
        p('Distance = sqrt of', in_r, '=', coef, 'sqrt', r_num)
    else:
        p('Distance = sqrt of', in_r)
