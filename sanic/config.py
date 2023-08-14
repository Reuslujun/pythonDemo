from sanic import Sanic, Request
import time

class defineRequest(Request):

    @classmethod
    def define_id(*args):
        return time.time_ns()
    
