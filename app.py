from flask import Flask, render_template, request, url_for
import pickle
from flask.templating import Environment
import sklearn
app = Flask(__name__)

model = pickle.load(open('model\model.pkl','rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET','POST'])
def predict():

    if request.method == 'POST':
        day = int(request.form["Day"])
        month = int(request.form['Month'])
        source = request.form['From']
        
        if source == "Delhi":
            Source_Delhi = 1
            S_Mumbai = 0
            S_Chennai = 0
            S_Kolkata = 0
        elif source == "Mumbai":
            Source_Delhi = 0
            S_Mumbai = 1
            S_Chennai = 0
            S_Kolkata = 0
        elif source == "Chennai":
            Source_Delhi = 0
            S_Mumbai = 0
            S_Chennai = 1
            S_Kolkata = 0
        elif source == "Kolkata":
            Source_Delhi = 0
            S_Mumbai = 0
            S_Chennai = 0
            S_Kolkata = 1
        else:
            Source_Delhi = 0
            S_Mumbai = 0
            S_Chennai = 0
            S_Kolkata = 0

        destination = request.form['To']

        if destination == "Cochin":
            D_Cochin = 1
            D_Delhi = 0
            D_Hyderabad = 0
            D_Kolkata = 0
            D_New_Delhi = 0
        elif destination == "Delhi":
            D_Cochin = 0
            D_Delhi = 1
            D_Hyderabad = 0
            D_Kolkata = 0
            D_New_Delhi = 0
        elif destination == "Hyderabad":
            D_Cochin = 0
            D_Delhi = 0
            D_Hyderabad = 1
            D_Kolkata = 0
            D_New_Delhi = 0
        elif destination == "Kolkata":
            D_Cochin = 0
            D_Delhi = 0
            D_Hyderabad = 0
            D_Kolkata = 1
            D_New_Delhi = 0
        elif destination == "New Delhi":
            D_Cochin = 0
            D_Delhi = 0
            D_Hyderabad = 0
            D_Kolkata = 0
            D_New_Delhi = 1
        else:
            D_Cochin = 0
            D_Delhi = 0
            D_Hyderabad = 0
            D_Kolkata = 0
            D_New_Delhi = 0

        airline = request.form['Airline']

        if airline == "Air India":
            Air_India = 1
            GoAir = 0
            IndiGo = 0
            Jet_Airways = 0	
            Jet_Airways_Business = 0	
            Multiple_carriers = 0
            Multiple_carriers_Premium_economy = 0	
            SpiceJet = 0
            Trujet = 0
            Vistara	 = 0
            Vistara_Premium_economy = 0
        elif airline == "GoAir":
            Air_India = 0
            GoAir = 1
            IndiGo = 0
            Jet_Airways = 0	
            Jet_Airways_Business = 0	
            Multiple_carriers = 0
            Multiple_carriers_Premium_economy = 0	
            SpiceJet = 0
            Trujet = 0
            Vistara	 = 0
            Vistara_Premium_economy = 0
        elif airline == "IndiGo":
            Air_India = 0
            GoAir = 0
            IndiGo = 1
            Jet_Airways = 0	
            Jet_Airways_Business = 0	
            Multiple_carriers = 0
            Multiple_carriers_Premium_economy = 0	
            SpiceJet = 0
            Trujet = 0
            Vistara	 = 0
            Vistara_Premium_economy = 0
        elif airline == "Jet Airways":
            Air_India = 0
            GoAir = 0
            IndiGo = 0
            Jet_Airways = 1
            Jet_Airways_Business = 0	
            Multiple_carriers = 0
            Multiple_carriers_Premium_economy = 0	
            SpiceJet = 0
            Trujet = 0
            Vistara	 = 0
            Vistara_Premium_economy = 0
        elif airline == "Jet Airways Bussiness":
            Air_India = 0
            GoAir = 0
            IndiGo = 0
            Jet_Airways = 0	
            Jet_Airways_Business = 1
            Multiple_carriers = 0
            Multiple_carriers_Premium_economy = 0	
            SpiceJet = 0
            Trujet = 0
            Vistara	 = 0
            Vistara_Premium_economy = 0
        elif airline == "Multiple carriers":
            Air_India = 0
            GoAir = 0
            IndiGo = 0
            Jet_Airways = 0	
            Jet_Airways_Business = 0	
            Multiple_carriers = 1
            Multiple_carriers_Premium_economy = 0	
            SpiceJet = 0
            Trujet = 0
            Vistara	 = 0
            Vistara_Premium_economy = 0
        elif airline == "Multiple carriers Premium economy":
            Air_India = 0
            GoAir = 0
            IndiGo = 0
            Jet_Airways = 0	
            Jet_Airways_Business = 0	
            Multiple_carriers = 0
            Multiple_carriers_Premium_economy = 1	
            SpiceJet = 0
            Trujet = 0
            Vistara	 = 0
            Vistara_Premium_economy = 0
        elif airline == "SpiceJet":
            Air_India = 0
            GoAir = 0
            IndiGo = 0
            Jet_Airways = 0	
            Jet_Airways_Business = 0	
            Multiple_carriers = 0
            Multiple_carriers_Premium_economy = 0	
            SpiceJet = 1
            Trujet = 0
            Vistara	 = 0
            Vistara_Premium_economy = 0
        elif airline == "TruJet":
            Air_India = 0
            GoAir = 0
            IndiGo = 0
            Jet_Airways = 0	
            Jet_Airways_Business = 0	
            Multiple_carriers = 0
            Multiple_carriers_Premium_economy = 0	
            SpiceJet = 0
            Trujet = 1
            Vistara	 = 0
            Vistara_Premium_economy = 0
        elif airline == "Vistara":
            Air_India = 0
            GoAir = 0
            IndiGo = 0
            Jet_Airways = 0	
            Jet_Airways_Business = 0	
            Multiple_carriers = 0
            Multiple_carriers_Premium_economy = 0	
            SpiceJet = 0
            Trujet = 0
            Vistara	 = 1
            Vistara_Premium_economy = 0
        elif airline == "Vistara Premium economy":
            Air_India = 0
            GoAir = 0
            IndiGo = 0
            Jet_Airways = 0	
            Jet_Airways_Business = 0	
            Multiple_carriers = 0
            Multiple_carriers_Premium_economy = 0	
            SpiceJet = 0
            Trujet = 0
            Vistara	 = 0
            Vistara_Premium_economy = 1
        else:
            Air_India = 0
            GoAir = 0
            IndiGo = 0
            Jet_Airways = 0	
            Jet_Airways_Business = 0	
            Multiple_carriers = 0
            Multiple_carriers_Premium_economy = 0	
            SpiceJet = 0
            Trujet = 0
            Vistara	 = 0
            Vistara_Premium_economy = 0

        stops = request.form['Stops']
        Total_Stops = int(stops)

        prediction = model.predict([[
        Total_Stops,
        Air_India,
        GoAir,
        IndiGo,	
        Jet_Airways,	
        Jet_Airways_Business,	
        Multiple_carriers,	
        Multiple_carriers_Premium_economy,	
        SpiceJet,	
        Trujet,	
        Vistara,	
        Vistara_Premium_economy,	
        S_Chennai,
        Source_Delhi,	
        S_Kolkata,	
        S_Mumbai,	
        D_Cochin,	
        D_Delhi,	
        D_Hyderabad,	
        D_Kolkata,	
        D_New_Delhi,	
        day,
        month]])

        output=round(prediction[0],2)

        return render_template('index.html',prediction_text="Your Predicted Flight price is Rs. {}".format(output))


    return render_template("index.html")


if __name__=='__main__':
    app.run()