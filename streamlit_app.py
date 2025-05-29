import streamlit as st
import openai

client = openai.OpenAI(api_key=st.secrets["openai"]["api_key"])

def analyser_annonce(description):
    prompt = f"""
    Voici une annonce de voiture d'occasion :
    Description : {description}

    Est-ce une bonne affaire ? Donne un score d'opportunité sur 100 et explique pourquoi.
    """

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Erreur : {str(e)}"

st.set_page_config(page_title="Analyse Auto IA", layout="centered")
st.title("🚗 Analyse d'Annonce Auto par IA")

st.write("📱 Colle ici la description d'une annonce automobile pour savoir si c'est une bonne affaire.")

description = st.text_area("Description de l'annonce", height=200, placeholder="Ex : Clio IV, 2017, 104 000 km, très bon état...")

if st.button("Analyser avec l'IA"):
    if description.strip():
        st.info("Analyse en cours avec ChatGPT...")
        resultat = analyser_annonce(description)
        st.success("Résultat de l'IA :")
        st.markdown(f"""
        <div style='padding:10px; background-color:#f9f9f9; border-left:5px solid #4CAF50;'>
        {resultat}
        </div>
        """, unsafe_allow_html=True)
    else:
        st.warning("Merci de coller une description d'annonce.")
