import streamlit as st
from PIL import Image

from data import *
from functions import setPageConfig
from pages.sidebar import sidebarPage

# custom_html = """
# <div class="header">
#     <div class="logo">
#         <a href="home.py" target="_self">
#             <img src="https://i.imgur.com/YonN1NM.png?1"
#                  title="source: imgur.com"
#                  alt="{{$lang.project_name}}"
#                  id="logo-changer">
#         </a>
#     </div>
# </div>
# """

# <div class="banner" onclick="window.location.href = 'http://localhost/home.py';">
#     <img src="https://img.freepik.com/premium-photo/wide-banner-with-many-random-square-hexagons-charcoal-dark-black-color_105589-1820.jpg" alt="Banner Image">
# </div>
# <style>
#     .banner {
#         width: 160%;
#         height: 200px;
#         overflow: hidden;
#     }
#     .banner img {
#         width: 100%;
#         object-fit: cover;
#     }
# </style>

# # Display the custom HTML
# st.components.v1.html(custom_html)

setPageConfig()

st.title("Prompt Edition")

with st.sidebar:
    sidebarPage()

cols = st.columns(
    [.5, .5],
    gap="medium",
    vertical_alignment="center"
)

with cols[0]:
    ilo = st.text_area(
        "Intend Learning Outcomes (ILOs)",
        height=300,
        placeholder="Type the ILO's prompt",
    )

    tm = st.text_area(
        "Teaching Methodology (TM)",
        height=300,
        placeholder="Type the TM's prompt",
    )

    evTmAss = st.text_area(
        "Evidence between TM and Assessment",
        height=300,
        placeholder="Type the evidence between TM and Assessment's prompt",
    )

    obs = st.text_area(
        "Observations",
        height=300,
        placeholder="Type the observation's prompt",
    )

with cols[1]:
    evSyIlo = st.text_area(
        "Evidence between Sylabus and ILO",
        height=300,
        placeholder="Type the evidence between Sylabus and ILO's prompt",
    )

    ass = st.text_area(
        "Assessment (A)",
        height=300,
        placeholder="Type the assessment's prompt",
    )

    bib = st.text_area(
        "Bibliography",
        height=300,
        placeholder="Type the bibliography's prompt",
    )

    fCheck = st.text_area(
        "Final Check Rules",
        height=300,
        placeholder="Type the final check rule's prompt",
    )

cols = st.columns(
    [.8, .2],
    gap="small",
    vertical_alignment="bottom"
)

with cols[0]:
    backBtn = st.button(
        "Back",
        type="secondary"
    )

    if backBtn:
        st.switch_page("home.py")

with cols[1]:

    cols = st.columns(
        [.35, .4, .35],
        gap="small",
        vertical_alignment="bottom"
    )

    with cols[1]:
        st.button(
            #"Revert",
            st.session_state["icons"]["revert"],
            type="secondary",
            help="Restore default prompt"
        )

    with cols[2]:
        st.button(
            "Save",
            type="primary"
        )
