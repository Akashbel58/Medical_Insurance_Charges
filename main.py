
# Import all required dependencies
from flask import Flask, request, jsonify, render_template
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import datetime

from app.utils import MedicalInsurance
from app.database import get_db
import config

# obj of MedicalInsurance class
insobj = MedicalInsurance()

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'secret-key'
jwt = JWTManager(app)

user_collection,testing_data_collection = get_db()

##################################################################

@app.route('/login.html')
def login_page():
    return render_template('login.html')

@app.route('/register.html')
def register_page():
    return render_template('register.html')

@app.route('/forgot.html')
def forgot_page():
    return render_template('forgot.html')

###################################################################
# user authentication api

@app.route('/medins/register', methods = ['POST'])
def register():
    user_data = request.form
    name = user_data.get('name', '')
    username = user_data.get('username', '')
    password = user_data.get('password', '')
    email_id = user_data.get('email_id', '')
    mobile_number = user_data.get('mobile_number', '')
    dob = user_data.get('dob', '')

    res = user_collection.find_one({'email_id':email_id})
    if res:
        return jsonify({"status": 'Error', "message" :  "User already exist"})
    else:
        user_collection.insert_one({"name":name, 'username':username, 'password':password,
                    'email_id':email_id, 'mobile_number':mobile_number, 'dob':dob})
        return jsonify({"status": 'Success', "message" :  "User Registerd Successfully"})


@app.route('/medins/login', methods = ['POST'])
def login():
    user_data = request.form
    username = user_data.get('username', '')
    password = user_data.get('password', '')

    res = user_collection.find_one({'username': username, 'password':password})
    if res :
        access_token = create_access_token(identity= username, expires_delta= datetime.timedelta(minutes=3))
        print('access_token :', access_token)
        return jsonify({"status": 'Success', "message" :  "Login Successful", 
                        'token': access_token})
    else:
        return jsonify({"status": 'Error', "message" :  "Invalid Credentials"})


@app.route('/medins/forgot', methods = ['POST'])
def forgot_password():
    user_data = request.form
    email_id = user_data.get('email_id', '')
    dob = user_data.get('dob','')
    # set new_password
    new_password = user_data.get('new_password', '')

    res =  user_collection.find_one({'email_id':email_id,'dob':dob})
    print(res)
    if res:
        user_collection.update_one({'email_id':email_id,'dob':dob}, 
                                   {"$set": {'password':new_password}})
        
        return jsonify({"status": 'Success', "message" :  "Password updated successfully"})
    
    else:
        return jsonify({"status": 'Error', "message" :  "User not exist"})
    


###################################################################
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gender_options', methods=['GET'])
@jwt_required()
def gender_options():
    col_data = insobj.load_columns_encoded_data()
    print(col_data)
    gender_values = list(col_data['gender'].keys())
    return jsonify(gender_values)


@app.route('/smoker_options', methods= ['GET'])
@jwt_required()
def smoker_options():
    col_data = insobj.load_columns_encoded_data()
    smoker_values = list(col_data['smoker'].keys())
    return jsonify(smoker_values)


@app.route('/region_options', methods = ['GET'])
@jwt_required()
def region_options():
    col_names = insobj.load_model()
    region_values = [col_name.replace('region_', '') for col_name in col_names if col_name.startswith('region_')]
    return jsonify(region_values)


@app.route('/prediction', methods = ['POST'])
@jwt_required()
def prediction():
    data = request.form

    predicted_charges = insobj.predict_charges(data)
    print(f'Prediction_charges: {predicted_charges}')

    res = insobj.save_data_in_db(testing_data_collection)
    if res:
        return jsonify({"message": "Result Successfully stored in Database", "result": f"Predicted Medical Insurance Charges : {predicted_charges}"})
    else:
        return jsonify({"message": "Error"})


if __name__ == '__main__': 
    app.run(host='0.0.0.0', debug=True)