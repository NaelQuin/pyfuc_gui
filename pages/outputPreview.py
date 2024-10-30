import streamlit as st

from pages.sidebar import sidebarPage
from data import *

sidebarPage()

st.switch_page("pages/maintenance.py")