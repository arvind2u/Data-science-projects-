from flask import Flask, request
import pickle 
import numpy as np 

local_classifier = pickle.load(open('classifier.pickle', 'rb'))
local_scaler = pickle.load(open('sc.pickle', 'rb'))

app = Flask(__name__)

@app.route('/model', methods=['POST'])
def flask_app():
    request_data = request.get_jason(froce=True)
    age = request_data['age']
    EstimatedSalary = request_data['EstimatedSalary']
    prediction = local_classifier.prediction_scler(local_scaler.transform(np.array([[age, EstimatedSalary]])))
    
    
    return "The prediction is {}".format(prediction)

if __name__ == "__main__":
   app.run(port=8009, debug=True)  