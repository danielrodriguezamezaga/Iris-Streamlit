# Daniel Rodriguez Amezaga
# Install requeriments.txt for this app
# Run app: streamlit run IrisStreamlit.py

import streamlit as st
import pickle
import plotly.express as px

df = px.data.iris()

figure = px.scatter(df, x="sepal_length", y="sepal_width", 
                    color="species")
figure2 = px.scatter(df, x="petal_length", y="petal_width", 
                     color="species")
st.markdown("<h1 style='text-align: center;'>Iris Species</h1>", 
            unsafe_allow_html=True)
st.image(
            "https://www.embedded-robotics.com/wp-content/uploads/2022/01/Iris-Dataset-Classification.png",
            width=700,
        )

st.markdown("<h1 style='text-align: center;'>Width and length \
            of sepal chart</h1>", unsafe_allow_html=True)
st.plotly_chart(figure, use_container_width=False, 
                sharing="streamlit")

st.markdown("<h1 style='text-align: center;'>Width and length \
            of petal chart</h1>", unsafe_allow_html=True)
st.plotly_chart(figure2, use_container_width=False, 
                sharing="streamlit")

# I import the already trained model from jupyter NoteBook 
# and saved in a "savemodel.sav".
model = pickle.load(open('savemodel.sav', 'rb'))

def predict():
    result = ''
    result = model.predict([[sepal_length, sepal_width, 
                            petal_length, petal_width]])[0]
    
    return st.write("The Predict is... ", result)

st.markdown("<h1 style='text-align: center;'>Iris Predict </h1>", 
            unsafe_allow_html=True)

sepal_length = st.number_input("Insert sepal length: ")
sepal_width = st.number_input("Insert sepal width: ")
petal_length = st.number_input("Insert petal length: ")
petal_width = st.number_input("Insert petal width: ")

predict()

