import time

# list_a  = [i for i in range(10)]
# iter_list_a = iter(list_a)


# while True:
#     try:
#         result = iter_list_a.__next__()
#         print("result: ",result)
#     except StopIteration as e:
#         break


class iterDemo:
    def __init__(self,max_num):
        self.max_num = max_num
    
    def __iter__(self):
        self.fistNum = 1
        return self

    def __next__(self):
        if self.fistNum <= self.max_num:
            self.fistNum += 1
            print("fistNum: ",self.fistNum)
            return self.max_num-1
        else:
            raise StopIteration
        
if __name__ == '__main__':
    temp = iterDemo(5)
    temp_iter = iter(temp)
    while True:
        time.sleep(2)
        print(next(temp_iter))