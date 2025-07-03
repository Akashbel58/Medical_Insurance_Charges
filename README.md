# 🩺 Medical Insurance Cost Prediction API

## 📘 Project Overview
A Flask-based API that predicts medical insurance costs using machine learning. The system includes user authentication, cost prediction, and MongoDB data storage.

---

## ✅ Features

### 🔐 User Authentication
- Registration with email verification  
- Login with JWT token  
- Password reset functionality  

### 💡 Insurance Prediction
- Machine learning model for cost prediction  
- Form with dynamic dropdown options  
- Result display with database storage  

### 🗃️ Database
- MongoDB for user data and prediction results  
- Secure password storage  

---

## ⚙️ Technologies Used

**Backend:**
- Python 3.x  
- Flask  
- Flask-JWT-Extended  
- pymongo  
- scikit-learn  

**Frontend:**
- HTML5  
- CSS3  
- JavaScript (vanilla)  

**Database:**
- MongoDB  

**Other:**
- JSON for data serialization  
- Pickle for model serialization  

---

## 📁 Project Structure

```text
medical-insurance-api/
├── app/
│   ├── __init__.py
│   ├── database.py         # MongoDB connection setup
│   ├── utils.py            # ML model loading and prediction logic
│   └── routes.py           # API endpoints
├── config.py               # Configuration variables
├── main.py                 # Main application entry point
├── requirements.txt        # Python dependencies
├── artifacts/
│   ├── lr_model.pkl        # Trained ML model
│   ├── feature.json        # Feature information
│   └── label_enc_data.json # Label encoding data
├── templates/
│   ├── index.html          # Main prediction page
│   ├── login.html          # User login page
│   ├── register.html       # User registration page
│   └── forgot.html         # Password reset page
└── README.md               # This file
```

---

## 🛠️ Installation & Setup

### 📋 Prerequisites
- Python 3.7+  
- MongoDB installed and running locally  
- pip package manager  

---

### 🔧 Installation

**Clone the repository:**

```bash
git clone https://github.com/yourusername/medical-insurance-api.git
cd medical-insurance-api
```

**Create and activate a virtual environment:**

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

**Install dependencies:**

```bash
pip install -r requirements.txt
```

**Set up MongoDB:**
- Ensure MongoDB is running locally on default port `27017`  
- The application will create the necessary collections automatically

---

## ⚙️ Configuration (`config.py`)

```python
# File paths
MODEL_PATH = 'artifacts/lr_model.pkl'
FEATURE_PATH = 'artifacts/feature.json'
LABEL_ENC_DATAPATH = 'artifacts/label_enc_data.json'

# Database configuration
MONGO_URL = 'mongodb://localhost:27017/'
DB_NAME = 'medins_db'
USER_CRED_COLLECTION_NAME = 'user_details'
TESTING_COLLECTION_NAME = 'testing_data'
```

---

## 🚀 Running the Application

**Start the Flask development server:**

```bash
python main.py
```

Visit the app at:  
[http://localhost:5000](http://localhost:5000)

---

## 🔗 API Endpoints

### 🔐 Authentication
- `POST /medins/register` — User registration  
- `POST /medins/login` — User login (returns JWT token)  
- `POST /medins/forgot` — Password reset  

### 📊 Prediction
- `GET /gender_options` — Get gender options (JWT required)  
- `GET /smoker_options` — Get smoker options (JWT required)  
- `GET /region_options` — Get region options (JWT required)  
- `POST /prediction` — Predict insurance charges (JWT required)  

---

## 🧪 Usage

1. Register a new user at `/register.html`  
2. Login at `/login.html` to get a JWT token  
3. Access the prediction form at `/index.html`  
4. Fill the form and submit to get predicted charges  

---

## 🌐 Frontend Pages

- **Login Page:** `/login.html`  
- **Registration Page:** `/register.html`  
- **Password Reset Page:** `/forgot.html`  
- **Prediction Form:** `/index.html`  

---

## 🧩 Troubleshooting

### ❌ MongoDB Connection Failed
- Ensure MongoDB is running  
- Check Mongo URL in `config.py`  

### 🔐 JWT Token Not Working
- Verify the token is in the `Authorization` header  
- Token might be expired (default expiry is 3 minutes)  

### ⚠️ Prediction Errors
- Ensure all required fields are provided  
- Model and feature files must exist in `artifacts/`  

### 🐞 Debugging Tips
- Set `debug=True` in `main.py`  
- Use browser dev tools to inspect API calls  

---

## 🌱 Future Enhancements

- Add email verification  
- Stronger password rules  
- Admin dashboard for viewing predictions  
- Deploy on a cloud platform  
- API documentation using Swagger or Redoc  

---

## 📄 License

This project is licensed under the **MIT License** — see the `LICENSE` file.

---

## 🙏 Acknowledgments

- Flask documentation  
- Scikit-learn documentation  
- MongoDB documentation  
- All open-source contributors ❤️
