import streamlit as st
import streamlit.components.v1 as components

from functions import cssStyles

# =========
# CSS Style
# =========
# Custom CSS to remove button borders
st.markdown(
    f'''
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
    <style>
    {cssStyles()}
    </style>
    ''',
    unsafe_allow_html=True
)

# ==============
# Page Info Data
# ==============
# Common GPT personas and prompts
gpt_personas = {
    "Life Coach": "You are a life coach specializing in helping people with stress management.",
    "Tech Support": "You are a tech support specialist helping users troubleshoot their devices.",
    "Travel Guide": "You are a travel guide providing recommendations for tourists.",
    "Fitness Coach": "You are a fitness coach providing workout plans and nutrition advice."
}

gpt_prompts = {
    "Short": "Provide a brief summary.",
    "Medium": "Give a detailed explanation.",
    "Long": "Write an in-depth analysis."
}

# =======
# Sidebar
# =======
# Sidebar for GPT settings
st.sidebar.title("Settings")
st.sidebar.header("GPT Properties")

with st.sidebar:
    st.markdown('<button class="icon-button"><i class="fas fa-cog"></i> GPT Properties</button>', unsafe_allow_html=True)
    # Example GPT properties
    gpt_temperature = st.slider("Temperature", 0.0, 1.0, 0.5)
    gpt_max_tokens = st.number_input("Max Tokens", min_value=1, max_value=5000, value=150)
    api_key = st.text_input("API Key")
    gpt_model = st.selectbox("GPT Model", ["GPT-3", "GPT-4", "GPT-3.5"])

    gpt_persona = st.selectbox("GPT Persona", list(gpt_personas.keys()))
    gpt_prompt = st.selectbox("GPT Prompt", list(gpt_prompts.keys()))

    # Add a space
    st.write("")

    # Page buttons
    btnProperties = st.button("GPT Properties")
    btnPersona = st.button("GPT Persona")
    btnPrompt = st.button("GPT Prompt")

# =============
# Pages Content
# =============
# Function to render each page
def gpt_properties_page():
    import streamlit as st
    import matplotlib.pyplot as plt
    import numpy as np

    # Custom CSS to style the dashboard
    st.markdown("""
        <style>
        .dashboard {
            background-color: #f5f5f5;
            padding: 20px;
            border-radius: 10px;
        }
        .title {
            font-size: 24px;
            font-weight: bold;
            color: #333;
        }
        .section {
            margin-bottom: 20px;
        }
        .section-title {
            font-size: 20px;
            font-weight: bold;
            color: #666;
            margin-bottom: 10px;
        }
        .parameter {
            font-size: 18px;
            color: #444;
        }
        </style>
        """, unsafe_allow_html=True)

    # Example data for charts
    data = np.random.randn(100)

    # Dashboard layout
    st.markdown('<div class="dashboard">', unsafe_allow_html=True)
    st.markdown('<div class="title">GPT Settings Dashboard</div>', unsafe_allow_html=True)

    # GPT Properties Section
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">GPT Properties</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="parameter">Temperature: {gpt_temperature}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="parameter">Max Tokens: {gpt_max_tokens}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Add a histogram to visualize temperature distribution
    fig, ax = plt.subplots()
    ax.hist(data, bins=20, color='skyblue', edgecolor='black')
    ax.set_title("Temperature Distribution")
    ax.set_xlabel("Temperature")
    ax.set_ylabel("Frequency")
    st.pyplot(fig)

    # API Key Section
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">API Key</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="parameter">{api_key}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # GPT Model Section
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">GPT Model</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="parameter">{gpt_model}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Add a bar chart for model usage distribution
    model_usage = {"GPT-3": 40, "GPT-4": 35, "GPT-3.5": 25}
    models = list(model_usage.keys())
    usage = list(model_usage.values())

    fig, ax = plt.subplots()
    ax.bar(models, usage, color='lightgreen')
    ax.set_title("Model Usage Distribution")
    ax.set_xlabel("GPT Model")
    ax.set_ylabel("Usage (%)")
    st.pyplot(fig)

    # GPT Persona Section
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">GPT Persona</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="parameter">{gpt_persona}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # GPT Prompt Section
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">GPT Prompt</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="parameter">{gpt_prompt}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    components.html(open("component.html").read(), height=200)

    # JavaScript event listener in Streamlit to show toast
    st.js_event("show-toast", lambda e: st.toast(e.detail))

def program1_page():
    st.title("Program 1")
    st.write("Content for Program 1.")

def program2_page():
    st.title("Program 2")
    st.write("Content for Program 2.")

# ===========
# Page design
# ===========
# Page navigation with buttons
if btnProperties:
    gpt_properties_page()
elif btnPersona:
    program1_page()
elif btnPrompt:
    program2_page()