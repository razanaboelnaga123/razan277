name = 'ahmed'

def modify():
    global name
    name = 'samir'
    print(name)

def say_hi():
    print('hi',name)


    modify()
    say_hi()
    print(name)
    