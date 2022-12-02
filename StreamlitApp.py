import streamlit as st
import streamlit_authenticator

st.set_page_config(page_title="Movie Booking System", page_icon=":movie_camera:", layout="wide")

# log in
usernames = ['jsmith', 'rbriggs']
names = ['John Smith', 'Rebecca Briggs']
passwords = ['123', '456']
hashed_passwords = streamlit_authenticator.Hasher(passwords).generate()

credentials = {
    "usernames": {
        usernames[0]: {
            "name": names[0],
            "password": hashed_passwords[0]
        },
        usernames[1]: {
            "name": names[1],
            "password": hashed_passwords[1]
        }
    }
}
authenticator = streamlit_authenticator.Authenticate(credentials, "app_home", "auth", cookie_expiry_days=30)
name, authentication_status, username = authenticator.login('Log in', 'main')

# home page
if st.session_state["authentication_status"]:
    authenticator.logout("Logout", "sidebar")
    st.sidebar.title(f"Welcome {name}")

    st.title("Home")


# login failure
elif st.session_state["authentication_status"] is False:
    st.error("username or password is incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning("Please enter your username and password")