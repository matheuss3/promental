import pandas as pd
from joblib import load
import streamlit as st

import json

model = load("random_forest_sklearn.joblib")

def predict(model, input_df):
    # predictions_df = predict_model(estimator=model, data=input_df)
    predictions = model.predict(input_df)
    return predictions

def create_question(description, options):
    options_fmt = []
    for key, value in options.items():
        # if value == "":
        #     options_fmt.append(f"{key}")
        # else:
        options_fmt.append(f"{value} - {key}")


    question = st.selectbox(description, options_fmt)
    return question

def run():
    questions = json.load(open("questions.json", encoding="utf8"))
    st.write("""
    # Questionário""")


    st.sidebar.write("""
    # 🧠 Promental""")

    
    add_selectbox = st.sidebar.selectbox(
        "Como gostaria realizar o teste?", 
        ("Online", "Bacht"))
    
    
    if add_selectbox == "Online":
        input_dict = {}
        for question in questions:
            input_dict[question["column"]] = int(create_question(question["question"], question["options"]).split(" - ")[0])
        

        input_df = pd.DataFrame([input_dict])
        print(input_df)
        output = ""

        if st.button("Finalizar"):
            output = predict(model=model, input_df=input_df)
            output = '$' + str(output)
        
        st.success('O resultado é {}'.format(output))

run()