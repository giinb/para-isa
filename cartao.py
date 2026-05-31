import streamlit as st

# Configuração da página (Ícone de coração e título na aba do navegador)
st.set_page_config(page_title="Com amor para Isa ❤️", page_icon="💝", layout="centered")

# Cores de fundo (Deixei um tom bem suave e acolhedor)
st.markdown("""
    <style>
    .stApp {
        background-color: #FFF5F5;
    }
    h1 {
        color: #C08081;
        text-align: center;
        font-family: 'Arial';
    }
    p {
        font-size: 18px;
        text-align: center;
        color: #4A4A4A;
    }
    </style>
""", unsafe_allow_html=True)

# ---- INSIRA SEU TEXTO ABAIXO ----

# Título principal da página
st.title("Para você lembrar todos os dias... ✨")

# Um espaço em branco para não ficar colado
st.write("")

# Sua frase ou mensagem principal
st.write("O tempo e ninguém apagará o que foi vivido, te amei do ínicio ao fim.")
st.write("Sei que os últimos tempos não têm sido fáceis e que algumas cargas parecem pesadas demais, mas eu queria que você abrisse esse link para lembrar que você não precisa carregar tudo sozinha. Nossa parceria e nossa história são gigantes, e eu tenho muito orgulho da sua força. Estou aqui com você em cada segundo, nos dias bons e nos dias difíceis. Sempre juntas.")

st.write("---") # Linha bonita para separar os assuntos

# O botão mágico
st.write("Tenho um abraço guardado para você bem aqui:")
if st.button("💖 CLIQUE AQUI PARA RECEBER 💖"):
    st.balloons() # Os balões lindos continuam voando!
    
    # Mensagem de sucesso que aparece logo após o clique
    st.success("### independente de tudo, conta comigo. 🥰")
    
    # Imagem ou GIF (Você pode manter esse de abraço ou colocar outro depois)
    st.image ("https://tse1.explicit.bing.net/th/id/OIP.gUUN1Jlr1_OCqznaC60MPwHaFC?rs=1&pid=ImgDetMain&o=7&rm=3")
