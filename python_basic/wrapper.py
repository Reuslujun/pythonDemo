import time
import threading


def count_time(fun):
    print("count_time")
    def count():
        startime = time.time()
        fun()
        endtime = time.time()
        print(" 一共花费了{}时间".format(endtime-startime))

    return count


def easy_print(func):
    print("print_content")
    def print_content():
        print("starting!")
        func()
        time.sleep(3)
        print("ending!")
    return print_content




# @count_time 
# @easy_print
# def test_a():
#     time.sleep(5)
#     print("睡觉了5秒")
    


@count_time
@easy_print
def test_b():
    time.sleep(1)
    print("睡觉了3秒")
    


if __name__ == '__main__':
    
    test_b()




