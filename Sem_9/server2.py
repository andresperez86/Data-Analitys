from flask import Flask, request, render_template
import pickle
import numpy as np
import os

app = Flask(__name__)

# Load the model
model = pickle.load(open('dtmodel.pckl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract values from form inputs
        x1 = float(request.form['x1'])
        x2 = float(request.form['x2'])

        # Make prediction
        prediction = model.predict([[x1, x2]])[0]
        return render_template('index.html', prediction_text=f'The predicted class is: {prediction}')
    except Exception as e:
        return render_template('index.html', prediction_text=f'Error: {str(e)}')

if __name__ == '__main__':
    # Verify that the index.html file exists in the templates directory
    template_path = os.path.join(app.root_path, 'templates', 'index.html')

    if not os.path.exists(template_path):
        raise FileNotFoundError(f'Template "index.html" not found at: {template_path}')
    else:
        print(f'Template found: {template_path}')

    app.run(debug=True, host='127.0.0.1', port=7766)
