import os
from django.shortcuts import redirect, render
import pandas as pd
from sklearn.preprocessing import LabelEncoder,StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR

def home(request):

    if request.method =='POST':

        data_file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data.csv')
        original_data = pd.read_csv(data_file_path)

        gender = original_data[['Gender']]

        gender_le = LabelEncoder().fit_transform(gender)

        x = original_data.iloc[:,:3]
        y = pd.DataFrame(data=gender_le,index=range(40),columns=['gender'])

        x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.30,random_state=0)

        svr_reg = SVR(kernel='rbf',degree=3)

        scaler_x = StandardScaler() # !!!!

        x_train_sc = scaler_x.fit_transform(x_train)

        svr_reg.fit(x_train_sc, y_train)
        

        user_data = pd.DataFrame({'Height': [request.POST['height']], 'Weight': [request.POST['weight']], 'Age': [request.POST['age']]})

        user_data_sc = scaler_x.transform(user_data) # !


        user_pred = svr_reg.predict(user_data_sc)

        if user_pred <=0.5:
            gender = "Female"
        else:
            gender = "Male"    

        return render(request,'result.html',{"gender":gender})
    
    return render(request,'home.html')

