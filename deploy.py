import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from flask import Flask, jsonify, request
import joblib

# Load the trained model and scaler
clf = joblib.load('model.pkl')
#scaler = joblib.load('scaler.pkl')

# Create a Flask app
app = Flask(__name__)

# Define a predict endpoint
@app.route('/predict', methods=['POST'])
def predict():
    # Parse the JSON input data
    input_data = request.get_json()
    df = pd.DataFrame(input_data, index=[0])

    # Preprocess the input data
    df = pd.get_dummies(df, columns=['gender', 'Partner', 'Dependents', 'PhoneService', 'MultipleLines',
                                     'InternetService', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection',
                                     'TechSupport', 'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling',
                                     'PaymentMethod'])
    #X = df.reindex(columns=scaler.get_feature_names_out()).values
    #X = scaler.transform(X)

    # Make a prediction
    prediction = clf.predict(df)

    # Convert the prediction to a string
    if prediction[0] == 0:
        churn_prediction = 'No churn'
    else:
        churn_prediction = 'Churn'

    # Return the prediction as JSON
    return jsonify({'Churn prediction': churn_prediction})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
