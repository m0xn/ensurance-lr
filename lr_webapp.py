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

st.title('Predicción del importe de un seguro')

st.markdown("""
            ## Introducción
            👋 Bienvenido a la aplicación web interactiva del modelo de **Regresión Lineal**
            para predecir el **importe de tu seguro** 💵 en base a unas características.
            
            ⚠️ :orange[Aviso]: *Tu información no será recolectada por ninguna entidad, sólo será
            utilizada de referencia para los parámetros de la regresión lineal.*
            """)

st.markdown("""
            ## Contexto
            Esta aplicación web tiene como propósito servir de **interfaz interactiva** para
            probar los modelos de **Regresión Lineal** que he entrenado en el [trabajo de IA](https://github.com/iavalle2024/proyecto-eval-1)
            del que proviene esta página.
            """)

st.markdown("""
            ## Información sobre el modelo
            Los modelos entrenados, que podrás utilizar en la página, han sido entrenados a partir de la muestra
            de una base de datos de una empresa de seguros estadounidense. El tamaño de la muestra tomada es de **~$200$ registros**.

            Los parámetros o *features* de estos modelos son:
            - **Edad** -> `age`
            - **IMC** ->  `bmi`
            - **Sexo** -> `sex`
            - **Fumador / No fumador** -> `smoker`
            - **Hijos** -> `children`
            """)

st.markdown("""
            ## Interacción con el modelo
            Ahora que conoces información básica acerca de los modelos entrenados, es hora de que trastees con ellos! 🔧

            Voy a clasificar los modelos por su **rendimiento**. El **rendimiento** en este caso se entiende como el **porcentaje
            de las predicciones** del modelo (*hechas en el proceso de entrenamiento*) que se ajustan a los **valores reales**. 

            Por lo tanto, los modelos disponibles son:
            - **RL Base (Ajustado)**: :green[^78%]
            - **RL Ridge (Ajustado)**: :orange[78%]
            - **Rl Ridge**: :red[^75%]
            - **RL Base**: :grey[75%]
            """)



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

charge_container = st.empty()
charge_container.write("""
            <style>@import url('https://fonts.googleapis.com/css2?family=Quantico&display=swap');</style>
            <p style="font-size: 100px; font-family: 'Quantico', sans-serif; text-align: center; color: #ff0000;">0.00<span style="display: inline-block; font-size: 50px;">€</span></p>
            <p style="font-size: 50px; font-family: 'Quantico', sans-serif; text-align: center; margin-top: -50px; color: #b70603;">0.00<span style="display: inline-block; font-size: 25px;">$</span></p>
            """,
            unsafe_allow_html=True)

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
