import streamlit as st
from PIL import Image

from data import defaultData
from functions import setPageConfig

setPageConfig()

try:
    _ = st.session_state['icons']
except Exception as err:
    st.session_state.update(defaultData)

st.title(f"Page is under Maintenance {st.session_state['icons']['sad']}")

st.write("""
    This page is under maintenance.

    Please come back later."""
)

homeBtn = st.button(
    "Back Home",
    type="primary",
)

if homeBtn:
    st.switch_page("home.py")
