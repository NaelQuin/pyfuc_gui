import streamlit as st

from data import defaultData

def sidebarPage():

    try:
        settingsIcon = st.session_state["icons"]["settings"]
        languages = st.session_state["lists"]["languages"]
        _data = st.session_state["dicts"]["_data"]
        abbreviate = st.session_state["dicts"]["abbreviate"]
    except Exception as err:
        st.session_state.update(defaultData)
        st.rerun()
        return None

    # Set default parameters
    data = _data[st.session_state["localVars"]["languageAbbrev"]]

    fa_css = '''<i class="fab fa-github"></i>'''

    st.header(
        f'{settingsIcon} **{data["settings"]}**'
    )

    language = st.selectbox(
        f'**{data["selectLanguage"]}**',
        languages,
        index=languages.index(st.session_state["localVars"]["language"]),
        placeholder="Select language: "
    )
    data = _data[abbreviate[language]]

    if language != st.session_state["localVars"]["language"]:
        # Updating parameters
        st.session_state["localVars"]["data"] = data
        st.session_state["localVars"]["language"] = language
        st.session_state["localVars"]["languageAbbrev"] = abbreviate[language]
        st.rerun()

    cols = st.columns(
        [.2, .2, .6],
        gap="small",
        vertical_alignment="center"
    )

    st.page_link(
        "home.py", label="Home", icon=None
    )
    st.page_link(
        "pages/promptEdition.py", label="Edit", icon=None
    )
    st.page_link(
        "pages/outputPreview.py", label="Preview", icon=None
    )
    st.page_link(
        "pages/outputTranslation.py", label="Translation", icon=None
    )
    st.page_link(
        "pages/templateExplain.py", label="Template", icon=None
    )

    return None
