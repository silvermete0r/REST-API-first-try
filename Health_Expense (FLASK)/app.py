from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
model = pickle.load(open('expense_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods = ['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # Access the data from form
        age = int(request.form["age"])
        bmi = int(request.form["bmi"])
        children = int(request.form["children"])
        Sex = int(request.form["Sex"])
        Smoker = int(request.form["Smoker"])
        Region = int(request.form["Region"])
        
        # Get prediction
        input_cols = [[age, bmi, children, Sex, Smoker, Region]]
        prediction = model.predict(input_cols)
        output = round(prediction[0], 2)
        return render_template("index.html", prediction_val='{} $'.format(output))

if __name__ == "__main__":
    app.run(debug=True)