from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
# load the model
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    result = ''
    return render_template('index.html', **locals())


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    Accel =float(request.form['Accel'])
    TopSpeed =float(request.form['TopSpeed'])
    Range =float(request.form['Range'])
    Efficiency =float(request.form['Efficiency'])
    FastCharge =float(request.form['FastCharge'])
    RapidCharge =float(request.form['RapidCharge'])
    PowerTrain =float(request.form['PowerTrain'])
    PlugType =float(request.form['PlugType'])
    Segment =float(request.form['Segment'])
    Seats =float(request.form['Seats'])
    PriceINR_in_Lakhs =float(request.form['PriceINR_in_Lakhs'])
    


    result = model.predict([[Accel	,TopSpeed	,Range,	Efficiency,	FastCharge,	RapidCharge	,PowerTrain,	PlugType,	Segment	,Seats,	PriceINR_in_Lakhs]])[0]
    return render_template('index.html', **locals())

if __name__ == '__main__':
    app.run(debug=True)