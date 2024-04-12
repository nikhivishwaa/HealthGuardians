from django.http import JsonResponse
from rest_framework.views import APIView
from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd
import os
import joblib

print(os.path)
model = joblib.load(os.path.join('./ML Model/Diabeties/diabetes_model.joblib'))
scaler = StandardScaler()
X = pd.read_csv('./ML Model/Diabeties/diabetes.csv').drop(columns = 'Outcome', axis=1)
scaler.fit(X)

class Test(APIView):		
    def post(self, request):
        input_data = pd.DataFrame(request.data, index=[0])

        # standardize the input data
        std_data = scaler.transform(input_data)

        prediction = model.predict(std_data)[0]
        if prediction == 0:
            return JsonResponse({'diabetic':False})
        else:
            return JsonResponse({'diabetic':True})
    
    



