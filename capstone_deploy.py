import time
import streamlit as st
import pandas as pd
import pickle

df_load = pickle.load(open('./source/data_final.pkl', 'rb'))
model_load = pickle.load(open('./source/model.pkl', 'rb'))
accuracy_load = pickle.load(open('./source/accuracy_model.pkl', 'rb'))
df_final = df_load["data"]

scaler = pickle.load(open("./source/scaler.pkl", "rb"))

def selected_model():
    with st.expander("CHOOSE MODEL PREDICTION"):
        mdl = st.selectbox(label="Select Model", options=["-", "KNN", "Random Forest", "Decision Tree"])
        if mdl == "Random Forest":
            model = model_load["rf"]
            accuracy = accuracy_load["accuracy_rf"]
        elif mdl == "KNN":
            model = model_load["knn"]
            accuracy = accuracy_load["accuracy_knn"]
        elif mdl == "Decision Tree":
            model = model_load["dt"]
            accuracy = accuracy_load["accuracy_dt"]
        else:
            model = None
            accuracy = None

    return mdl, model, accuracy

def input_data():
    st.sidebar.title('Input Data')

    
    with st.sidebar.expander("AGE"):
        # min_age = int(df_final["age"].min())
        # max_age = int(df_final["age"].max())
        age = st.number_input('Input Age', min_value=0, max_value=100, step=1)

    with st.sidebar.expander("SEX"):
        sex_sb = st.selectbox(
            label="Select Sex", options=["-", "Male", "Female"])
        if sex_sb == "Male":
            sex = 1
        elif sex_sb == "Female":
            sex = 0
        else:
            sex = None
        # -- Nilai 0: Wanita
        # -- Nilai 1: Pria

    with st.sidebar.expander("CHEST PAIN TYPE"):
        cp_sb = st.selectbox(
            label="Select Chest Pain Type",
            options=[
                "-",
                "Typical angina",
                "Atypical angina",
                "Non-anginal pain",
                "Asymptomatic",
            ],
        )
        if cp_sb == "Typical angina":
            cp = 1
        elif cp_sb == "Atypical angina":
            cp = 2
        elif cp_sb == "Non-anginal pain":
            cp = 3
        elif cp_sb == "Asymptomatic":
            cp = 4
        else:
            cp = None
        # -- Nilai 1: typical angina
        # -- Nilai 2: atypical angina
        # -- Nilai 3: non-anginal pain
        # -- Nilai 4: asymptomatic

    with st.sidebar.expander("RESTING BLOOD PRESSURE "):
        # trestbps = st.number_input(
        #     label="Resting BP (mm Hg)",
        #     min_value=int(df_final["trestbps"].min()),
        #     max_value=int(df_final["trestbps"].max()),
        # )
        trestbps = st.slider('Resting BP (mm Hg)', min_value=int(0), max_value=int(df_final["trestbps"].max()))
        # st.sidebar.write(
        #     f"Nilai :orange[Min]: :orange[**{df_final['trestbps'].min()}**], Nilai :red[Max]: :red[**{df_final['trestbps'].max()}**]"
        # )

    with st.sidebar.expander("SERUM CHOLESTORAL "):
        # chol = st.number_input(
        #     label="Serum Cholestoral (mg/dl)",
        #     min_value=int(df_final["chol"].min()),
        #     max_value=int(df_final["chol"].max()),
        # )
        chol = st.slider('Serum Cholestoral (mg/dl)', min_value=int(df_final["chol"].min()), max_value=int(df_final["chol"].max()))
 
    with st.sidebar.expander("FBS > 120 mg/dl?"):
        fbs_sb = st.selectbox(
            label="Fasting Blood Sugar > 120 mg/dl",
            options=["-","True", "False"],
        )
        if fbs_sb == "False":
            fbs = 0
        elif fbs_sb == "True":
            fbs = 1
        else:
            fbs = None
        # -- Nilai 0: False
        # -- Nilai 1: True

    with st.sidebar.expander("RESTING ECG"):
        restecg_sb = st.selectbox(
            label="Resting ECG",
            options=[
                "-",
                "Normal",
                "Having ST-T Wave Abnormality",
                "Showing probable or Definite Left Ventricular Hypertrophy",
            ],
        )
        if restecg_sb == "Normal":
            restecg = 0
        elif restecg_sb == "Having ST-T Wave Abnormality":
            restecg = 1
        elif restecg_sb == "Showing probable or Definite Left Ventricular Hypertrophy":
            restecg = 2
        else:
            restecg = None
        # -- Nilai 0: normal
        # -- Nilai 1: mengalami kelainan gelombang ST-T (Inversi gelombang T > 0.05 mV)
        # -- Nilai 2: menunjukkan hipertrofi ventrikel kiri

    with st.sidebar.expander("MAXIMUM HEART RATE"):
        # thalach = st.number_input(
        #     label="Maximum Heart Rate",
        #     min_value=int(df_final["thalach"].min()),
        #     max_value=int(df_final["thalach"].max()),
        # )
        thalach = st.slider('Maximum Heart Rate', min_value=int(df_final["thalach"].min()), max_value=int(df_final["thalach"].max()))

    with st.sidebar.expander("EXERCISE INDUCED ANGINA"):
        exang_sb = st.selectbox(
            label="Exercise induced angina?",
            options=["-","Yes", "No"],
        )
        if exang_sb == "No":
            exang = 0
        elif exang_sb == "Yes":
            exang = 1
        else:
            exang = None
        # -- Nilai 0: Tidak
        # -- Nilai 1: Iya

    with st.sidebar.expander("ST DEPRESSION"):
        # oldpeak = st.number_input(
        #     label="ST Depression induced by exercise relative to rest",
        #     min_value=float(df_final["oldpeak"].min()),
        #     max_value=float(df_final["oldpeak"].max()),
        #     step=0.5
        # )
        oldpeak = st.slider('ST Depression induced by exercise relative to rest', min_value=float(df_final["oldpeak"].min()), max_value=float(df_final["oldpeak"].max()), step=0.5)
        # st.sidebar.write(
        #     f"Nilai :orange[Min]: :orange[**{df_final['oldpeak'].min()}**], Nilai :red[Max]: :red[**{df_final['oldpeak'].max()}**]"
        # )

    # Menyusun data input ke dalam dataframe
    data_print = {
        "Age": [age],
        "Sex": [sex_sb],
        "Chest pain type": [cp_sb],
        "Resting BP (mm Hg)": [trestbps],
        "Serum Cholestoral (mg/dl)": [chol],
        "FBS > 120 mg/dl?": [fbs_sb],
        "Resting ECG": [restecg_sb],
        "Maximum heart rate": [thalach],
        "Exercise induced angina?": [exang_sb],
        "ST depression": [oldpeak],
    }
    
    data_process = {
        "age": [age],
        "sex": [sex],
        "cp": [cp],
        "trestbps": [trestbps],
        "chol": [chol],
        "fbs": [fbs],
        "restecg": [restecg],
        "thalach": [thalach],
        "exang": [exang],
        "oldpeak": [oldpeak],
    }

    
    df_print = pd.DataFrame(data_print, index=["INPUT"])
    df_process = pd.DataFrame(data_process, index=["input"])
    
    return df_print, df_process

