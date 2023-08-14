import asyncio
import time



def task_a():
        for temp in range(5):
            print("这是task_a： ",temp)  
            time.sleep(2)
        return 2

def task_b(num_b):
        result =1 
        print("result: ",result)
        for i in range(10000):
            result += 1
        print("result: ",result)
        result = result + num_b

        print("result: ",result)
        return result
                   
def main():
    temp =  task_a()
    finalReulst =  task_b(temp)
    print("finalReulst: ",finalReulst)

if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print("cost: ",end -start)