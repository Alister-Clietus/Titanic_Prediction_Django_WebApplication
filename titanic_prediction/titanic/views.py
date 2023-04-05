from django.shortcuts import render
from titanic.models import Data
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib


def index(request):
    return render(request, 'home.html')

def predictions(request):
    if request.method=='POST':
      name=request.POST.get('name',None)
      PClass=int(request.POST.get('pclass',None))
      Sex=int(request.POST.get('sex',None))
      Age=int(request.POST.get('age',None))
      Sibsp=int(request.POST.get('sibsp',None))
      Parch=int(request.POST.get('parch',None))
      Fare=int(request.POST.get('fare',None))
      Embarked=int(request.POST.get('embarked',None))

      ml_model = joblib.load('ml_model/titanic_prediction.joblib')
      prediction = ml_model.predict(
        [[PClass,Sex,Age,Sibsp,Parch,Fare,Embarked]])
      
      temp = Data.objects.create(
         name=name,
         PClass=PClass,
         Sex=Sex,Age=Age,Sibsp=Sibsp,Parch=Parch,
         Fare=Fare,Embarked=Embarked,predictions=prediction[0])
      temp.save()

      predict = prediction[0]
      final={'name':name,'predict':predict}
      return render(request,'suc.html',{'final':final})
    else:
      return render(request, 'predictions.html')



