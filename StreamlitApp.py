import streamlit as st
import streamlit_authenticator as stauth

st.set_page_config(page_title="Movie Booking System", page_icon=":movie_camera:", layout="wide")

# log in
usernames = ["user1", "user2", "user3"]
passwords = ["pw111", "pw222", "pw333"]

authenticator = stauth.Authenticate(usernames, passwords, "dashboard", "abcdef", cookie_expiry_days=30)

username, authentication_status = authenticator.login("Login", "main")

if authentication_status == False:
    st.error("username or password is incorrect")

if authentication_status == None:
    st.error("Please enter your username and passowrd")

# home page
if authentication_status == True:
    authenticator.logout("Logout", "sidebar")
    st.sidebar.title("Your account")

    st.title("Home")
    st.button("Search Movies")
    st.button("Browse Current Movie Catalog")
    st.button("Browse Upcoming Movie Catalog")

