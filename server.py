import os
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(195779873e17a8da4d4ae7f535f241d8)

class Greeting (Resource):
    def get(self):
        return "Zaid Userbot is Up & Running!"

api.add_resource(Greeting, '/')
app.run(host="0.0.0.0", port=os.environ.get("PORT", 8080))
