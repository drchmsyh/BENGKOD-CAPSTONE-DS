import streamlit as st
import pandas as pd

def input_data():
    st.sidebar.title('Input Data')

    with st.sidebar.expander("AGE"):
        age = st.number_input('Input Age', min_value=0, max_value=100, value=0, step=1)

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
        trestbps = st.number_input(
            label="Resting BP (mm Hg)",
            # min_value=int(df_final["trestbps"].min()),
            # max_value=int(df_final["trestbps"].max()),
        )
        # st.sidebar.write(
        #     f"Nilai :orange[Min]: :orange[**{df_final['trestbps'].min()}**], Nilai :red[Max]: :red[**{df_final['trestbps'].max()}**]"
        # )

    with st.sidebar.expander("SERUM CHOLESTORAL "):
        chol = st.number_input(
            label="Serum Cholestoral (mg/dl)",
            # min_value=int(df_final["chol"].min()),
            # max_value=int(df_final["chol"].max()),
        )
        # st.sidebar.write(
        #     f"Nilai :orange[Min]: :orange[**{df_final['chol'].min()}**], Nilai :red[Max]: :red[**{df_final['chol'].max()}**]"
        # )
 
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
        thalach = st.number_input(
            label="Maximum Heart Rate",
            # min_value=int(df_final["thalach"].min()),
            # max_value=int(df_final["thalach"].max()),
        )
        # st.sidebar.write(
        #     f"Nilai :orange[Min]: :orange[**{df_final['thalach'].min()}**], Nilai :red[Max]: :red[**{df_final['thalach'].max()}**]"
        # )

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
        oldpeak = st.number_input(
            label="ST Depression induced by exercise relative to rest",
            # min_value=float(df_final["oldpeak"].min()),
            # max_value=float(df_final["oldpeak"].max()),
        )
        # st.sidebar.write(
        #     f"Nilai :orange[Min]: :orange[**{df_final['oldpeak'].min()}**], Nilai :red[Max]: :red[**{df_final['oldpeak'].max()}**]"
        # )

    # Menyusun data input ke dalam dataframe
    data = {
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
    df = pd.DataFrame(data, index=["input"])
    return df

def main():
    # Title
    st.title('Heart Disease Prediction')
    
    # Mengambil data input
    df = input_data()
    
    # Menampilkan data input dalam bentuk tabel
    st.subheader('Data Input')
    st.write(df.T)

    submit = st.button('Submit', key='submit', type='primary')

    if submit:
        st.text('test')
        # Proses prediksi
        # pred = predict(df)
        # st.write('Prediction:', pred)

    

if __name__ == '__main__':
    main()
