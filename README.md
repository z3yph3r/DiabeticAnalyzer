# DiabeticAnalyzer

Django web application designed to predict whether a person having diabetes or havn't based on certain input features.By using pandas, numpy, and scikit-learn libraries for data manipulation, analysis, and machine learning.

### Features

- User-friendly web interface for inputting data.
- Utilizes a pre-trained machine learning model to predict diabetes probability.
- Displays the prediction result along with relevant information.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/riz4d/DiabeticAnalyzer
   cd DiabeticAnalyzer
   ```

2. Create a virtual environment (recommended) and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Start the development server:

   ```bash
   python manage.py runserver
   ```

5. Access the application in your browser at `http://127.0.0.1:8000/`.

### Usage

1. Fill out the input form with relevant data such as age, BMI, glucose levels, etc.
2. Click the "Check" button to see the predicted probability of having diabetes.
3. The application will display the prediction result along with additional insights.

### DataSet

The Dataset for predicting diabetes is stored in the `/static/diabetes.csv` file. It is trained using the scikit-learn library and takes input features to make predictions.

### Note

```bash
The accuracy and reliability of the predictions made by the machine learning model are subject to various factors,
 including the quality of the dataset, the features used for prediction, and the limitations of the model itself.
The model's predictions should not be considered as a definitive diagnosis, and users are strongly advised to consult
 with qualified medical professionals for accurate medical guidance.
```
<br><b>limitation</b>
```bash
It's important to note that the machine learning model is built on historical data and patterns and may not encompass
 all potential variables that can impact an individual's health status. The model's predictions are based on statistical
correlations and probabilities and should not be interpreted as a definitive diagnosis

```
### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

