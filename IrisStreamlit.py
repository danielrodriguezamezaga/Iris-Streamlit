# Daniel Rodriguez Amezaga
# Install requeriments.txt for this app
# Run app: streamlit run IrisStreamlit.py

import streamlit as st
import pickle
import plotly.express as px
import pandas as pd


df = px.data.iris()

# creating graphs with plotly
figure = px.scatter(df, x="sepal_length", y="sepal_width", 
                    color="species")
figure2 = px.scatter(df, x="petal_length", y="petal_width", 
                     color="species")

### display an image with streamlit ###
st.markdown("<h1 style='text-align: center;'>Iris Species</h1>", 
            unsafe_allow_html=True)
st.image(
            "https://www.embedded-robotics.com/wp-content/uploads/2022/01/Iris-Dataset-Classification.png",
            width=700,
        )
### display the graphs with streamlit ###
st.markdown("<h1 style='text-align: center;'>Width and length \
            of sepal chart</h1>", unsafe_allow_html=True)
st.plotly_chart(figure, use_container_width=False, 
                sharing="streamlit")

st.markdown("<h1 style='text-align: center;'>Width and length \
            of petal chart</h1>", unsafe_allow_html=True)
st.plotly_chart(figure2, use_container_width=False, 
                sharing="streamlit")

### Insert data ###
df = pd.read_csv('iris.csv')
# get the last value of the "ID" column in the dataframe
id = df.loc[df.index[-1], "id"]

st.sidebar.markdown("<h1 style='text-align: center;'>Insert Data </h1>", 
            unsafe_allow_html=True)
options_form = st.sidebar.form("options_form")
sepal_length_insert = options_form.number_input("sepal_length")
sepal_width_insert = options_form.number_input("sepal_width")
petal_length_insert = options_form.number_input("petal_length")
petal_width_insert = options_form.number_input("petal_width")
species_insert = options_form.text_input("species")
add_data = options_form.form_submit_button("Insert Data")
if add_data:
    # Save the values inserted by the web in the DataFrame
    st.write(sepal_length_insert, sepal_width_insert,
             petal_length_insert, petal_width_insert,
             species_insert)
    #last value of the ID column + 1 to insert the new value
    new_data = {"id": id +1,
                "sepal_length":sepal_length_insert,
                "sepal_width":sepal_width_insert,
                "petal_length":petal_length_insert,
                "petal_width":petal_width_insert,
                "species":species_insert}
    df = df.append(new_data, ignore_index=True)
    st.header("New file")
    st.write(df)
    df.to_csv('iris.csv', index=False)
    
### update data ###
st.sidebar.markdown("<h1 style='text-align: center;'>Update last Data </h1>", 
            unsafe_allow_html=True)
options_form3 = st.sidebar.form("options_form3")
id_update = options_form3.number_input("id")
sepal_length_update = options_form3.number_input("sepal_length")
sepal_width_update = options_form3.number_input("sepal_width")
petal_length_update = options_form3.number_input("petal_length")
petal_width_update = options_form3.number_input("petal_width")
species_update = options_form3.text_input("species")
updateData = options_form3.form_submit_button("Update Data")
if updateData:
    df = pd.read_csv('iris.csv')
    df.loc[df.index[-1], "id"] = id_update
    df.loc[df.index[-1], "sepal_width"] = sepal_length_update
    df.loc[df.index[-1], "sepal_length"] = sepal_width_update
    df.loc[df.index[-1], "petal_width"] = petal_length_update
    df.loc[df.index[-1], "petal_length"] = petal_width_update
    df.loc[df.index[-1], "species"] = species_update
    df.to_csv('iris.csv', index=False)

### Iris Predict ###    
# I import the already trained model from jupyter NoteBook 
# and saved in a "savemodel.sav".
model = pickle.load(open('savemodel.sav', 'rb'))

# Create function
def predict():
    result = model.predict([[sepal_length, sepal_width, 
                            petal_length, petal_width]])[0]
    st.sidebar.markdown("<h1 style='text-align: center;'>Predict</h1>", 
            unsafe_allow_html=True)
    # return value
    st.sidebar.write(result)

st.sidebar.markdown("<h1 style='text-align: center;'>Iris Predict </h1>", 
            unsafe_allow_html=True)
options_form2 = st.sidebar.form("options_form2")
sepal_length = options_form2.number_input("Sepal length: ")
sepal_width = options_form2.number_input("Sepal width: ")
petal_length = options_form2.number_input("Petal length: ")
petal_width = options_form2.number_input("Petal width: ")
add_data = options_form2.form_submit_button("Predict Iris")
if add_data:
    predict()