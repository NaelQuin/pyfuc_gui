import streamlit as st
from streamlit_extras.grid import grid
from pyidebug import debug

_data = {
    'PT-PT': {
        'title': "Pyfuc - Gerador de Ficha de Unidade Curricular",
        'description': "Este aplicativo gera uma ficha de unidade curricular com base nas suas entradas. Por favor, preencha os campos obrigatórios abaixo. O aplicativo utiliza o modelo OpenAI GPT-3.5-turbo para gerar a ficha de unidade curricular. Você também pode definir a persona do modelo GPT para combinar com o tom da ficha de unidade curricular. O aplicativo permite que você personalize o prompt para o modelo GPT gerar a ficha de unidade curricular.",
        'api': "Insira a sua chave da API do GPT:",
        'gptModel': "Selecione o modelo GPT:",
        'persona': "Defina a persona do GPT:",
        'prompt_default': "Insira seu prompt aqui...",
        'prompt': "Insira o prompt:",
    },
    'EN-GB': {
        'title': "Pyfuc - Course Unit Sheet Generator",
        'description': "This app generates a course unit sheet based on your input. Please fill in the required fields below. The app uses the OpenAI GPT-3.5-turbo model to generate the course unit sheet. You can also set the persona of the GPT model to match the tone of the course unit sheet. Additionally, the app allows you to customize the prompt for the GPT model to generate the course unit sheet.",
        'api': "Enter your GPT API Key:",
        'gptModel': "Select GPT Model:",
        'persona': "Set the GPT persona:",
        'prompt_default': "Enter your prompt here...",
        'prompt': "Enter prompt:",
    }
}

def setLanguage():
    
    return None

def style_button_row(clicked_button_ix, n_buttons):
    def get_button_indices(button_ix):
        return {
            'nth_child': button_ix,
            'nth_last_child': n_buttons - button_ix + 1
        }

    clicked_style = """
    div[data-testid*="stHorizontalBlock"] 
        > div:nth-child(%(nth_child)s):
            nth-last-child(%(nth_last_child)s) button {
                border-color: rgb(255, 125, 125);
                color: rgb(255, 125, 125);
                box-shadow: rgba(255, 75, 75, 0.5) 0px 0px 0px 0.2rem;
                outline: currentcolor none medium;
            }
    """
    unclicked_style = """
    div[data-testid*="stHorizontalBlock"]
        > div:nth-child(%(nth_child)s):
            nth-last-child(%(nth_last_child)s) button {
                pointer-events: none;
                cursor: not-allowed;
                opacity: 0.2;
                filter: alpha(opacity=65);
                -webkit-box-shadow: none;
                box-shadow: none;
            }
    """
    style = ""
    for ix in range(n_buttons):
        ix += 1
        if ix == clicked_button_ix:
            style += clicked_style % get_button_indices(ix)
        else:
            style += unclicked_style % get_button_indices(ix)
    st.markdown(f"<style>{style}</style>", unsafe_allow_html=True)

def addElement(element, key):
    st.session_state.elements[key] = element
    return element

def getElement(key):
    return st.session_state.elements[key]

def delElement(key):
    #st.session_state.trash[key] = st.session_state.elements.pop(key)

    del(st.session_state.elements[key])
    #print(st.session_state.trash)
    return None

def main():

    st.session_state.elements = {}
    st.session_state.trash = {}

    # col1, col2, col3, col4 = st.sidebar.columns([1, 1, 1, 1])
    # with col1:
    #     st.button("📆", on_click=style_button_row, kwargs={
    #         'clicked_button_ix': 1, 'n_buttons': 4
    #     })
    # with col2:
    #     st.button("👌", on_click=style_button_row, kwargs={
    #         'clicked_button_ix': 2, 'n_buttons': 4
    #     })

    st.session_state.lang = "en"
    data = _data['EN-GB']

    with st.sidebar:
        addElement(
            st.header("Select language:"),
            "header"
        )
        col1, col2, col3, col4 = st.sidebar.columns([1, 1, 1, 1])
        with col1:
            buttonEN = addElement(
                st.button(
                    "EN",
                    on_click=setLanguage,
                    key="langButtonEN"
                ),
                "buttonEN"
            )
        with col2:
            buttonPT = addElement(
                st.button(
                    "PT",
                    on_click=setLanguage,
                    key="langButtonPT"
                ),
                "buttonPT"
            )
        if buttonEN:
            st.session_state.lang = "en"
            data = _data['EN-GB']
            delElement("buttonEN")
        if buttonPT:
            st.session_state.lang = "pt"
            data = _data['PT-PT']
            delElement("buttonPT")

    st.title(data['title'])

    st.write(data['description'])

    # Text entry for GPT API key
    api_key = st.text_input(data["api"])

    # Dropdown for GPT models
    gpt_models = [
        "gpt-3.5-turbo",
        "gpt-4o",
        "gpt-4"
    ]
    selected_model = st.selectbox(data["gptModel"], gpt_models)

    # Persona and prompt entry
    persona = st.text_input(data["persona"])
    prompt = st.text_area(data["prompt"], data["prompt_default"])

    # Submit button
    if st.button("Generate Response"):
        # Call GPT model with provided inputs (use your API integration)
        generated_response = generate_gpt_response(
            api_key, selected_model,
            persona, prompt
            )
        st.write("Generated Response:")
        st.write(generated_response)

def generate_gpt_response(api_key, model, persona, prompt):
    # Implement your GPT interaction logic here
    # Example: Use OpenAI API or any other library to generate response
    # Replace this placeholder with actual code
    return "This is a sample generated response."

if __name__ == "__main__":
    main()
