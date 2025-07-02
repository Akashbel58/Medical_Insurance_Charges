
# Read & laod .pkl & .json files
# Logic to load model and features

import pickle
import json
import numpy as np
import pandas as pd

from config import MODEL_PATH, FEATURE_PATH, LABEL_ENC_DATAPATH


class MedicalInsurance():

    def __init__(self):
        # self.data = data
        pass

    # Load trained Model    
    def load_model(self):
        with open(MODEL_PATH, 'rb') as fp:
            self.lr_model = pickle.load(fp)
            # Ensure columns are in the same order as during training
            self.feature_names = self.lr_model.feature_names_in_
            print(self.feature_names)
        return self.feature_names
    
    # Load columns and encoded data
    def load_columns_encoded_data(self):
        with open(FEATURE_PATH, 'r') as f1, \
             open(LABEL_ENC_DATAPATH, 'r') as f2:
            self.column_names = json.load(f1)
            self.label_data = json.load(f2)
        # print(self.column_names)
        # print(self.label_data)

        return self.label_data
    
        
    # Get user input for testing
    def get_user_input(self):

        self.load_model()
        self.load_columns_encoded_data()

        age         = int(self.data['age'])
        gender      = self.data['gender']
        bmi         = float(self.data['bmi'])
        children    = int(self.data['children'])
        smoker      = self.data['smoker']
        region      = self.data['region']

        test_array = np.zeros((1, self.feature_names.size))

        test_array[0,0] = age
        test_array[0,1] = self.label_data['gender'][gender]
        test_array[0,2] = bmi
        test_array[0,3] = children
        test_array[0,4] = self.label_data['smoker'][smoker]

        region = f'region_{region}'
        region_index = np.where(self.feature_names == region)[0][0]
        test_array[0,region_index] = 1

        # Create df of user input 
        self.df_test = pd.DataFrame(test_array, columns = self.feature_names)
        # print(self.df_test)

    # Prediction
    def predict_charges(self, data):
        self.data = data
        self.get_user_input()

        self.prediction = self.lr_model.predict(self.df_test)[0]
        print('Prediction Price is :', np.around(self.prediction,3))
        return self.prediction
    
    # Save user_input to database
    def save_data_in_db(self, testing_data_collection):

        input_data = dict(self.data)
        print(input_data)
        input_data.update({'Prediction':self.prediction})
        testing_data_collection.insert_one(input_data)
        return "Sucessful"

