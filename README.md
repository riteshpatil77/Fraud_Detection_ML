
# 🛡️ PaySim Fraud Detection

An AI-powered financial fraud detection system built using **Machine Learning, Random Forest, FastAPI, and a modern fintech web interface**.

This project analyzes financial transactions and predicts whether a transaction is potentially fraudulent or legitimate.

## 🚀 Project Overview

Financial fraud detection is an important application of machine learning.

This project uses the PaySim synthetic mobile money transaction dataset to train a Random Forest classifier capable of identifying potentially fraudulent transactions.

The trained model is integrated with a FastAPI backend and an interactive fintech-inspired web application.

## ✨ Features

- Machine learning-based fraud detection
- Random Forest classification model
- Fraud probability estimation
- FastAPI REST API
- Interactive transaction input form
- Modern fintech-inspired dashboard
- Animated buttons and visual effects
- Swagger API documentation
- Real-time transaction prediction

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Pandas | Data manipulation |
| NumPy | Numerical operations |
| Scikit-learn | Machine learning |
| Random Forest | Fraud classification |
| FastAPI | Backend API |
| Uvicorn | API server |
| HTML | Frontend structure |
| CSS | Styling and animations |
| JavaScript | Frontend functionality |
| Joblib | Model serialization |

## 📊 Dataset

**PaySim Synthetic Financial Dataset**

Dataset source: [Kaggle - PaySim](https://www.kaggle.com/datasets/ealaxi/paysim1)

The dataset contains simulated mobile money transactions.

### Important Features

- `step` - Transaction time step
- `type` - Transaction type
- `amount` - Transaction amount
- `oldbalanceOrg` - Sender balance before transaction
- `newbalanceOrig` - Sender balance after transaction
- `oldbalanceDest` - Receiver balance before transaction
- `newbalanceDest` - Receiver balance after transaction
- `isFraud` - Target variable

### Target Variable

- `0` - Legitimate transaction
- `1` - Fraudulent transaction

## 🤖 Machine Learning Workflow

The project follows these steps:

1. Data loading and exploration
2. Exploratory Data Analysis (EDA)
3. Data preprocessing
4. Feature engineering
5. Train-test splitting
6. Handling class imbalance
7. Random Forest model training
8. Model evaluation
9. Model serialization using Joblib
10. FastAPI integration
11. Web application development

## 📈 Model Evaluation

The Random Forest model was evaluated using:

- Precision
- Recall
- F1-score
- Confusion Matrix
- Precision-Recall AUC

### Model Performance

| Metric | Score |
|---|---|
| Fraud Precision | 60.5% |
| Fraud Recall | 82.3% |
| Fraud F1-score | 70.0% |
| PR-AUC | 84.59% |

**Note:** These results are based on the evaluation performed during development. Results may vary depending on preprocessing, dataset splits, and model configuration.

## 📁 Project Structure

```text
PaySim-Fraud-Detection/
│
├── app.py
├── index.html
├── fraud_detection_model.pkl
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/riteshpatil77/PaySim-Fraud-Detection.git
```

### 2. Navigate to the project directory

```bash
cd PaySim-Fraud-Detection
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

For Windows:

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the application

```bash
uvicorn app:app --reload
```

## 🌐 Access the Application

Once the server is running, open the following URLs:

| Resource | URL |
|---|---|
| Web Application | http://127.0.0.1:8000 |
| API Documentation | http://127.0.0.1:8000/docs |
| Health Check | http://127.0.0.1:8000/health |

## 🔌 API Usage

### Endpoint

```http
POST /predict
```

### Example Request

```json
{
  "step": 100,
  "amount": 5000,
  "oldbalanceOrg": 10000,
  "newbalanceOrig": 5000,
  "oldbalanceDest": 20000,
  "newbalanceDest": 25000,
  "type": "TRANSFER"
}
```

### Example Response

```json
{
  "prediction": 0,
  "result": "Legitimate",
  "fraud_probability": 0.0
}
```

The response above is illustrative. Actual predictions depend on the trained model and transaction input.

## 🔮 Future Improvements

- Improve model performance
- Add transaction history
- Implement user authentication
- Add interactive analytics dashboard
- Deploy the application to a cloud platform
- Improve model monitoring
- Add additional machine learning models

## ⚠️ Disclaimer

This project is developed for educational and portfolio purposes using a synthetic dataset.

It is not intended for real-world financial decisions or production fraud prevention.

## 👨‍💻 Author

**Ritesh Patil**

BTech Artificial Intelligence and Machine Learning Engineering Student

- GitHub: [riteshpatil77](https://github.com/riteshpatil77)
- LinkedIn: [Ritesh Patil](https://www.linkedin.com/in/ritesh-patil-14398a38a/)

---

⭐ If you find this project interesting, feel free to explore the repository!
