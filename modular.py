lst = range(19)

def modular():
    num = 118
    new = 118
    j = 0
    for i in range(19):
        new = (new*num)%337
        print(new)

modular()