def main():
    # Title
    st.title('Heart Disease Prediction')

    
    # Mengambil data input
    df_print, df_process = input_data()
    
    mdl, model, accuracy = selected_model()


    # Menampilkan data input dalam bentuk tabel
    if accuracy is not None:
        st.metric(label=f"{mdl} Accuracy", value=f"{accuracy*100:.1f} %")

        

    st.subheader('Data Input')
    # st.write(df_final)
    st.write(df_print.T)
    # st.write(df_process.T)

    submit = st.button('Submit', key='submit', type='primary')

    if model is None:
        st.toast('Please select model')
        # st.write('Please select model')
        return





    if submit:
        if df_process.isnull().sum().sum() > 0:
            submit = False
            st.toast('Please fill all the data')
            # st.write('Please fill all the data')
            return
        bar = st.progress(0)
        status_text = st.empty()
        for i in range(1, 101):
            status_text.text(f"{i}% complete")
            bar.progress(i)
            time.sleep(0.01)
            if i == 100:
                time.sleep(1)
                status_text.empty()
                bar.empty()

        # Proses prediksi
        

        df_scale = scaler.transform(df_process)


        pred = model.predict(df_scale)

        if pred == 0:
            result = ":green[**No Heart Disease**]"
        elif pred == 1:
            result = ":orange[**Heart Disease lv 1**]"
        elif pred == 2:
            result = ":orange[**Heart Disease lv 2**]"
        elif pred == 3:
            result = ":red[**Heart Disease lv 3**]"
        elif pred == 4:
            result = ":red[**Heart Disease lv 4**]"

        st.subheader(f'Prediction : {result}')

    

if __name__ == '__main__':
    main()
