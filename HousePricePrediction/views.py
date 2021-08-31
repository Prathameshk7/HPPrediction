from django.shortcuts import render
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import numpy as np
import matplotlib.pyplot as plt
def home(request):
    return render(request, "home.html")

def predict(request):
    return render(request, "predict.html")

def result(request):

    var1 = float(request.GET['n1'])
    var2 = float(request.GET['n2'])
    var3 = float(request.GET['n3'])
    var4 = float(request.GET['n4'])
    var5 = float(request.GET['n5'])
    return render(request, "predict.html",{"result2":send_var(var1,var2,var3,var4,var5)})

def send_var(avgAIn,avgHa,nofrooms,nofbed,Apop):
    data = pd.read_csv('USA_Housing.csv')
    data = data.drop(['Address'],axis=1)

    X = data.drop('Price',axis=1)
    Y = data['Price']

    X_train,X_test, Y_train, Y_test = train_test_split(X,Y,test_size=.30)

    model = LinearRegression()
    model.fit(X_train, Y_train)

    '''var1 = float(avgAIn)
    var2 = float(avgHa)
    var3 = float(nofrooms)
    var4 = float(nofbed)
    var5 = float(Apop)'''
    pred = model.predict(np.array([[avgAIn,avgHa,nofrooms,nofbed,Apop]]))
    pred = round(pred[0])

    price = "The predicted price is $"+str(pred)

    return price