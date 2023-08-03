from threading import Thread

def func1():
    while(True): 
     print("A")

def func2():
    while(True):
     print("B")

if __name__ == '__main__':
    Thread(target = func1).start()
    Thread(target = func2).start()