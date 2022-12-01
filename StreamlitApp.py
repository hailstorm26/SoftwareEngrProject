import streamlit as st
import pickle
from pathlib import Path
import yaml
from streamlit_authenticator import Authenticate
from yaml import SafeLoader

st.set_page_config(page_title="Movie Booking System", page_icon=":movie_camera:", layout="wide")


# log in
with open('credentials.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

name, authentication_status, username = authenticator.login('Log in', 'main')

# home page
if st.session_state["authentication_status"]:
    authenticator.logout("Logout", "sidebar")
    st.sidebar.title(f"Welcome {name}")

    st.title("Home")
    st.button("Search Movies")
    st.button("Browse Current Movie Catalog")
    st.button("Browse Upcoming Movie Catalog")

# login failure
elif st.session_state["authentication_status"] is False:
    st.error("username or password is incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning("Please enter your username and password")