import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import accuracy_score, confusion_matrix
import pickle
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from os.path import join, dirname, realpath
import io

if __name__=='__main__':
    data = pd.read_csv("train1.csv")
    col = ['business','entertainment','politics','sport','tech']
    #Data Pre-Processing
    le_category = LabelEncoder()
    data['Encoded_Label'] = le_category.fit_transform(data.category)
    ohe_category = OneHotEncoder()
    temp = ohe_category.fit_transform(data.Encoded_Label.values.reshape(-1,1)).toarray()
    dataOneHot = pd.DataFrame(temp, columns = col)
    data = pd.concat([data, dataOneHot], axis=1)
    vector = TfidfVectorizer(stop_words='english')
    data_features = vector.fit_transform(data.iloc[:,1])
    filename='vect'
    pickle.dump(vector, open(filename, 'wb'))
    x_train, x_test, log_train, log_test = train_test_split(data_features, data.iloc[:,[3,4,5,6,7]], test_size=0.2)

    #Logistic Regression
    print("\n Logistic Regression ->\n")
    logreg = LogisticRegression(C=10,solver="liblinear")
    models={}
    avg_acc = 0
    model_acc = []
    for i in col:
        models[i] = logreg.fit(x_train, log_train[i])
        filename = "model_"+ str(i)
        pickle.dump(models[i], open(filename, 'wb'))
        y_pred = logreg.predict(x_test)
        acc = accuracy_score(log_test[i], y_pred)
        model_acc.append("{0:.2f}".format(acc*100))
        c_matrix = confusion_matrix(log_test[i], y_pred)
        avg_acc = avg_acc + acc
        print("\n Accuracy score for category "+str(i)+" using Logistic Regression: "+str(100*acc)+"%")
        print("\n Confusion Matrix for category "+str(i)+" using Logistic Regression: ")
        print(c_matrix)

    print("\n Average Accuracy Score for Logistic Regression: "+str(100*avg_acc/5)+"\n")
    print(model_acc)
    model_acc = [float(i) for i in model_acc]
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    ax.set_title('Comparison of testing accuracies for different labels')
    ax.set_xlabel('Labels')
    ax.set_ylabel('Model Accuracy')
    ax.set_xticklabels(col)
    ax.set_ylim([90,100])
    ax.bar(col,height = model_acc)
    for index,data in enumerate(model_acc):
        plt.text(x=index , y=data+0.2, s=f"{data}")
    path= join(dirname(realpath(__file__)), 'accuracy_score/')
    fig.savefig(path+"graph.jpg",bbox_inches = 'tight')
    print("Image saved!")

def myinput(text):
    col = ['business','entertainment','politics','sport','tech']
    input_string=[text]
    vec = pickle.load(open('vect', 'rb'))
    input_data = vec.transform(input_string)
    result = []
    mymodels={}
    for i in col:
        filename = 'model_'+str(i)
        loaded_model = pickle.load(open(filename, 'rb'))
        result.append(loaded_model.predict_proba(input_data)[0,1])
    
    col_no = result.index(max(result))
    return col[col_no], result
        


    