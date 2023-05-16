import streamlit as st

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

st.title('Hype Personal Dashboard')

st.markdown(
    """
    **Hello User, this is a WebApp for Hype card owners.**
"""    
)