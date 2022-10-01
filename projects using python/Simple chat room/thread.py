import threading

def func1():
    for i in range(10):
        print(True)

def func2():
    for i in range(10):
        print(False)

t1  = threading.Thread(target=func1)
t2 = threading.Thread(target=func2)

t1.start()
t2.start()


# func1()
# func2()