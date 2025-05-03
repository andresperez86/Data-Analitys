
# Import necessary libraries
from flask import Flask, request, redirect, url_for, flash, jsonify  # Flask web framework components
import pickle  # For loading the trained model
import json    # To handle JSON data
import numpy as np  # For numerical operations and array handling

# Create a Flask application instance
app = Flask(__name__)

# Define a route to handle POST requests at the '/predict' endpoint
@app.route('/predict', methods=['POST'])
def predict():
    # Receive and parse JSON data from the incoming request
    data = request.get_json()
    
    # Log the input for debugging purposes
    print("LOG: predicting on input", data)
    
    # Predict the output using the loaded model
    # The input 'data' must be a 2D list (e.g., [[1, 0]])
    prediction = np.array2string(model.predict(data))
    
    # Log the prediction result
    print("LOG: returning predictions", prediction)
    
    # Return the prediction as a JSON response
    return jsonify(prediction)

# Entry point of the application
if __name__ == '__main__':
    # Define the path to the trained model file
    modelfile = 'dtmodel.pckl'
    
    # Load the trained model using pickle
    model = pickle.load(open(modelfile, 'rb'))
    
    # Log the loaded model type for confirmation
    print("LOG: serving model", model.__class__.__name__)

     # Test the model with a sample input to ensure it's working
    test_input = [[1, 0]]
    test_prediction = model.predict(test_input)
    print("LOG: test prediction for input {} is {}".format(test_input, test_prediction))
   
    # Start the Flask development server on localhost, port 7766
    app.run(debug=True, host='127.0.0.1', port=7766)
