import pickle
import json
import numpy as np
import config


class BikePricePrediction():
    def __init__(self,Company,Country_of_Origin,Model,Number_of_cc,Horsepower,Transmission_Type,Drivetrain,Number_of_Seating,Year,Looks,Body_Type,Engine_Type):
        print("****** INIT Function *********")
        self.Company = Company
        self.Country_of_Origin = Country_of_Origin
        self.Model = Model
        self.Number_of_cc = Number_of_cc
        self.Horsepower = Horsepower
        self.Transmission_Type = Transmission_Type
        self.Drivetrain = Drivetrain
        self.Looks = Looks
        self.Number_of_Seating = Number_of_Seating
        self.Year = Year
        self.Body_Type = Body_Type
        self.Engine_Type = Engine_Type
        

    def __load_saved_data(self):

        with open(config.MODEL_FILE_PATH,'rb') as f:
            self.model = pickle.load(f)

        with open(config.JSON_FILE_PATH,'r') as f:
            self.json_data = json.load(f)

    def get_predicted_price(self):
        self.__load_saved_data()

        Company = self.json_data['Company'][self.Company]
        Country_of_Origin = self.json_data['Country_of_Origin'][self.Country_of_Origin]
        Model = self.json_data['Model'][self.Model]   
        Transmission_Type = self.json_data['Transmission_Type'][self.Transmission_Type]
        Drivetrain = self.json_data['Drivetrain'][self.Drivetrain]
        Looks = self.json_data['Looks'][self.Looks]
        Body_Type = self.json_data['Body_Type'][self.Body_Type]
        Engine_Type = self.json_data['Engine_Type'][self.Engine_Type]
        

        # region_index = self.json_data["Column Names"].index(region)

        test_array = np.zeros([1,self.model.n_features_in_])
        test_array[0,0] = Company
        test_array[0,1] = Country_of_Origin
        test_array[0,2] = Model
        test_array[0,3] = self.Number_of_cc
        test_array[0,4] = self.Horsepower
        test_array[0,5]= Transmission_Type
        test_array[0,6] = Drivetrain  
        test_array[0,7] = self.Number_of_Seating
        test_array[0,8] = self.Year
        test_array[0,9] = Looks
        test_array[0,10] = Body_Type
        test_array[0,11] = Engine_Type

        predicted_charges = np.around(self.model.predict(test_array)[0],3)
        # print(predicted_charges)
        return predicted_charges
# obj = BikePricePrediction("Aprilia","India","Octane",1200,100,"Automatic","Chain",2,2023,"Sport","Naked","Single-cylinder")
# obj.get_predicted_price()



