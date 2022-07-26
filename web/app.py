from ast import Add
from pycaret.classification import load_model, predict_model
import streamlit as st

model = load_model('deployment_26072022')

def predict(model, input_df):
    predictions_df = predict_model(extimator=model, data=input_df)
    predictions = predictions_df['Label'][0]
    return predictions


def run():
    st.write("""
    # Promental""")


    add_selectbox = st.sidebar.selectbox(
        "Como gostaria de prever?", 
        ("Online", "Bacht"))
    
    if add_selectbox == "Online":
        age = st.number_input("Qual sua idade?", min_value=0, max_value=100, value=18)
        if st.checkbox("Fumante"):
            fumante = 1
        else:
            fumante = 5
    

run()