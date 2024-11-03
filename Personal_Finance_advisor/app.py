import pandas as pd
from flask import Flask, render_template, request
from sklearn.linear_model import LinearRegression

# Load sample financial data from the correct file name
finance_data = pd.read_csv('financial_data_investments.csv')

# Print the columns to debug (optional)
print("Columns in finance_data:", finance_data.columns.tolist())

# Check if required columns exist in the DataFrame
required_columns = ['Income', 'Expenses', 'Investments', 'Savings']
missing_columns = [col for col in required_columns if col not in finance_data.columns]

if missing_columns:
    raise ValueError(f"Missing columns in the dataset: {', '.join(missing_columns)}")

# Prepare the features and target variable
X = finance_data[['Income', 'Expenses', 'Investments']]
y = finance_data['Savings']

# Create and train the model
model = LinearRegression()
model.fit(X, y)

# Initialize the Flask application
app = Flask(_name_)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None  # Initialize prediction variable

    if request.method == 'POST':
        try:
            income = float(request.form['income'])
            expenses = float(request.form['expenses'])
            investments = float(request.form['investments'])

            # Prepare input data for prediction
            input_data = pd.DataFrame({
                'Income': [income],
                'Expenses': [expenses],
                'Investments': [investments]
            })

            # Make prediction using the trained model
            prediction = model.predict(input_data)[0]

        except ValueError:
            return render_template('index.html', error="Please enter valid numerical values.")

    return render_template('index.html', prediction=prediction)

if _name_ == '_main_':
    app.run(debug=True)