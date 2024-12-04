import streamlit as st
import random
import time

# Equipos de los bombos confirmados
bombo_1 = ["Manchester City", "Real Madrid", "Bayern Munich", "Paris Saint Germen", "Flamengo", "Palmeiras", "River Plate", "Fluminense"]
bombo_2 = ["Chelsea", "Borussia Dortmund", "Inter Milan", "Porto", "Atletico Madrid", "Benfica", "Juventus", "Salzburgo"]
bombo_3 = ["Al Hilal", "Ulsan", "Al Ahly", "Wydad", "Monterrey", "Club Leon", "Boca Juniors", "Botafogo"]
bombo_4 = ["Urawa", "Al Ain", "Esperance Tunisie", "Mamelodi Sundowns", "Pachuca", "Seattle Sounders", "Auckland City", "Inter Miami"]

# Número de grupos que tengo que formar
num_grupos = 8

# Función para generar los grupos
def generar_grupos(bombo_1, bombo_2, bombo_3, bombo_4, num_grupos):
    random.shuffle(bombo_1)
    random.shuffle(bombo_2)
    random.shuffle(bombo_3)
    random.shuffle(bombo_4)

    grupos = []
    for i in range(num_grupos):
        grupo = {
            "Grupo": f"Grupo {chr(65 + i)}",
            "Equipos": [bombo_1[i], bombo_2[i], bombo_3[i], bombo_4[i]],
        }
        grupos.append(grupo)
    return grupos

# Streamlit App
st.image("https://media.ambito.com/p/9fab8c02179a45b125ec7955602799b8/adjuntos/239/imagenes/040/425/0040425725/mundial-clubes-copajpg.jpg", use_column_width=True, caption="Mundial de Clubes")
st.title("Generador de Grupos de Equipos")
st.write("Selecciona tu equipo favorito y descubre en qué grupo queda.")

# Crear lista combinada de equipos
equipos_todos = bombo_1 + bombo_2 + bombo_3 + bombo_4

equipo_favorito = st.selectbox("Elige tu equipo favorito:", equipos_todos)

if st.button("Generar Grupos"):
    # Generar los grupos
    grupos = generar_grupos(bombo_1, bombo_2, bombo_3, bombo_4, num_grupos)

    # Encontrar el grupo del equipo favorito
    grupo_favorito = None
    for grupo in grupos:
        if equipo_favorito in grupo["Equipos"]:
            grupo_favorito = grupo
            break

    # Informar al usuario dónde quedó su equipo favorito
    if grupo_favorito:
        st.subheader("¡Tu equipo favorito fue ubicado!")
        st.write(f"El equipo **{equipo_favorito}** está en el **{grupo_favorito['Grupo']}**.")

        # Agregar una animación con barra de progreso
        with st.spinner("Asignando equipos a los grupos..."):
            time.sleep(2)

    # Mostrar los grupos
    st.subheader("Grupos Generados")
    for grupo in grupos:
        if grupo == grupo_favorito:
            st.markdown(f"**:blue[{grupo['Grupo']}]**")
        else:
            st.markdown(f"**{grupo['Grupo']}**")

        for equipo in grupo["Equipos"]:
            if equipo == equipo_favorito:
                st.markdown(f"- **:green[{equipo}]**")
            else:
                st.markdown(f"- {equipo}")
