import asyncio
import time


a = []
a.next()


async def task_a():
            for temp in range(5):
                print("这是task_a： ",temp)
                await asyncio.sleep(2)
            return 2


async def task_b(num_b):
            result =1 
            print("result: ",result)
            for i in range(10000):
                result += 1
            print("result: ",result)

            result = result + num_b

            print("result: ",result)
            return result
                   
async def main():
       temp = await task_a()
       finalReulst = await task_b(temp)
       print("finalReulst: ",finalReulst)

if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print("cost: ",end -start)