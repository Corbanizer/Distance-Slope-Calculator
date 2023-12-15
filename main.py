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
in_root = dif_x ** 2 + dif_y ** 2
if in_root.is_integer():
    coef = 1           
    root_num = in_root 
    for i in range(int(in_root), 0, -1): 
        coef = math.sqrt(i)
        if coef.is_integer() and in_root % i == 0:
                root_num = in_root / i
                break
    if coef != 1:
        p('Distance = sqrt of', in_root, '=', coef, 'sqrt', root_num)
    else:
        p('Distance = sqrt of', in_root)