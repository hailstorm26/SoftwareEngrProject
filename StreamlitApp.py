import streamlit as st
import pickle
from pathlib import Path
import streamlit_authenticator as stauth

st.set_page_config(page_title="Movie Booking System", page_icon=":movie_camera:", layout="wide")

names = ["Peter Parker", "Rebecca Miller"]
usernames = ["pparker", "rmiller"]
passwords = ["pw1", "pw2"]
hashed_passwords = stauth.Hasher(passwords).generate()

# log in
authenticator = stauth.Authenticate(names, usernames, hashed_passwords,
    "sales_dashboard", "abcdef", cookie_expiry_days=0)
name, authentication_status, username = authenticator.login("Login", "main")
if not authentication_status:
    st.error("username or password is incorrect")
if authentication_status is None:
    st.error("Please enter your username and passowrd")

# home page
if authentication_status:
    authenticator.logout("Logout", "sidebar")
    st.sidebar.title("Your account")

    st.title("Home")
    st.button("Search Movies")
    st.button("Browse Current Movie Catalog")
    st.button("Browse Upcoming Movie Catalog")

