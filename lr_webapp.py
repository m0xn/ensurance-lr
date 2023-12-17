import streamlit as st
from pickle import load
import numpy as np

models = load(open('lr_models.pkl', 'rb'))


# ------------- FUNCTION DEFINITIONS ------------------
def calculate_bmi(height_cm: int, weight_kg: int) -> None:
    height_m = height_cm/100
    return weight_kg / height_m**2


def overwrite_prediction(container_ref, raw_pred: float) -> None:
    eur_pred = usd_to_euro(raw_pred)
    with st.empty():
        container_ref.write(f"""
                            <style>@import url('https://fonts.googleapis.com/css2?family=Quantico&display=swap');</style>
                            <p style="font-size: 100px; font-family: 'Quantico', sans-serif; text-align: center; color: #00ff00;">{eur_pred:.2f}<span style="display: inline-block; font-size: 50px;">€</span></p>
                            <p style="font-size: 50px; font-family: 'Quantico', sans-serif; text-align: center; margin-top: -50px; color: #03b70f;">{raw_pred:.2f}<span style="display: inline-block; font-size: 25px;">$</span></p>
                            """,
                            unsafe_allow_html=True)


def usd_to_euro(amount: float) -> float:
    return amount*0.92


def format_entry(age: int, height_cm: int, weight_kg: int, raw_sex: str, raw_smoker: str, children: int) -> np.array:
    sex = 1 if raw_sex == 'Hombre' else 0
    smoker = 1 if raw_smoker == 'Sí' else 0
    bmi = calculate_bmi(height_cm, weight_kg)

    entry = np.array([age, bmi, sex, smoker, children]) \
        .reshape(1, -1)

    return entry


# ------------ WEB PAGE STRUCTURE -----------------

charge_container = st.empty()
charge_container.write("""
            <style>@import url('https://fonts.googleapis.com/css2?family=Quantico&display=swap');</style>
            <p style="font-size: 100px; font-family: 'Quantico', sans-serif; text-align: center; color: #ff0000;">0.00<span style="display: inline-block; font-size: 50px;">€</span></p>
            <p style="font-size: 50px; font-family: 'Quantico', sans-serif; text-align: center; margin-top: -50px; color: #b70603;">0.00<span style="display: inline-block; font-size: 25px;">$</span></p>
            """,
            unsafe_allow_html=True)

model_selection = st.selectbox(label='Versión del modelo',
                               options=models.keys())

age_col, bmi_col, sex_col, smoker_col, children_col = st.columns(5)

with age_col:
    age_ref = st.number_input(label='Edad',
                              min_value=1,
                              max_value=100)

with bmi_col:
    height_ref = st.number_input(label='Altura (cm)',
                                 min_value=1,
                                 max_value=300)
    weight_ref = st.number_input(label='Peso (kg)',
                                 min_value=1,
                                 max_value=200)

with sex_col:
    sex_ref = st.radio(label='Sexo',
                       options=['Hombre', 'Mujer'])

with smoker_col:
    smoker_ref = st.radio(label='¿Fumador?',
                          options=['Sí', 'No'])

with children_col:
    children_ref = st.number_input(label='Nº hijos',
                                   min_value=0)

with st.container():
    ref_button = st.button(label='¡Predecir 🔮!',
                           use_container_width=True)

warning_container = st.container(border=True)
warning_container.markdown("""
                            ⚠️ :orange[**Aviso**]: *La información que insertes dentro de los elementos de entrada
                           no será recolectada por la aplicación. Sólo será utilizada como entrada temporal
                           para los modelos de **Regresión Lineal***.
                           """)

st.title('Predicción del importe de un seguro')

st.markdown("""
            ## Introducción
            Esta web proporciona una interfaz interactiva con la que puedes probar distintos modelos
            de **Regresión Lineal** para predecir el importe del seguro de una persona con las características
            siguientes:
            - **Su edad**
            - **Su IMC** (*calculado a través de la altura y peso*)
            - **Su sexo**
            - **Si es fumador o no**
            - **El número de hijos que tenga**
            """)

st.markdown("""
            ## Características de los modelos
            He entrenado un total de **3 modelos de Regersión Lineal**. Cada uno es ligeramente diferente por
            la forma en la que calcula la **ecuación de la regresión**.

            Los 3 han sido entrenados a través de una base de datos de una **aseguradora estadounidense**.
            Más específicamente, se han entrenado a través de una muestra de **200 registros**.

            En lo que a rendimiento respecta, los 3 son **bastante similares**. Para este caso se entiende **rendimiento**
            como el **porcentaje de las predicciones del modelo** que se ajustan a los valores reales de la muestra tomada.
            Aún así, se podrían clasificar los modelos en orden decreciente de rendmiento de la siguiente forma:
            1. :green[LR Ridge] -> :green[~74.94%]
            2. :orange[LR Lasso] -> :orange[~74.72%]
            3. :red[LR Base] -> :red[~74.72%]

            Pese a que los dos últimos parecen tener rendimiento idéntico, el segundo tiene un **ajuste ligeramente mejor** de los
            coeficientes de la regresión.
            """)

# --------------- FUNCTIONALITY ----------------
selected_model = models[model_selection]

if ref_button:
    entry = format_entry(
            age_ref,
            height_ref,
            weight_ref,
            sex_ref,
            smoker_ref,
            children_ref)

    raw_charge = selected_model.predict(entry.reshape(1, -1))
    charge_usd = raw_charge.ravel()[0]
    overwrite_prediction(charge_container, charge_usd)
