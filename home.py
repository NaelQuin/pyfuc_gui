import json
import pickle

import streamlit as st
import pandas as pd
from pyidebug import debug

from pages.sidebar import sidebarPage

from data import (_data, _prompts, _personas, abbreviate, languages,
                  apiKeys, favicon, instructionsIcon, editIcon, plusIcon,
                  gptIcon, settingsIcon, gptModels, defaultLanguage,
                  API_KEYS_FILE, CACHE_PATH)

from functions import (generateGptResponse, updateApiKeys, setPageConfig,
                       storeCache, cacheKeys)

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

@st.cache_data
def cachingUploadedFiles(files):
    return files

def main():
    # Set page config
    setPageConfig()

    st.write(
        """<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">""",
        unsafe_allow_html=True
    )

    st.session_state.elements = {}
    st.session_state.trash = {}

    with st.sidebar:
        sidebarPage()

    data = st.session_state["localVars"]["data"]
    language = st.session_state["localVars"]["language"]

    st.title(data['title'], anchor="home.py")

    st.write(data['description'])

    expander = st.expander(
        f'**{data["instructionsTitle"]}**',
        expanded=False,
        icon=st.session_state["icons"]["instructions"]
    )

    with expander:
        st.markdown(data["instructions"])

    # with st.popover(f'{instructionsIcon}'):
    # #with st.popover(f'{instructionsIcon} {data["instructionsTitle"]}'):
    #     st.markdown(data["instructions"])

    from PIL import Image

    expander = st.expander(
        f' **GPT parameters**',
        expanded=not st.session_state["generated"],
        icon=st.session_state["icons"]["gpt"]
    )

    with expander:
        cols = st.columns(
            [.9, .18],
            gap="small",
            vertical_alignment="bottom"
        )

        with cols[0]:
            # Text entry for GPT API key
            apiKey = st.selectbox(
                f'**{data["api"]}**',
                apiKeys,
                placeholder="Select or type your GPT API key"
            )

        with cols[1]:

            popoverApiKey = st.popover(
                plusIcon,
                help="Add a new GPT API key",
                )

            with popoverApiKey:
                st.text_input(
                    f'**{data["apiNew"]}**',
                    on_change=lambda: updateApiKeys(st.session_state["newApiKey"]),
                    key="newApiKey",
                    placeholder="Enter your GPT API key",
                )

        # Dropdown for GPT models
        selected_model = st.selectbox(
            f'**{data["gptModel"]}**',
            gptModels,
            index=7,
            placeholder="Select GPT Model"
        )

        # Persona and prompt entry
        persona = st.selectbox(
            f'**{data["persona"]}**',
            _personas[abbreviate[language]],
            index=0,
            placeholder="Select Persona"
        )

        cols = st.columns(
            [.925, .07],
            gap="small",
            vertical_alignment="bottom"
        )

        with cols[0]:
            prompt = st.selectbox(
                f'**{data["prompt"]}**',
                _prompts[abbreviate[language]],
                index=0,
                placeholder=data["promptPlaceholder"]
            )

            if prompt == _prompts[abbreviate[language]][-1]:
                st.session_state["promptChoice"] = "other"
                st.switch_page("pages/promptEdition.py")

        with cols[1]:
            # Clear button
            editPromptBtn = st.button(
                editIcon,
                type="secondary",
            )

            if editPromptBtn:
                st.session_state["promptChoice"] = prompt
                st.switch_page("pages/promptEdition.py")

    # ==========
    # INPUT DATA
    # ==========
    st.write("### Curricular Unit Data")

    # st.write(
    #     f'<a href="home.py">{st.session_state["fa_icons"]["uploadB"]}</a>',
    #     unsafe_allow_html=True
    # )

    cols = st.columns(1)

    with cols[0]:
        importContainer = st.popover(
            "**Import Data**",
            icon=st.session_state["icons"]["upload"],
            help="Upload a JSON or CSV file containing the curricular unit data",
        )
        
        with importContainer:
            # Import data
            filesUploaded = st.file_uploader(
                f'Import Data',
                help="Upload a JSON or CSV file containing the curricular unit data",
                type=["json", "csv"],
                accept_multiple_files=True
            )

    if not any(filesUploaded) and 'files_cache' in cacheKeys():
        filesCache = st.session_state.get(
            "files_cache",
            pickle.load(open("./.streamlit/cache/files_cache.pkl", "rb"))
        )
    else:
        filesCache = {}

    # Set the default CU data
    if not any(filesUploaded) and not any(filesCache):
        cu_data = st.session_state["cu_data"] = {
            "cu_name": "",
            "cu_year": "",
            "ects": "",
            "contact_hours": "",
            "syllabus": "",
        }

        with st.container():
            # Four columns for input fields
            col1, col2, col3, col4 = st.columns(
                [.55, .13, .13, .13],
                gap="small",
                vertical_alignment="center"
            )

            with col1:
                cu_name = st.text_input(
                    "Name",
                    cu_data["cu_name"],
                )

            with col2:
                cu_year = st.text_input(
                    "Year",
                    cu_data["cu_year"],
                )

            with col3:
                ects = st.text_input(
                    "ECTS",
                    cu_data["ects"],
                )

            with col4:
                contact_hours = st.text_input(
                    "Contact Hours",
                    cu_data["contact_hours"],
                )

            # Text area for syllabus
            syllabus = st.text_area(
                "Syllabus",
                cu_data["syllabus"],
                height=200
            )

    elif not any(filesUploaded) and len(filesCache) == 1:
        cu_data = st.session_state["cu_data"] = dict(filesCache.values())

        with st.container():
            # Four columns for input fields
            col1, col2, col3, col4 = st.columns(
                [.55, .13, .13, .13],
                gap="small",
                vertical_alignment="center"
            )

            with col1:
                cu_name = st.text_input(
                    "Name",
                    cu_data["cu_name"],
                )

            with col2:
                cu_year = st.text_input(
                    "Year",
                    cu_data["cu_year"],
                )

            with col3:
                ects = st.text_input(
                    "ECTS",
                    cu_data["ects"],
                )

            with col4:
                contact_hours = st.text_input(
                    "Contact Hours",
                    cu_data["contact_hours"],
                )

            # Text area for syllabus
            syllabus = st.text_area(
                "Syllabus",
                cu_data["syllabus"],
                height=200
            )

    elif not any(filesUploaded):

        for i, v in enumerate(filesCache.values()):
            if i == 0:
                st.session_state["cu_data"] = []

            # Get data and type from file
            fileType = file.type

            if fileType == "application/json":
                cu_data = json.load(file)
                cu_data = {
                    "cu_name": cu_data["cu_name"],
                    "cu_year": str(cu_data["cu_year"]),
                    "ects": str(cu_data["ects"]),
                    "contact_hours": str(cu_data["contact_hours"]),
                    "syllabus": cu_data["syllabus"],
                }
            elif fileType == "text/csv":
                cu_data = pd.read_csv(file)
                cu_data = {
                    "cu_name": cu_data.loc[0,"cu_name"],
                    "cu_year": str(cu_data.loc[0,"cu_year"]),
                    "ects": str(cu_data.loc[0,"ects"]),
                    "contact_hours": str(cu_data.loc[0,"contact_hours"]),
                    "syllabus": cu_data.loc[0,"syllabus"],
                }

            st.session_state["cu_data"].append(cu_data)

            if file.name not in filesCache:
                filesCache[file.name] = cu_data

        st.session_state["files_cache"] = filesCache

        for i, cu_data in enumerate(st.session_state["cu_data"]):

            with st.container(border=True):
                st.write(f"### {cu_data['cu_name'].capitalize()}")

                # Four columns for input fields
                cols = st.columns(
                    [.88, .12],
                    gap="small",
                    vertical_alignment="center"
                )

                with cols[0]:
                    # Text area for syllabus
                    syllabus = st.text_area(
                        "Syllabus",
                        cu_data["syllabus"],
                        height=225,
                        key=f"syllabus_{i}"
                    )

                with cols[1]:
                    cu_year = st.text_input(
                        "Year",
                        cu_data["cu_year"],
                        key=f"cu_year_{i}"
                    )

                    ects = st.text_input(
                        "ECTS",
                        cu_data["ects"],
                        key=f"ects_{i}"
                    )

                    contact_hours = st.text_input(
                        "Contact Hours",
                        cu_data["contact_hours"],
                        key=f"contact_hours_{i}"
                    )

    else:

        for i, file in enumerate(filesUploaded):
            if i == 0:
                st.session_state["cu_data"] = []

            # Get data and type from file
            fileType = file.type

            if fileType == "application/json":
                cu_data = json.load(file)
                cu_data = {
                    "cu_name": cu_data["cu_name"],
                    "cu_year": str(cu_data["cu_year"]),
                    "ects": str(cu_data["ects"]),
                    "contact_hours": str(cu_data["contact_hours"]),
                    "syllabus": cu_data["syllabus"],
                }
            elif fileType == "text/csv":
                cu_data = pd.read_csv(file)
                cu_data = {
                    "cu_name": cu_data.loc[0,"cu_name"],
                    "cu_year": str(cu_data.loc[0,"cu_year"]),
                    "ects": str(cu_data.loc[0,"ects"]),
                    "contact_hours": str(cu_data.loc[0,"contact_hours"]),
                    "syllabus": cu_data.loc[0,"syllabus"],
                }

            st.session_state["cu_data"].append(cu_data)

            if file.name not in filesCache:
                filesCache[file.name] = cu_data

        st.session_state["files_cache"] = filesCache
        storeCache('files_cache')

        for i, cu_data in enumerate(st.session_state["cu_data"]):

            with st.container(border=True):
                st.write(f"### {cu_data['cu_name'].capitalize()}")

                # Four columns for input fields
                cols = st.columns(
                    [.88, .12],
                    gap="small",
                    vertical_alignment="center"
                )

                with cols[0]:
                    # Text area for syllabus
                    syllabus = st.text_area(
                        "Syllabus",
                        cu_data["syllabus"],
                        height=225,
                        key=f"syllabus_{i}"
                    )

                with cols[1]:
                    cu_year = st.text_input(
                        "Year",
                        cu_data["cu_year"],
                        key=f"cu_year_{i}"
                    )

                    ects = st.text_input(
                        "ECTS",
                        cu_data["ects"],
                        key=f"ects_{i}"
                    )

                    contact_hours = st.text_input(
                        "Contact Hours",
                        cu_data["contact_hours"],
                        key=f"contact_hours_{i}"
                    )

    # =======
    # BUTTONS
    # =======
    cols = st.columns(
        [.35, .7],
    )

    with cols[0]:
        with st.container():
            cols = st.columns(
                2,
                gap="small",
                vertical_alignment="center"
            )

            with cols[0]:
                # Generate response button
                generateResponseBtn = st.button(
                    f'**{data["generateResponse"]}**',
                    type="primary"
                )

            with cols[1]:
                if st.session_state["generated"]:
                    if generateResponseBtn:
                        st.toast("Response generation successful!", icon="✅")
                    viewResponseBtn = st.button(
                        f'**{data["viewResponse"]}**',
                        type="secondary"
                    )

                    if viewResponseBtn:
                        st.switch_page("pages/outputPreview.py")

    # Submit button
    if generateResponseBtn:
        # Call GPT model with provided inputs (use your API integration)
        generated_response = generateGptResponse(
            apiKey, selected_model,
            persona, prompt
            )
        if not apiKey:
            st.warning('Please input a API Key', icon="⚠️")
            st.toast('Please input a API Key', icon="⚠️")
            st.stop()
        st.write(generated_response)
        st.session_state["generated"] = True
        st.rerun()

if __name__ == "__main__":
    main()
