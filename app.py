from operator import index
import streamlit as st
import pandas as pd
import os 

st.set_page_config(page_title="Chris Tester", page_icon="🎉", layout="centered", initial_sidebar_state="expanded")

with st.sidebar: 
    st.image("tester.png")
    st.title("Chris Tester")
    choice = st.radio("Navegación", ["Nuevo test","Pregunta 1","Pregunta 2","Pregunta 3","Pregunta 4","Pregunta 5","Pregunta 6","Pregunta 7","Pregunta 8","Pregunta 9","Pregunta 10","Enviar test"])
    st.info("¡Chris evalua sus conocimientos!")

if choice == "Nuevo test":
    st.title("Nuevo test")
    st.write("Este es un test de 10 preguntas. ¡Buena suerte!")
    if st.button("¡Empezar nuevo test!"):
        num_questions = 10
        gsheetid = "1yINIfl1Hl8Ts_DjTq-UaOC6sW83dCSxUwEPlsAA6-1w"
        sheet_name = "banco"
        gsheet_url = "https://docs.google.com/spreadsheets/d/{}/gviz/tq?tqx=out:csv&sheet={}".format(gsheetid, sheet_name)
        df = pd.read_csv(gsheet_url, header=1)
        df.columns = ['categoria_pregunta','enunciado_sin_categoria','enunciado_pregunta','opcion_1','opcion_2','opcion_3','opcion_4','respuesta_correcta']
        
        def get_n_questions(n,df):
            return df.sample(n)
        df_sampled = get_n_questions(num_questions,df)
        # st.dataframe(df_sampled)

        aciertos=[0,0,0,0,0,0,0,0,0,0]
        def write_to_csv(aciertos):
            df = pd.DataFrame(aciertos, columns=['aciertos'])
            df.to_csv('aciertos.csv', mode='a', header=True, index=False)

        if os.path.exists('aciertos.csv'):
            os.remove('aciertos.csv')
        write_to_csv(aciertos)

        respuesta_seleccionada = pd.DataFrame({'respuesta_seleccionada': [''] * 10, 'respuesta_correcta': [''] * 10})
        if os.path.exists('respuesta_seleccionada.csv'):
            os.remove('respuesta_seleccionada.csv')
        respuesta_seleccionada.to_csv('respuesta_seleccionada.csv', mode='a', header=True, index=False)

        for i in range(num_questions):
            df_sampled.iloc[i,3:7] = df_sampled.iloc[i,3:7].sample(frac=1).values
        
        # st.dataframe(df_sampled)
        if os.path.exists('df_sampled.csv'):
            os.remove('df_sampled.csv')
        df_sampled.to_csv("test.csv", index=False)
        st.write("¡Test generado! Ahora puedes empezar a responder las preguntas.")
        st.balloons()
        
