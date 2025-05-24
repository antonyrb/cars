# Importar librerías
import streamlit as st
import pickle
import pandas as pd
import base64
import sklearn

# Configuración de la página (debe ser la primera instrucción)
############################################################################################################################

st.set_page_config(page_title="Clasificador diferencial del Dengue, Zika y Chikungunya", layout="centered")
    # Título principal centrado
# Función para cargar imágenes locales como base64
def load_image_as_base64(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# Convertir imagen a base64
<<<<<<< HEAD
image_base64 = load_image_as_base64("Logocarro.jpg")
=======
image_base64 = load_image_as_base64("logocarro.jpg")
>>>>>>> 6403aef69988218fe26efbebd386aea5092a9c64

# HTML con la imagen convertida
st.markdown(
    f"""
    <style>
    .top-right {{
        position: absolute;
        top: 10px;
        right: 10px;
    }}
    </style>
    <div class="top-right">
        <img src="data:image/png;base64,{image_base64}" alt="Logo" width="150">
    </div>
    """,
    unsafe_allow_html=True
)



############################################################################################################################


# Cargar el modelo
filename = 'modelo-clas-tree-knn-nn.pkl'
modelTree, modelKnn, modelNN, labelencoder, variables, min_max_scaler = pickle.load(open(filename, 'rb'))

# Función para clasificar el riesgo
def clasify(clas):
    return 'Alto Riesgo' if clas == 'high' else 'Bajo Riesgo'

# Configuración de la página

def main():
    
    # Título principal
    st.title("Clasificador CarrRisk")
    #Titulo de Sidebar
    st.sidebar.header('Parametros del Ususario')

 # Entradas del usuario

 # Entradas del usuario en el Sidebar

    def user_input_features():
        # Edad como valor entero , entre 0 y 60 años)
        edad = st.sidebar.slider('age', min_value=18, max_value=60, value=25, step=1)  # step=1 garantiza que se seleccionen valores enteros
        # Seleccionar el tipo de vehículo
        option = ['combi', 'sport', 'family', 'minivan']
        Cartype = st.sidebar.selectbox('Seleccione el tipo de vehiculo', option)
    
        data = {
            'age': edad,
            'cartype': Cartype
        }
        features = pd.DataFrame(data, index=[0])
        
    # Verificar que el diccionario esté correctamente pasando los valores
        #st.write("Datos de entrada en el diccionario:", data)
        #st.write("Datos del DataFrame 'features':", features)
    
    
        # Preparar los datos

        data_preparada = features.copy()
        #st.write("copia de feacure: ", data_preparada)
        
        # Crear las variables dummies para la columna 'cartype'
        data_preparada = pd.get_dummies(data_preparada, columns=['cartype'], drop_first=False)
        
        # Se añaden las columnas faltantes en este caso si falta alguna dummy, se creará y se llenará con ceros
        data_preparada = data_preparada.reindex(columns=variables, fill_value=0)

    # Verificar las columnas generadas y los datos de entrada
        #st.write("Columnas del modelo: ", variables)
        #st.write("Columnas generadas en los datos de entrada: ", data_preparada.columns)
        #st.write("Datos de entrada para la predicción: ", data_preparada)

        return data_preparada

    # Llamada a la función
    df = user_input_features()  # permite ver en el front el sidebar

    #Selección del modelo
        # Seleccionar el modelo 
    option = ['DT', 'Knn','NN']
    model = st.sidebar.selectbox('Modelo?',option)

    st.subheader('Valores seleccionados')
    st.write(df)
    st.subheader(f'Modelo Seleccionado: {model}')


    # Crear un botón para realizar la predicción
    if st.button('Realizar Predicción'):
        
        if model == 'DT':
            Y_fut = modelTree.predict(df)
            resultado = labelencoder.inverse_transform(Y_fut)
            st.success(f'La predicción es: {clasify(resultado[0])}')
        elif model == 'Knn':
            #Normalización
            df[['age']] = min_max_scaler.transform(df[['age']])
            Y_fut = modelKnn.predict(df)
            resultado = labelencoder.inverse_transform(Y_fut)
            st.success(f'La predicción es: {clasify(resultado[0])}')
        else:
            #Normalización
            df[['age']] = min_max_scaler.transform(df[['age']])
            Y_fut = modelNN.predict(df)
            resultado = labelencoder.inverse_transform(Y_fut)
            st.success(f'La predicción es: {clasify(resultado[0])}')


    

    # Hacer la predicción utilizando el modelo cargado
    #Y_fut = modelTree.predict(df)
    
    # Mostrar la predicción
    #resultado = labelencoder.inverse_transform(Y_fut)
    #st.success(f'La predicción es: {clasify(resultado[0])}')
    #st.write("Columnas del modelo: ", variables)
    #st.write("Datos de entrada para la predicción: ", df)
    #st.write("Predicción cruda: ", Y_fut)
    

if __name__ == '__main__':
    main()
