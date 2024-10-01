import streamlit as st

def sidebarPage():
    data = st.session_state["localVars"]["data"]
    language = st.session_state["localVars"]["language"]
    languages = st.session_state["lists"]["languages"]
    abbreviate = st.session_state["dicts"]["abbreviate"]
    _data = st.session_state["dicts"]["_data"]

    st.header(f'⚙️**{data["settings"]}**')
    language = st.selectbox(
        f'**{data["selectLanguage"]}**',
        languages,
        index=languages.index(language),
        placeholder="Select language: "
    )
    data = _data[abbreviate[language]]

    cols = st.columns(
        [.2, .2, .6],
        gap="small",
        vertical_alignment="center"
    )
    with cols[0]:
        st.page_link("home.py", label="Home", icon=None)
    with cols[1]:
        st.page_link("pages/promptEdition.py", label="Edit", icon=None)

    return data, language
