import time

def time1(func):
    def func2():
        a=time.time()
        c=func()
        b=time.time()-a
        print(b)
        return  c
    return func2

@time1
def print1():
    print('hello')
    time.sleep(2)

print1()





