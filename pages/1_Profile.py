import streamlit as st
import pandas as pd

@st.cache_data
def load_profile():
    profile = pd.read_json('json/profile.json', orient='index').transpose()
    return profile

st.set_page_config(
    page_title="Hype Personal Dashboard",
    page_icon="🏠",
    initial_sidebar_state='expanded',
    menu_items={
        'Get Help': 'https://github.com/MatteoFasulo/HypeAPI',
        'Report a bug': "https://github.com/MatteoFasulo/HypeAPI/issues",
        'About': 
            """
            # Hype Personal Dashboard
            This webapp was created with the aim of allowing Hype users to better analyze their account through the use of aggregated statistics and graphs.
            Any contribution to this project is welcome to improve the quality of work!

            GitHub Repository: https://github.com/MatteoFasulo/HypeAPI
            """
        }
)

profile = load_profile()
profile = profile.iloc[0]

st.title(f"Welcome  {profile.firstname.capitalize()} {profile.lastname.capitalize()}!")
st.header("Account Information")
st.subheader("Phone Number")
st.write(profile.phone)
st.subheader("Email")
st.write(profile.email)
st.subheader("Address")
st.write(f"{profile.address}, {profile.city} ({profile.zipCode})")
st.divider()
st.header("Current Plan")
st.write(profile.userType)