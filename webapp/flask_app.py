from flask import Flask, request
from flask_restful import Resource, Api 
from datetime import date
import os

app = Flask(__name__)
api = Api(app)

class FizzBuzz(Resource):

    def post(self):
        #store start date and end date 
        self.input = request.json['input']

        if self.input > 0 :
            return self.fizzbuzz(), 200
        else:
            return "Invalid number" ,400

    def fizzbuzz(self):
        five = False
        three = False
        if self.input % 5 == 0:
            five = True
        if self.input % 3 == 0:
            three = True
        if five and three:
            return "fizzbuzz"
        elif five == True and three == False:
            return "buzz"
        elif five == False and three == True:
            return "fizz"
        else:
            return str(self.input)
            
api.add_resource(FizzBuzz, '/fizzbuzz')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ['WEBAPP_PORT'], debug=True) 