if choice == "Pregunta 1":
    df_sampled = pd.read_csv("test.csv")
    aciertos_df = pd.read_csv("aciertos.csv")
    respuesta_seleccionada_df = pd.read_csv("respuesta_seleccionada.csv")

    st.title("Pregunta 1:")
    st.write(df_sampled['enunciado_pregunta'].values[0])
    st.markdown("<hr/>", unsafe_allow_html=True)
    st.write("")
    st.write("")

    q1_options = [df_sampled['opcion_1'].values[0],df_sampled['opcion_2'].values[0],df_sampled['opcion_3'].values[0],df_sampled['opcion_4'].values[0]]
    q1_answer = df_sampled['respuesta_correcta'].values[0]

    st.write("🔹 **A)** " + q1_options[0])
    st.write("🔹 **B)** " + q1_options[1])
    st.write("🔹 **C)** " + q1_options[2])
    st.write("🔹 **D)** " + q1_options[3])

    st.markdown("<hr/>", unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button("A"):
            q1_selection = q1_options[0]
            if q1_selection == q1_answer:
                aciertos_df.iloc[0,0] = 1
                aciertos_df.to_csv("aciertos.csv", index=False)
                respuesta_seleccionada_df.iloc[0,0] = q1_selection
                respuesta_seleccionada_df.iloc[0,1] = q1_answer
                respuesta_seleccionada_df.to_csv("respuesta_seleccionada.csv", index=False)
            else:
                aciertos_df.iloc[0,0] = 0
                aciertos_df.to_csv("aciertos.csv", index=False)
                respuesta_seleccionada_df.iloc[0,0] = q1_selection
                respuesta_seleccionada_df.iloc[0,1] = q1_answer
                respuesta_seleccionada_df.to_csv("respuesta_seleccionada.csv", index=False)
    with col2:
        if st.button("B"):
            q1_selection = q1_options[1]
            if q1_selection == q1_answer:
                aciertos_df.iloc[0,0] = 1
                aciertos_df.to_csv("aciertos.csv", index=False)
                respuesta_seleccionada_df.iloc[0,0] = q1_selection
                respuesta_seleccionada_df.iloc[0,1] = q1_answer
                respuesta_seleccionada_df.to_csv("respuesta_seleccionada.csv", index=False)
            else:
                aciertos_df.iloc[0,0] = 0
                aciertos_df.to_csv("aciertos.csv", index=False)
                respuesta_seleccionada_df.iloc[0,0] = q1_selection
                respuesta_seleccionada_df.iloc[0,1] = q1_answer
                respuesta_seleccionada_df.to_csv("respuesta_seleccionada.csv", index=False)
    with col3:
        if st.button("C"):
            q1_selection = q1_options[2]
            if q1_selection == q1_answer:
                aciertos_df.iloc[0,0] = 1
                aciertos_df.to_csv("aciertos.csv", index=False)
                respuesta_seleccionada_df.iloc[0,0] = q1_selection
                respuesta_seleccionada_df.iloc[0,1] = q1_answer
                respuesta_seleccionada_df.to_csv("respuesta_seleccionada.csv", index=False)
            else:
                aciertos_df.iloc[0,0] = 0
                aciertos_df.to_csv("aciertos.csv", index=False)
                respuesta_seleccionada_df.iloc[0,0] = q1_selection
                respuesta_seleccionada_df.iloc[0,1] = q1_answer
                respuesta_seleccionada_df.to_csv("respuesta_seleccionada.csv", index=False)
    with col4:
        if st.button("D"):
            q1_selection = q1_options[3]
            if q1_selection == q1_answer:
                aciertos_df.iloc[0,0] = 1
                aciertos_df.to_csv("aciertos.csv", index=False)
                respuesta_seleccionada_df.iloc[0,0] = q1_selection
                respuesta_seleccionada_df.iloc[0,1] = q1_answer
                respuesta_seleccionada_df.to_csv("respuesta_seleccionada.csv", index=False)
            else:
                aciertos_df.iloc[0,0] = 0
                aciertos_df.to_csv("aciertos.csv", index=False)
                respuesta_seleccionada_df.iloc[0,0] = q1_selection
                respuesta_seleccionada_df.iloc[0,1] = q1_answer
                respuesta_seleccionada_df.to_csv("respuesta_seleccionada.csv", index=False)

    # st.write("q1_selection: " + str(q1_selection))
    # st.write("q1_answer: " + str(q1_answer))



if choice == "Pregunta 2":
    df_sampled = pd.read_csv("test.csv")
    aciertos_df = pd.read_csv("aciertos.csv")
    respuesta_seleccionada_df = pd.read_csv("respuesta_seleccionada.csv")

    st.title("Pregunta 2")
    st.write(df_sampled['enunciado_pregunta'].values[1])
    st.markdown("<hr/>", unsafe_allow_html=True)
    st.write("")
    st.write("")

    q2_options = [df_sampled['opcion_1'].values[1], df_sampled['opcion_2'].values[1], df_sampled['opcion_3'].values[1], df_sampled['opcion_4'].values[1]]
    q2_answer = df_sampled['respuesta_correcta'].values[1]

    st.write("🔹 **A)** " + q2_options[0])
    st.write("🔹 **B)** " + q2_options[1])
    st.write("🔹 **C)** " + q2_options[2])
    st.write("🔹 **D)** " + q2_options[3])

    st.markdown("<hr/>", unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button("A"):
            q2_selection = q2_options[0]
            if q2_selection == q2_answer:
                aciertos_df.iloc[1,0] = 1
                aciertos_df.to_csv("aciertos.csv", index=False)
                respuesta_seleccionada_df.iloc[1,0] = q2_selection
                respuesta_seleccionada_df.iloc[1,1] = q2_answer
                respuesta_seleccionada_df.to_csv("respuesta_seleccionada.csv", index=False)
            else:
                aciertos_df.iloc[1,0] = 0
                aciertos_df.to_csv("aciertos.csv", index=False)
                respuesta_seleccionada_df.iloc[1,0] = q2_selection
                respuesta_seleccionada_df.iloc[1,1] = q2_answer
                respuesta_seleccionada_df.to_csv("respuesta_seleccionada.csv", index=False)
    with col2:
        if st.button("B"):
            q2_selection = q2_options[1]
            if q2_selection == q2_answer:
                aciertos_df.iloc[1,0] = 1
                aciertos_df.to_csv("aciertos.csv", index=False)
                respuesta_seleccionada_df.iloc[1,0] = q2_selection
                respuesta_seleccionada_df.iloc[1,1] = q2_answer
                respuesta_seleccionada_df.to_csv("respuesta_seleccionada.csv", index=False)
            else:
                aciertos_df.iloc[1,0] = 0
                aciertos_df.to_csv("aciertos.csv", index=False)
                respuesta_seleccionada_df.iloc[1,0] = q2_selection
                respuesta_seleccionada_df.iloc[1,1] = q2_answer
                respuesta_seleccionada_df.to_csv("respuesta_seleccionada.csv", index=False)
    with col3:
        if st.button("C"):
            q2_selection = q2_options[2]
            if q2_selection == q2_answer:
                aciertos_df.iloc[1,0] = 1
                aciertos_df.to_csv("aciertos.csv", index=False)
                respuesta_seleccionada_df.iloc[1,0] = q2_selection
                respuesta_seleccionada_df.iloc[1,1] = q2_answer
                respuesta_seleccionada_df.to_csv("respuesta_seleccionada.csv", index=False)
            else:
                aciertos_df.iloc[1,0] = 0
                aciertos_df.to_csv("aciertos.csv", index=False)
                respuesta_seleccionada_df.iloc[1,0] = q2_selection
                respuesta_seleccionada_df.iloc[1,1] = q2_answer
                respuesta_seleccionada_df.to_csv("respuesta_seleccionada.csv", index=False)
    with col4:
        if st.button("D"):
            q2_selection = q2_options[3]
            if q2_selection == q2_answer:
                aciertos_df.iloc[1,0] = 1
                aciertos_df.to_csv("aciertos.csv", index=False)
                respuesta_seleccionada_df.iloc[1,0] = q2_selection
                respuesta_seleccionada_df.iloc[1,1] = q2_answer
                respuesta_seleccionada_df.to_csv("respuesta_seleccionada.csv", index=False)
            else:
                aciertos_df.iloc[1,0] = 0
                aciertos_df.to_csv("aciertos.csv", index=False)
                respuesta_seleccionada_df.iloc[1,0] = q2_selection
                respuesta_seleccionada_df.iloc[1,1] = q2_answer
                respuesta_seleccionada_df.to_csv("respuesta_seleccionada.csv", index=False)

    # st.write("q2_selection: " + str(q2_selection))
    # st.write("q2_answer: " + str(q2_answer))       


if choice == "Pregunta 3":
    df_sampled = pd.read_csv("test.csv")
    aciertos_df = pd.read_csv("aciertos.csv")
    respuesta_seleccionada_df = pd.read_csv("respuesta_seleccionada.csv")

    st.title("Pregunta 3")
    st.write(df_sampled['enunciado_pregunta'].values[2])
    st.markdown("<hr/>", unsafe_allow_html=True)
    st.write("")
    st.write("")

    q3_options = [df_sampled['opcion_1'].values[2], df_sampled['opcion_2'].values[2], df_sampled['opcion_3'].values[2], df_sampled['opcion_4'].values[2]]
    q3_answer = df_sampled['respuesta_correcta'].values[2]

    st.write("🔹 **A)** " + q3_options[0])
    st.write("🔹 **B)** " + q3_options[1])
    st.write("🔹 **C)** " + q3_options[2])
    st.write("🔹 **D)** " + q3_options[3])

    st.markdown("<hr/>", unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button("A"):
            q3_selection = q3_options[0]
            if q3_selection == q3_answer:
                aciertos_df.iloc[2,0] = 1
                aciertos_df.to_csv("aciertos.csv", index=False)
                respuesta_seleccionada_df.iloc[2,0] = q3_selection
                respuesta_seleccionada_df.iloc[2,1] = q3_answer
                respuesta_seleccionada_df.to_csv("respuesta_seleccionada.csv", index=False)
            else:
                aciertos_df.iloc[2,0] = 0
                aciertos_df.to_csv("aciertos.csv", index=False)
                respuesta_seleccionada_df.iloc[2,0] = q3_selection
                respuesta_seleccionada_df.iloc[2,1] = q3_answer
                respuesta_seleccionada_df.to_csv("respuesta_seleccionada.csv", index=False)
    with col2:
        if st.button("B"):
            q3_selection = q3_options[1]
            if q3_selection == q3_answer:
                aciertos_df.iloc[2,0] = 1
                aciertos_df.to_csv("aciertos.csv", index=False)
                respuesta_seleccionada_df.iloc[2,0] = q3_selection
                respuesta_seleccionada_df.iloc[2,1] = q3_answer
                respuesta_seleccionada_df.to_csv("respuesta_seleccionada.csv", index=False)
            else:
                aciertos_df.iloc[2,0] = 0
                aciertos_df.to_csv("aciertos.csv", index=False)
                respuesta_seleccionada_df.iloc[2,0] = q3_selection
                respuesta_seleccionada_df.iloc[2,1] = q3_answer
                respuesta_seleccionada_df.to_csv("respuesta_seleccionada.csv", index=False)
    with col3:
        if st.button("C"):
            q3_selection = q3_options[2]
            if q3_selection == q3_answer:
                aciertos_df.iloc[2,0] = 1
                aciertos_df.to_csv("aciertos.csv", index=False)
                respuesta_seleccionada_df.iloc[2,0] = q3_selection
                respuesta_seleccionada_df.iloc[2,1] = q3_answer
                respuesta_seleccionada_df.to_csv("respuesta_seleccionada.csv", index=False)
            else:
                aciertos_df.iloc[2,0] = 0
                aciertos_df.to_csv("aciertos.csv", index=False)
                respuesta_seleccionada_df.iloc[2,0] = q3_selection
                respuesta_seleccionada_df.iloc[2,1] = q3_answer
                respuesta_seleccionada_df.to_csv("respuesta_seleccionada.csv", index=False)
    with col4:
        if st.button("D"):
            q3_selection = q3_options[3]
            if q3_selection == q3_answer:
                aciertos_df.iloc[2,0] = 1
                aciertos_df.to_csv("aciertos.csv", index=False)
                respuesta_seleccionada_df.iloc[2,0] = q3_selection
                respuesta_seleccionada_df.iloc[2,1] = q3_answer
                respuesta_seleccionada_df.to_csv("respuesta_seleccionada.csv", index=False)
            else:
                aciertos_df.iloc[2,0] = 0
                aciertos_df.to_csv("aciertos.csv", index=False)
                respuesta_seleccionada_df.iloc[2,0] = q3_selection
                respuesta_seleccionada_df.iloc[2,1] = q3_answer
                respuesta_seleccionada_df.to_csv("respuesta_seleccionada.csv", index=False)

    # st.write("q3_selection: " + str(q3_selection))
    # st.write("q3_answer: " + str(q3_answer)) 


if choice == "Pregunta 4":
    df_sampled = pd.read_csv("test.csv")
    aciertos_df = pd.read_csv("aciertos.csv")
    respuesta_seleccionada_df = pd.read_csv("respuesta_seleccionada.csv")

    st.title("Pregunta 4")
    st.write(df_sampled['enunciado_pregunta'].values[3])
    st.markdown("<hr/>", unsafe_allow_html=True)
    st.write("")
    st.write("")

    q4_options = [df_sampled['opcion_1'].values[3], df_sampled['opcion_2'].values[3], df_sampled['opcion_3'].values[3], df_sampled['opcion_4'].values[3]]
    q4_answer = df_sampled['respuesta_correcta'].values[3]

    st.write("🔹 **A)** " + q4_options[0])
    st.write("🔹 **B)** " + q4_options[1])
    st.write("🔹 **C)** " + q4_options[2])
    st.write("🔹 **D)** " + q4_options[3])

    st.markdown("<hr/>", unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button("A"):
            q4_selection = q4_options[0]
            if q4_selection == q4_answer:
                aciertos_df.iloc[3,0] = 1
                aciertos_df.to_csv("aciertos.csv", index=False)
                respuesta_seleccionada_df.iloc[3,0] = q4_selection
                respuesta_seleccionada_df.iloc[3,1] = q4_answer
                respuesta_seleccionada_df.to_csv("respuesta_seleccionada.csv", index=False)
            else:
                aciertos_df.iloc[3,0] = 0
                aciertos_df.to_csv("aciertos.csv", index=False)
                respuesta_seleccionada_df.iloc[3,0] = q4_selection
                respuesta_seleccionada_df.iloc[3,1] = q4_answer
                respuesta_seleccionada_df.to_csv("respuesta_seleccionada.csv", index=False)
    with col2:
        if st.button("B"):
            q4_selection = q4_options[1]
            if q4_selection == q4_answer:
                aciertos_df.iloc[3,0] = 1
                aciertos_df.to_csv("aciertos.csv", index=False)
                respuesta_seleccionada_df.iloc[3,0] = q4_selection
                respuesta_seleccionada_df.iloc[3,1] = q4_answer
                respuesta_seleccionada_df.to_csv("respuesta_seleccionada.csv", index=False)
            else:
                aciertos_df.iloc[3,0] = 0
                aciertos_df.to_csv("aciertos.csv", index=False)
                respuesta_seleccionada_df.iloc[3,0] = q4_selection
                respuesta_seleccionada_df.iloc[3,1] = q4_answer
                respuesta_seleccionada_df.to_csv("respuesta_seleccionada.csv", index=False)
    with col3:
        if st.button("C"):
            q4_selection = q4_options[2]
            if q4_selection == q4_answer:
                aciertos_df.iloc[3,0] = 1
                aciertos_df.to_csv("aciertos.csv", index=False)
                respuesta_seleccionada_df.iloc[3,0] = q4_selection
                respuesta_seleccionada_df.iloc[3,1] = q4_answer
                respuesta_seleccionada_df.to_csv("respuesta_seleccionada.csv", index=False)
            else:
                aciertos_df.iloc[3,0] = 0
                aciertos_df.to_csv("aciertos.csv", index=False)
                respuesta_seleccionada_df.iloc[3,0] = q4_selection
                respuesta_seleccionada_df.iloc[3,1] = q4_answer
                respuesta_seleccionada_df.to_csv("respuesta_seleccionada.csv", index=False)
    with col4:
        if st.button("D"):
            q4_selection = q4_options[3]
            if q4_selection == q4_answer:
                aciertos_df.iloc[3,0] = 1
                aciertos_df.to_csv("aciertos.csv", index=False)
                respuesta_seleccionada_df.iloc[3,0] = q4_selection
                respuesta_seleccionada_df.iloc[3,1] = q4_answer
                respuesta_seleccionada_df.to_csv("respuesta_seleccionada.csv", index=False)
            else:
                aciertos_df.iloc[3,0] = 0
                aciertos_df.to_csv("aciertos.csv", index=False)
                respuesta_seleccionada_df.iloc[3,0] = q4_selection
                respuesta_seleccionada_df.iloc[3,1] = q4_answer
                respuesta_seleccionada_df.to_csv("respuesta_seleccionada.csv", index=False)

    # st.write("q4_answer: " + str(q4_answer))
    # st.write("q4_selection: " + str(q4_selection))


if choice == "Pregunta 5":
    df_sampled = pd.read_csv("test.csv")
    aciertos_df = pd.read_csv("aciertos.csv")
    respuesta_seleccionada_df = pd.read_csv("respuesta_seleccionada.csv")

    st.title("Pregunta 5")
    st.write(df_sampled['enunciado_pregunta'].values[4])
    st.markdown("<hr/>", unsafe_allow_html=True)
    st.write("")
    st.write("")

    q5_options = [df_sampled['opcion_1'].values[4], df_sampled['opcion_2'].values[4], df_sampled['opcion_3'].values[4], df_sampled['opcion_4'].values[4]]
    q5_answer = df_sampled['respuesta_correcta'].values[4]

    st.write("🔹 **A)** " + q5_options[0])
    st.write("🔹 **B)** " + q5_options[1])
    st.write("🔹 **C)** " + q5_options[2])
    st.write("🔹 **D)** " + q5_options[3])

    st.markdown("<hr/>", unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if st.button("A"):
            q5_selection = q5_options[0]
            if q5_selection == q5_answer:
                aciertos_df.iloc[4,0] = 1
                aciertos_df.to_csv("aciertos.csv", index=False)
                respuesta_seleccionada_df.iloc[4,0] = q5_selection
                respuesta_seleccionada_df.iloc[4,1] = q5_answer
                respuesta_seleccionada_df.to_csv("respuesta_seleccionada.csv", index=False)
            else:
                aciertos_df.iloc[4,0] = 0
                aciertos_df.to_csv("aciertos.csv", index=False)
                respuesta_seleccionada_df.iloc[4,0] = q5_selection
                respuesta_seleccionada_df.iloc[4,1] = q5_answer
                respuesta_seleccionada_df.to_csv("respuesta_seleccionada.csv", index=False)
    with col2:
        if st.button("B"):
            q5_selection = q5_options[1]
            if q5_selection == q5_answer:
                aciertos_df.iloc[4,0] = 1
                aciertos_df.to_csv("aciertos.csv", index=False)
                respuesta_seleccionada_df.iloc[4,0] = q5_selection
                respuesta_seleccionada_df.iloc[4,1] = q5_answer
                respuesta_seleccionada_df.to_csv("respuesta_seleccionada.csv", index=False)
            else:
                aciertos_df.iloc[4,0] = 0
                aciertos_df.to_csv("aciertos.csv", index=False)
                respuesta_seleccionada_df.iloc[4,0] = q5_selection
                respuesta_seleccionada_df.iloc[4,1] = q5_answer
                respuesta_seleccionada_df.to_csv("respuesta_seleccionada.csv", index=False)
    with col3:
        if st.button("C"):
            q5_selection = q5_options[2]
            if q5_selection == q5_answer:
                aciertos_df.iloc[4,0] = 1
                aciertos_df.to_csv("aciertos.csv", index=False)
                respuesta_seleccionada_df.iloc[4,0] = q5_selection
                respuesta_seleccionada_df.iloc[4,1] = q5_answer
                respuesta_seleccionada_df.to_csv("respuesta_seleccionada.csv", index=False)
            else:
                aciertos_df.iloc[4,0] = 0
                aciertos_df.to_csv("aciertos.csv", index=False)
                respuesta_seleccionada_df.iloc[4,0] = q5_selection
                respuesta_seleccionada_df.iloc[4,1] = q5_answer
                respuesta_seleccionada_df.to_csv("respuesta_seleccionada.csv", index=False)
    with col4:
        if st.button("D"):
            q5_selection = q5_options[3]
            if q5_selection == q5_answer:
                aciertos_df.iloc[4,0] = 1
                aciertos_df.to_csv("aciertos.csv", index=False)
                respuesta_seleccionada_df.iloc[4,0] = q5_selection
                respuesta_seleccionada_df.iloc[4,1] = q5_answer
                respuesta_seleccionada_df.to_csv("respuesta_seleccionada.csv", index=False)
            else:
                aciertos_df.iloc[4,0] = 0
                aciertos_df.to_csv("aciertos.csv", index=False)
                respuesta_seleccionada_df.iloc[4,0] = q5_selection
                respuesta_seleccionada_df.iloc[4,1] = q5_answer
                respuesta_seleccionada_df.to_csv("respuesta_seleccionada.csv", index=False)

    # st.write("q5_answer: " + str(q5_answer))
    # st.write("q5_selection: " + str(q5_selection))


if choice == "Pregunta 6":
    df_sampled = pd.read_csv("test.csv")
    aciertos_df = pd.read_csv("aciertos.csv")
    respuesta_seleccionada_df = pd.read_csv("respuesta_seleccionada.csv")

    st.title("Pregunta 6")
    st.write(df_sampled['enunciado_pregunta'].values[5])
    st.markdown("<hr/>", unsafe_allow_html=True)
    st.write("")
    st.write("")

    q6_options = [df_sampled['opcion_1'].values[5], df_sampled['opcion_2'].values[5], df_sampled['opcion_3'].values[5], df_sampled['opcion_4'].values[5]]
    q6_answer = df_sampled['respuesta_correcta'].values[5]

    st.write("🔹 **A)** " + q6_options[0])
    st.write("🔹 **B)** " + q6_options[1])
    st.write("🔹 **C)** " + q6_options[2])
    st.write("🔹 **D)** " + q6_options[3])

    st.markdown("<hr/>", unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if st.button("A"):
            q6_selection = q6_options[0]
            if q6_selection == q6_answer:
                aciertos_df.iloc[5,0] = 1
                aciertos_df.to_csv("aciertos.csv", index=False)
                respuesta_seleccionada_df.iloc[5,0] = q6_selection
                respuesta_seleccionada_df.iloc[5,1] = q6_answer
                respuesta_seleccionada_df.to_csv("respuesta_seleccionada.csv", index=False)
            else:
                aciertos_df.iloc[5,0] = 0
                aciertos_df.to_csv("aciertos.csv", index=False)
                respuesta_seleccionada_df.iloc[5,0] = q6_selection
                respuesta_seleccionada_df.iloc[5,1] = q6_answer
                respuesta_seleccionada_df.to_csv("respuesta_seleccionada.csv", index=False)
    with col2:
        if st.button("B"):
            q6_selection = q6_options[1]
            if q6_selection == q6_answer:
                aciertos_df.iloc[5,0] = 1
                aciertos_df.to_csv("aciertos.csv", index=False)
                respuesta_seleccionada_df.iloc[5,0] = q6_selection
                respuesta_seleccionada_df.iloc[5,1] = q6_answer
                respuesta_seleccionada_df.to_csv("respuesta_seleccionada.csv", index=False)
            else:
                aciertos_df.iloc[5,0] = 0
                aciertos_df.to_csv("aciertos.csv", index=False)
                respuesta_seleccionada_df.iloc[5,0] = q6_selection
                respuesta_seleccionada_df.iloc[5,1] = q6_answer
                respuesta_seleccionada_df.to_csv("respuesta_seleccionada.csv", index=False)
    with col3:
        if st.button("C"):
            q6_selection = q6_options[2]
            if q6_selection == q6_answer:
                aciertos_df.iloc[5,0] = 1
                aciertos_df.to_csv("aciertos.csv", index=False)
                respuesta_seleccionada_df.iloc[5,0] = q6_selection
                respuesta_seleccionada_df.iloc[5,1] = q6_answer
                respuesta_seleccionada_df.to_csv("respuesta_seleccionada.csv", index=False)
            else:
                aciertos_df.iloc[5,0] = 0
                aciertos_df.to_csv("aciertos.csv", index=False)
                respuesta_seleccionada_df.iloc[5,0] = q6_selection
                respuesta_seleccionada_df.iloc[5,1] = q6_answer
                respuesta_seleccionada_df.to_csv("respuesta_seleccionada.csv", index=False)
    with col4:
        if st.button("D"):
            q6_selection = q6_options[3]
            if q6_selection == q6_answer:
                aciertos_df.iloc[5,0] = 1
                aciertos_df.to_csv("aciertos.csv", index=False)
                respuesta_seleccionada_df.iloc[5,0] = q6_selection
                respuesta_seleccionada_df.iloc[5,1] = q6_answer
                respuesta_seleccionada_df.to_csv("respuesta_seleccionada.csv", index=False)
            else:
                aciertos_df.iloc[5,0] = 0
                aciertos_df.to_csv("aciertos.csv", index=False)
                respuesta_seleccionada_df.iloc[5,0] = q6_selection
                respuesta_seleccionada_df.iloc[5,1] = q6_answer
                respuesta_seleccionada_df.to_csv("respuesta_seleccionada.csv", index=False)

    # st.write("q6_answer: " + str(q6_answer))
    # st.write("q6_selection: " + str(q6_selection))


if choice == "Pregunta 7":
    df_sampled = pd.read_csv("test.csv")
    aciertos_df = pd.read_csv("aciertos.csv")
    respuesta_seleccionada_df = pd.read_csv("respuesta_seleccionada.csv")

    st.title("Pregunta 7")
    st.write(df_sampled['enunciado_pregunta'].values[6])
    st.markdown("<hr/>", unsafe_allow_html=True)
    st.write("")
    st.write("")

    q7_options = [df_sampled['opcion_1'].values[6], df_sampled['opcion_2'].values[6], df_sampled['opcion_3'].values[6], df_sampled['opcion_4'].values[6]]
    q7_answer = df_sampled['respuesta_correcta'].values[6]

    st.write("🔹 **A)** " + q7_options[0])
    st.write("🔹 **B)** " + q7_options[1])
    st.write("🔹 **C)** " + q7_options[2])
    st.write("🔹 **D)** " + q7_options[3])

    st.markdown("<hr/>", unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if st.button("A"):
            q7_selection = q7_options[0]
            if q7_selection == q7_answer:
                aciertos_df.iloc[6,0] = 1
                aciertos_df.to_csv("aciertos.csv", index=False)
                respuesta_seleccionada_df.iloc[6,0] = q7_selection
                respuesta_seleccionada_df.iloc[6,1] = q7_answer
                respuesta_seleccionada_df.to_csv("respuesta_seleccionada.csv", index=False)
            else:
                aciertos_df.iloc[6,0] = 0
                aciertos_df.to_csv("aciertos.csv", index=False)
                respuesta_seleccionada_df.iloc[6,0] = q7_selection
                respuesta_seleccionada_df.iloc[6,1] = q7_answer
                respuesta_seleccionada_df.to_csv("respuesta_seleccionada.csv", index=False)
    with col2:
        if st.button("B"):
            q7_selection = q7_options[1]
            if q7_selection == q7_answer:
                aciertos_df.iloc[6,0] = 1
                aciertos_df.to_csv("aciertos.csv", index=False)
                respuesta_seleccionada_df.iloc[6,0] = q7_selection
                respuesta_seleccionada_df.iloc[6,1] = q7_answer
                respuesta_seleccionada_df.to_csv("respuesta_seleccionada.csv", index=False)
            else:
                aciertos_df.iloc[6,0] = 0
                aciertos_df.to_csv("aciertos.csv", index=False)
                respuesta_seleccionada_df.iloc[6,0] = q7_selection
                respuesta_seleccionada_df.iloc[6,1] = q7_answer
                respuesta_seleccionada_df.to_csv("respuesta_seleccionada.csv", index=False)
    with col3:
        if st.button("C"):
            q7_selection = q7_options[2]
            if q7_selection == q7_answer:
                aciertos_df.iloc[6,0] = 1
                aciertos_df.to_csv("aciertos.csv", index=False)
                respuesta_seleccionada_df.iloc[6,0] = q7_selection
                respuesta_seleccionada_df.iloc[6,1] = q7_answer
                respuesta_seleccionada_df.to_csv("respuesta_seleccionada.csv", index=False)
            else:
                aciertos_df.iloc[6,0] = 0
                aciertos_df.to_csv("aciertos.csv", index=False)
                respuesta_seleccionada_df.iloc[6,0] = q7_selection
                respuesta_seleccionada_df.iloc[6,1] = q7_answer
                respuesta_seleccionada_df.to_csv("respuesta_seleccionada.csv", index=False)
    with col4:
        if st.button("D"):
            q7_selection = q7_options[3]
            if q7_selection == q7_answer:
                aciertos_df.iloc[6,0] = 1
                aciertos_df.to_csv("aciertos.csv", index=False)
                respuesta_seleccionada_df.iloc[6,0] = q7_selection
                respuesta_seleccionada_df.iloc[6,1] = q7_answer
                respuesta_seleccionada_df.to_csv("respuesta_seleccionada.csv", index=False)
            else:
                aciertos_df.iloc[6,0] = 0
                aciertos_df.to_csv("aciertos.csv", index=False)
                respuesta_seleccionada_df.iloc[6,0] = q7_selection
                respuesta_seleccionada_df.iloc[6,1] = q7_answer
                respuesta_seleccionada_df.to_csv("respuesta_seleccionada.csv", index=False)

    # st.write("q7_answer: " + str(q7_answer))
    # st.write("q7_selection: " + str(q7_selection))


if choice == "Pregunta 8":
    df_sampled = pd.read_csv("test.csv")
    aciertos_df = pd.read_csv("aciertos.csv")
    respuesta_seleccionada_df = pd.read_csv("respuesta_seleccionada.csv")

    st.title("Pregunta 8")
    st.write(df_sampled['enunciado_pregunta'].values[7])
    st.markdown("<hr/>", unsafe_allow_html=True)
    st.write("")
    st.write("")

    q8_options = [df_sampled['opcion_1'].values[7], df_sampled['opcion_2'].values[7], df_sampled['opcion_3'].values[7], df_sampled['opcion_4'].values[7]]
    q8_answer = df_sampled['respuesta_correcta'].values[7]

    st.write("🔹 **A)** " + q8_options[0])
    st.write("🔹 **B)** " + q8_options[1])
    st.write("🔹 **C)** " + q8_options[2])
    st.write("🔹 **D)** " + q8_options[3])

    st.markdown("<hr/>", unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if st.button("A"):
            q8_selection = q8_options[0]
            if q8_selection == q8_answer:
                aciertos_df.iloc[7,0] = 1
                aciertos_df.to_csv("aciertos.csv", index=False)
                respuesta_seleccionada_df.iloc[7,0] = q8_selection
                respuesta_seleccionada_df.iloc[7,1] = q8_answer
                respuesta_seleccionada_df.to_csv("respuesta_seleccionada.csv", index=False)
            else:
                aciertos_df.iloc[7,0] = 0
                aciertos_df.to_csv("aciertos.csv", index=False)
                respuesta_seleccionada_df.iloc[7,0] = q8_selection
                respuesta_seleccionada_df.iloc[7,1] = q8_answer
                respuesta_seleccionada_df.to_csv("respuesta_seleccionada.csv", index=False)
    with col2:
        if st.button("B"):
            q8_selection = q8_options[1]
            if q8_selection == q8_answer:
                aciertos_df.iloc[7,0] = 1
                aciertos_df.to_csv("aciertos.csv", index=False)
                respuesta_seleccionada_df.iloc[7,0] = q8_selection
                respuesta_seleccionada_df.iloc[7,1] = q8_answer
                respuesta_seleccionada_df.to_csv("respuesta_seleccionada.csv", index=False)
            else:
                aciertos_df.iloc[7,0] = 0
                aciertos_df.to_csv("aciertos.csv", index=False)
                respuesta_seleccionada_df.iloc[7,0] = q8_selection
                respuesta_seleccionada_df.iloc[7,1] = q8_answer
                respuesta_seleccionada_df.to_csv("respuesta_seleccionada.csv", index=False)
    with col3:
        if st.button("C"):
            q8_selection = q8_options[2]
            if q8_selection == q8_answer:
                aciertos_df.iloc[7,0] = 1
                aciertos_df.to_csv("aciertos.csv", index=False)
                respuesta_seleccionada_df.iloc[7,0] = q8_selection
                respuesta_seleccionada_df.iloc[7,1] = q8_answer
                respuesta_seleccionada_df.to_csv("respuesta_seleccionada.csv", index=False)
            else:
                aciertos_df.iloc[7,0] = 0
                aciertos_df.to_csv("aciertos.csv", index=False)
                respuesta_seleccionada_df.iloc[7,0] = q8_selection
                respuesta_seleccionada_df.iloc[7,1] = q8_answer
                respuesta_seleccionada_df.to_csv("respuesta_seleccionada.csv", index=False)
    with col4:
        if st.button("D"):
            q8_selection = q8_options[3]
            if q8_selection == q8_answer:
                aciertos_df.iloc[7,0] = 1
                aciertos_df.to_csv("aciertos.csv", index=False)
                respuesta_seleccionada_df.iloc[7,0] = q8_selection
                respuesta_seleccionada_df.iloc[7,1] = q8_answer
                respuesta_seleccionada_df.to_csv("respuesta_seleccionada.csv", index=False)
            else:
                aciertos_df.iloc[7,0] = 0
                aciertos_df.to_csv("aciertos.csv", index=False)
                respuesta_seleccionada_df.iloc[7,0] = q8_selection
                respuesta_seleccionada_df.iloc[7,1] = q8_answer
                respuesta_seleccionada_df.to_csv("respuesta_seleccionada.csv", index=False)

    # st.write("q8_answer: " + str(q8_answer))
    # st.write("q8_selection: " + str(q8_selection))


if choice == "Pregunta 9":
    df_sampled = pd.read_csv("test.csv")
    aciertos_df = pd.read_csv("aciertos.csv")
    respuesta_seleccionada_df = pd.read_csv("respuesta_seleccionada.csv")

    st.title("Pregunta 9")
    st.write(df_sampled['enunciado_pregunta'].values[8])
    st.markdown("<hr/>", unsafe_allow_html=True)
    st.write("")
    st.write("")

    q9_options = [df_sampled['opcion_1'].values[8], df_sampled['opcion_2'].values[8], df_sampled['opcion_3'].values[8], df_sampled['opcion_4'].values[8]]
    q9_answer = df_sampled['respuesta_correcta'].values[8]

    st.write("🔹 **A)** " + q9_options[0])
    st.write("🔹 **B)** " + q9_options[1])
    st.write("🔹 **C)** " + q9_options[2])
    st.write("🔹 **D)** " + q9_options[3])

    st.markdown("<hr/>", unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if st.button("A"):
            q9_selection = q9_options[0]
            if q9_selection == q9_answer:
                aciertos_df.iloc[8,0] = 1
                aciertos_df.to_csv("aciertos.csv", index=False)
                respuesta_seleccionada_df.iloc[8,0] = q9_selection
                respuesta_seleccionada_df.iloc[8,1] = q9_answer
                respuesta_seleccionada_df.to_csv("respuesta_seleccionada.csv", index=False)
            else:
                aciertos_df.iloc[8,0] = 0
                aciertos_df.to_csv("aciertos.csv", index=False)
                respuesta_seleccionada_df.iloc[8,0] = q9_selection
                respuesta_seleccionada_df.iloc[8,1] = q9_answer
                respuesta_seleccionada_df.to_csv("respuesta_seleccionada.csv", index=False)
    with col2:
        if st.button("B"):
            q9_selection = q9_options[1]
            if q9_selection == q9_answer:
                aciertos_df.iloc[8,0] = 1
                aciertos_df.to_csv("aciertos.csv", index=False)
                respuesta_seleccionada_df.iloc[8,0] = q9_selection
                respuesta_seleccionada_df.iloc[8,1] = q9_answer
                respuesta_seleccionada_df.to_csv("respuesta_seleccionada.csv", index=False)
            else:
                aciertos_df.iloc[8,0] = 0
                aciertos_df.to_csv("aciertos.csv", index=False)
                respuesta_seleccionada_df.iloc[8,0] = q9_selection
                respuesta_seleccionada_df.iloc[8,1] = q9_answer
                respuesta_seleccionada_df.to_csv("respuesta_seleccionada.csv", index=False)
    with col3:
        if st.button("C"):
            q9_selection = q9_options[2]
            if q9_selection == q9_answer:
                aciertos_df.iloc[8,0] = 1
                aciertos_df.to_csv("aciertos.csv", index=False)
                respuesta_seleccionada_df.iloc[8,0] = q9_selection
                respuesta_seleccionada_df.iloc[8,1] = q9_answer
                respuesta_seleccionada_df.to_csv("respuesta_seleccionada.csv", index=False)
            else:
                aciertos_df.iloc[8,0] = 0
                aciertos_df.to_csv("aciertos.csv", index=False)
                respuesta_seleccionada_df.iloc[8,0] = q9_selection
                respuesta_seleccionada_df.iloc[8,1] = q9_answer
                respuesta_seleccionada_df.to_csv("respuesta_seleccionada.csv", index=False)
    with col4:
        if st.button("D"):
            q9_selection = q9_options[3]
            if q9_selection == q9_answer:
                aciertos_df.iloc[8,0] = 1
                aciertos_df.to_csv("aciertos.csv", index=False)
                respuesta_seleccionada_df.iloc[8,0] = q9_selection
                respuesta_seleccionada_df.iloc[8,1] = q9_answer
                respuesta_seleccionada_df.to_csv("respuesta_seleccionada.csv", index=False)
            else:
                aciertos_df.iloc[8,0] = 0
                aciertos_df.to_csv("aciertos.csv", index=False)
                respuesta_seleccionada_df.iloc[8,0] = q9_selection
                respuesta_seleccionada_df.iloc[8,1] = q9_answer
                respuesta_seleccionada_df.to_csv("respuesta_seleccionada.csv", index=False)

    # st.write("q9_answer: " + str(q9_answer))
    # st.write("q9_selection: " + str(q9_selection))

    
if choice == "Pregunta 10":
    df_sampled = pd.read_csv("test.csv")
    aciertos_df = pd.read_csv("aciertos.csv")
    respuesta_seleccionada_df = pd.read_csv("respuesta_seleccionada.csv")

    st.title("Pregunta 10")
    st.write(df_sampled['enunciado_pregunta'].values[9])
    st.markdown("<hr/>", unsafe_allow_html=True)
    st.write("")
    st.write("")

    q10_options = [df_sampled['opcion_1'].values[9], df_sampled['opcion_2'].values[9], df_sampled['opcion_3'].values[9], df_sampled['opcion_4'].values[9]]
    q10_answer = df_sampled['respuesta_correcta'].values[9]

    st.write("🔹 **A)** " + q10_options[0])
    st.write("🔹 **B)** " + q10_options[1])
    st.write("🔹 **C)** " + q10_options[2])
    st.write("🔹 **D)** " + q10_options[3])

    st.markdown("<hr/>", unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if st.button("A"):
            q10_selection = q10_options[0]
            if q10_selection == q10_answer:
                aciertos_df.iloc[9,0] = 1
                aciertos_df.to_csv("aciertos.csv", index=False)
                respuesta_seleccionada_df.iloc[9,0] = q10_selection
                respuesta_seleccionada_df.iloc[9,1] = q10_answer
                respuesta_seleccionada_df.to_csv("respuesta_seleccionada.csv", index=False)
            else:
                aciertos_df.iloc[9,0] = 0
                aciertos_df.to_csv("aciertos.csv", index=False)
                respuesta_seleccionada_df.iloc[9,0] = q10_selection
                respuesta_seleccionada_df.iloc[9,1] = q10_answer
                respuesta_seleccionada_df.to_csv("respuesta_seleccionada.csv", index=False)
    with col2:
        if st.button("B"):
            q10_selection = q10_options[1]
            if q10_selection == q10_answer:
                aciertos_df.iloc[9,0] = 1
                aciertos_df.to_csv("aciertos.csv", index=False)
                respuesta_seleccionada_df.iloc[9,0] = q10_selection
                respuesta_seleccionada_df.iloc[9,1] = q10_answer
                respuesta_seleccionada_df.to_csv("respuesta_seleccionada.csv", index=False)
            else:
                aciertos_df.iloc[9,0] = 0
                aciertos_df.to_csv("aciertos.csv", index=False)
                respuesta_seleccionada_df.iloc[9,0] = q10_selection
                respuesta_seleccionada_df.iloc[9,1] = q10_answer
                respuesta_seleccionada_df.to_csv("respuesta_seleccionada.csv", index=False)
    with col3:
        if st.button("C"):
            q10_selection = q10_options[2]
            if q10_selection == q10_answer:
                aciertos_df.iloc[9,0] = 1
                aciertos_df.to_csv("aciertos.csv", index=False)
                respuesta_seleccionada_df.iloc[9,0] = q10_selection
                respuesta_seleccionada_df.iloc[9,1] = q10_answer
                respuesta_seleccionada_df.to_csv("respuesta_seleccionada.csv", index=False)
            else:
                aciertos_df.iloc[9,0] = 0
                aciertos_df.to_csv("aciertos.csv", index=False)
                respuesta_seleccionada_df.iloc[9,0] = q10_selection
                respuesta_seleccionada_df.iloc[9,1] = q10_answer
                respuesta_seleccionada_df.to_csv("respuesta_seleccionada.csv", index=False)
    with col4:
        if st.button("D"):
            q10_selection = q10_options[3]
            if q10_selection == q10_answer:
                aciertos_df.iloc[9,0] = 1
                aciertos_df.to_csv("aciertos.csv", index=False)
                respuesta_seleccionada_df.iloc[9,0] = q10_selection
                respuesta_seleccionada_df.iloc[9,1] = q10_answer
                respuesta_seleccionada_df.to_csv("respuesta_seleccionada.csv", index=False)
            else:
                aciertos_df.iloc[9,0] = 0
                aciertos_df.to_csv("aciertos.csv", index=False)
                respuesta_seleccionada_df.iloc[9,0] = q10_selection
                respuesta_seleccionada_df.iloc[9,1] = q10_answer
                respuesta_seleccionada_df.to_csv("respuesta_seleccionada.csv", index=False)

    # st.write("q10_answer: " + str(q10_answer))
    # st.write("q10_selection: " + str(q10_selection))


if choice == "Enviar test":
    st.title("Enviar test")
    if st.button("Enviar test"):
        st.write("")
        st.write("")

        aciertos_df = pd.read_csv("aciertos.csv")
        aciertos = aciertos_df['aciertos'].sum()
        total = aciertos_df['aciertos'].count()

        if aciertos >= 7:
            st.balloons()
            st.image("win.png", width=200)
            st.success("💪💪 ¡Enhorabuena! Has aprobado el test con " + str(aciertos) + " aciertos de " + str(total) + ". 🥳🤠😎")
        else:
            st.image("lost.png", width=200)
            st.error("😶 Lo siento, has suspendido el test con " + str(aciertos) + " aciertos de " + str(total) + ". 😓")
        st.write("")
        st.write("")

        st.write("📝 Aquí tienes el detalle de tus respuestas:")
        st.write("")

        respuesta_seleccionada_df = pd.read_csv("respuesta_seleccionada.csv")
        respuesta_seleccionada_df = respuesta_seleccionada_df.rename(columns={"respuesta_seleccionada": "Tu respuesta", "respuesta_correcta": "Respuesta correcta"})

        test_df = pd.read_csv("test.csv")
        respuesta_seleccionada_df = test_df['enunciado_pregunta'].to_frame().join(respuesta_seleccionada_df)
        st.dataframe(respuesta_seleccionada_df)
