from flask import Flask, request, jsonify, render_template
from utils import BikePricePrediction
import config

app = Flask(__name__,template_folder='template')

@app.route('/')
def home1():
    
    return render_template('Bikeprice.html')


# @app.route('/predict_prices', methods = ['GET'])
# def predict_charges():

#     if request.method == 'GET':
#         data = request.args.get
#         print("Data :",data)
#         Company = data('Company')
#         Country_of_Origin = data('Country_of_Origin')
#         Model = data('Model')
#         Number_of_cc = int(data('Number_of_cc'))
#         Horsepower = int(data('Horsepower'))
#         Transmission_Type = data('Transmission_Type')
#         Drivetrain = data('Drivetrain')
#         Number_of_Seating = int(data('Number_of_Seating'))
#         Year = int(data('Year'))
#         Looks = data('Looks')
#         Body_Type = data('Body_Type')
#         Engine_Type = data('Engine_Type')




#         Obj = BikePricePrediction(Company,Country_of_Origin,Model,Number_of_cc,Horsepower,Transmission_Type,Drivetrain,Number_of_Seating,Year,Looks,Body_Type,Engine_Type)
#         pred_price = Obj.get_predicted_price()
        
#         # return jsonify({"Result":f"Predicted Bike Prices == {pred_price}"})
#         return render_template('Bikeprice.html', prediction = pred_price)

#     # if request.method == 'POST':
@app.route('/BikePrice',methods=["POST"])
def BikePrice():
        data=request.form
        print('Data:',data)
        Company = data['Company']
        Country_of_Origin = data['origin']
        Model = data['Model']
        Number_of_cc = data['cc']
        Horsepower = data['horsepower']
        Transmission_Type = data['transmission']
        Drivetrain = data['drivetrain']
        Number_of_Seating = data['seating']
        Year = data['year']
        Looks = data['looks']
        Body_Type = data['bodytype']
        Engine_Type = data['enginetype']
  

        
        Obj1 = BikePricePrediction(Company,Country_of_Origin,Model,Number_of_cc,Horsepower,Transmission_Type,Drivetrain,Number_of_Seating,Year,Looks,Body_Type,Engine_Type)
        pred_price = Obj1.get_predicted_price()
        # return jsonify({"Result":f"Predicted Medical Charges == {pred_price}"})
        return render_template('Bikeprice.html', prediction = pred_price)

        # return jsonify({"Message" : "Unsuccessful"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=config.PORT_NUMBER,debug=True)
