from multiprocessing import Process
def func1():
     print(1)

def func2():
     print(0)

if __name__=='__main__':
     p1 = Process(target = func1)
     p1.start()
     p2 = Process(target = func2)
     p2.start()