# app.py
from sanic import Sanic
from sanic.response import text

# 创建Sanic应用实例
app = Sanic(__name__)

# 定义一个简单的路由处理器
@app.route("/hello")
async def hello(request):
    
    print("nihao! Sanic")
    return text("Hello, Sanic!")

@app.route("/lujun")
async def getName(request):
    return text("卢俊")


# 运行应用
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8001)
