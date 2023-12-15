import math
p=print
p(":3")
f=float
i=input
x1= f(i('Enter (x1) --> '))
y1= f(i('Enter (y1) --> '))
x2= f(i('Enter (x2) --> '))
y2= f(i('Enter (y2) --> '))
diff_x= x2 - x1
diff_y= y2 - y1
p('Slope =',diff_y,'/',diff_x)
p('Slope =',diff_y / diff_x)
in_root = diff_x ** 2 + diff_y ** 2
if in_root.is_integer():
    coefficient = 1           
    root_num = in_root 
    for i in range(int(in_root), 0, -1): 
        coefficient = math.sqrt(i)
        if coefficient.is_integer() and in_root % i == 0:
                root_num = in_root / i
                break
    if coefficient != 1:
        p('Distance = sqrt of', in_root, '=', coefficient, 'sqrt', root_num)
    else:
        p('Distance = sqrt of', in_root)
