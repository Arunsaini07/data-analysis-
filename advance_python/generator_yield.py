# ye tbi kam krega generator yield se jab hme jrurt hogi kisi value ki tabhi hme usko generate krna hoga

def get_number(i):
    # square krna hai i ka i tk clakr
    return i**2
def complex_generator(n):
    for i in range(8):
        yield get_number(i) # ye line hme ek generator object dega jo ki complex_generator function ke andar ke values ko generate karega jab hme unki jrurt hogi
        # basically ye tbi kam krta h jb hme jrurt hoti h 

gen = complex_generator(100)
for value in gen:
    print(value)

a=complex_generator(100)
# print(a,type(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))



