import pickle
import pandas as pd
import numpy as np


def predict(age, sex, embarked):
    with open("./model/trained.pkl", "rb") as file:
        clf = pickle.load(file)
    data = np.array([[age, embarked, sex]])
    df = pd.DataFrame(data, columns=["Age", "Embarked", "Sex"])
    df.Age = df.Age.astype(int)
    transDf = pd.get_dummies(df)
    defaultData = pd.DataFrame([], columns=[
                               "Age",	"Embarked_C",	"Embarked_Q",	"Embarked_S",	"Sex_female",	"Sex_male"])
    transData = defaultData.append(transDf).fillna(value=0)
    return clf.predict(transData)[0]
