from sanic import Sanic,Request
from sanic.response import text,json
import time
import asyncio


app = Sanic("my_first_Sanic")


@app.get("/slow")
def getSlow(request):
    time.sleep(3)
    print("request_id: ",request.id)
    print("requst_port",request.port)
    return text("slow")

@app.post("/fast")
async def getFast(request):
    
    print("request_id: ",request.id)
    print("requst_port",request.port)
    print("requst content: ",request.json)
    print("request_args: ",request.query_args)
    id = str(request.id)
    return json({"name":"lujun","request_id":id},status=666)



if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8088)