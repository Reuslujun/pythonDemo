import time

def test_a():
    num = 1 
    while num <=10:
        temp = yield num
        num+=1
        print("temp: ",temp)


    print("all done!")
    return None



if __name__ == '__main__':
    generator_a = (test_a())
    while True:
        time.sleep(0.5)
        value = next(generator_a)
        print("value Result: ",value)
