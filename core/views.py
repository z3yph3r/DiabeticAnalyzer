from django.shortcuts import render
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score
from .disclaimer import disclaimer
diabetes_dataset=pd.read_csv("static/diabetes.csv")

diabetes_dataset.describe()

diabetes_dataset['Outcome'].value_counts()

x=diabetes_dataset.drop(columns='Outcome',axis=1).drop(columns='DiabetesPedigreeFunction',axis=1)
y=diabetes_dataset['Outcome']

scaler = StandardScaler()


def diabeticfunc(x,input_data,gender):
    if gender =="male":
        x=x.drop(columns="Pregnancies", axis=1)
    scaler.fit(x)
    
    standardized_data=scaler.transform(x)
    
    x= standardized_data
    
    X_train,X_test,Y_train,Y_test = train_test_split(x,y,test_size=0.2,stratify=y,random_state=2)
    
    classifier = svm.SVC(kernel='linear')
    classifier.fit(X_train,Y_train)
    
    input_data_as_np=np.asarray(input_data)

    input_data_reshape = input_data_as_np.reshape(1,-1)
    input_data_standardize = scaler.transform(input_data_reshape)
    
    prediction = classifier.predict(input_data_standardize)
    return prediction

def home(request):
    return render(request,'home.html')

def male(request):
    
    patient_data=request.POST
    patient_name=patient_data.get('Patient_name')
    print(patient_name)
    if patient_name != None:
       age=patient_data.get('age')
       glucose=patient_data.get('glucose')
       bloodpressure=patient_data.get('bloodpressure')
       skinthickness=patient_data.get('skinthickness')
       insulin=patient_data.get('insulin')
       bmi=patient_data.get('bmi')
       patient_db=dict()
       patient_db['name']=patient_name
       patient_db['age']=age
       patient_db['glucose']=glucose
       patient_db['bloodpressure']=bloodpressure
       patient_db['skinthickness']=skinthickness
       patient_db['insulin']=insulin
       patient_db['bmi']=bmi
       patient_db['disclaimer']=disclaimer
       input_report=(glucose,bloodpressure,skinthickness,insulin,bmi,age)
       diabetic_bool=diabeticfunc(x,input_report,'male')
       print(input_report,diabetic_bool)
       if diabetic_bool[0] == 1:
           patient_db['res']="You're a Diabetic Patient"
       else:
           patient_db['res']="You're not a Diabetic Patient"
       return render(request,'male_result.html',{'patient_db':patient_db})
    else:
       return render(request,'male.html')
def female(request):
    patient_data=request.POST
    patient_name=patient_data.get('Patient_name')
    if patient_name != None:
       pregnencies=patient_data.get('pregnencies')
       age=patient_data.get('age')
       glucose=patient_data.get('glucose')
       bloodpressure=patient_data.get('bloodpressure')
       skinthickness=patient_data.get('skinthickness')
       insulin=patient_data.get('insulin')
       bmi=patient_data.get('bmi')
       
       patient_db=dict()
       patient_db['name']=patient_name
       patient_db['pregnencies']=pregnencies
       patient_db['age']=age
       patient_db['glucose']=glucose
       patient_db['bloodpressure']=bloodpressure
       patient_db['skinthickness']=skinthickness
       patient_db['insulin']=insulin
       patient_db['bmi']=bmi
       patient_db['disclaimer']=disclaimer
          
       input_report=(pregnencies,glucose,bloodpressure,skinthickness,insulin,bmi,age)
       diabetic_bool=diabeticfunc(x,input_report,'female')
       if diabetic_bool[0] == 1:
           patient_db['res']="You're a Diabetic Patient"
       else:
           patient_db['res']="You're not a Diabetic Patient"
       return render(request,'female_result.html',{'patient_db':patient_db})
    else:
       return render(request,'female.html')