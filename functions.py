import os
import pickle
import textwrap
from typing import Any

import streamlit as st

from data import API_KEYS_FILE, CACHE_PATH

def cssStyles():
    styles = open("./styles.css", "r").read()
    # output = textwrap.dedent(f"""
    # <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
    # <style>
    # {styles}
    # </style>
    # """)
    return styles


def setPageConfig():

    try:
        favicon = st.session_state["icons"]["favicon"]\
            if "icons" in st.session_state\
            else None

        # Set page config
        st.set_page_config(
            page_title="Pyfuc APP",
            page_icon=favicon,
            layout="wide",
            initial_sidebar_state="expanded",
        )

    except KeyError:
        from data import setDefault
        setDefault()
        st.switch_page("home.py")

    except Exception as err:
        print(err)
        st.switch_page("home.py")

    return None

def generateGptResponse(apiKey, model, persona, prompt):
    # Implement your GPT interaction logic here
    # Example: Use OpenAI API or any other library to generate response
    # Replace this placeholder with actual code
    return "This is a sample generated response."

def updateApiKeys(key):

    if not any(key):
        return None

    with open(API_KEYS_FILE, 'r+') as f:
        lines = f.readlines()
        if not (f"{key}\n" in lines or key in lines):
            f.seek(0); f.truncate(0)
            f.writelines([f"{key}\n", *lines])
            st.success("API key added to list", icon="✅")
            st.toast("API key added to list", icon="✅")
        else:
            st.error("API key already exists", icon="❌")
            st.toast("API key already exists", icon="❌")
    return None

def storeCache(
        key: str,
        cachePath: str = CACHE_PATH
        ) -> (None):

    # Set the cache file path
    cacheFile = f"{cachePath}/{key}.pkl"

    # Getting data from session state
    dataToCache = st.session_state[key]

    # # Loading cache file
    # cacheData = loadCache(cacheFile)

    # if cacheData is not None:
    #     # Updating cache data
    #     cacheData[key] = dataToCache
    # else:
    #     # Asking for store
    #     overwrite = cachingConfirm(key)

    #     if not overwrite:
    #         return None

    # Updating cache file
    with open(cacheFile, "wb") as file:
        pickle.dump(dataToCache, file)

    return None

@st.dialog("Cache overwrite")
def cachingConfirm():
    st.write(f"Do you want the input data on cache?")
    cols = st.columns(
        [.1, .1, .8],
        gap="small",
        vertical_alignment="center"
    )
    with cols[0]:
        yesBtn = st.button("Yes", type="primary")
    with cols[1]:
        cancelBtn = st.button("Cancel", type="secondary")

    if cancelBtn:
        st.rerun()

    return yesBtn


def loadCache(cacheFile: str) -> (dict):

    if os.path.exists(cacheFile):
        with open(cacheFile, "rb") as file:
            cacheData = pickle.load(file)
    else:
        with open(cacheFile, "wb") as file:
            pickle.dump(None, file)
            cacheData = None

    return cacheData


def getFromCache(key: str) -> (Any):
    cacheFile = f"{CACHE_PATH}/{key}.pkl"
    return pickle.load(cacheFile)


def cacheKeys():
    cacheFiles = os.listdir(CACHE_PATH)
    cacheKeys = [
        file.split(".")[0]
            for file in cacheFiles
            if file.endswith(".pkl")
    ]
    return cacheKeys


if not any(st.session_state):
    st.session_state.update({
        "functions": {
            "updateApiKeys": updateApiKeys,
            "generateGptResponse": generateGptResponse,
            "storeCache": storeCache,
            "loadCache": loadCache,
        }
    })