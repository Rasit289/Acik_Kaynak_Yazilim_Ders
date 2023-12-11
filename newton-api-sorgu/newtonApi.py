from flask import Flask, request  
from flask_restful import Api, Resource
import pandas as pd
import requests

app = Flask(__name__)
api = Api(app)

# türev,integral,sin,cos ve  basit matematiksel işlemleri yapan sınıf
class NewtonOperations(Resource):
    def get(self, operation, expression):
        try:
            url = f"https://newton.now.sh/api/v2/{operation}/{expression}"
            response = requests.get(url)
            data = response.json()
            return data, 200
        except requests.exceptions.RequestException as e:
	    # Eğer istekte hata olursa, hata mesajını ve 500 hata durum kodunu döndür
            return {'error': f'Newton API error: {e}'}, 500  


api.add_resource(NewtonOperations, '/newton/<string:operation>/<string:expression>')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=6767)