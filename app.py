import numpy as np
import pandas as pd
import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

st.set_page_config(page_title = 'Data_Analysis.com',layout='wide')


# Web App Title
st.markdown(
    """
    <div style='text-align:center; background-color:#00c5c8; padding: 20px'>
        <h1>Data-Analysis</h1>
        <h3>Data Analysis with pandas-profiling</h3>
        <div style='background-color:#8e8e8e; padding: 10px'>
            <p style='margin-bottom: 0;'><b>Credit :</b> App built in `Python` + `Streamlit` by </p>
            <p style='margin-top: 0;'><a href='https://github.com/SarangGami'>SARANG GAMI</a></p>
        </div>
    </div>
    <div style='height: 5px'></div>
    """,
    unsafe_allow_html=True
)


# Upload CSV data
with st.sidebar.header('📤 Upload Your CSV Dataset'):
    uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])
    st.sidebar.markdown("""
[Example Of CSV input file](https://raw.githubusercontent.com/SarangGami/EDA-Analysis-WEBSITE-using-pandas-profile-report/main/CSV%20files%20for%20website%20demo/automobile_data.csv)
""")

# Pandas Profiling Report
if uploaded_file is not None:
    @st.cache_data
    def load_csv():
        csv = pd.read_csv(uploaded_file)
        return csv
    df = load_csv()
    pr = ProfileReport(df, explorative=True)
    st.header('**Input DataFrame**')
    st.write(df)
    st.write('---')
    st.header('**Pandas Profiling Report**')
    st_profile_report(pr)

else:
    st.markdown(
        """
        <div style='background-color: #occ9bc; padding: 10px;'>
            <h3 style='margin-top: 0;'>Awaiting CSV file upload</h3>
            <p style='margin-bottom: 0;'>Please upload a CSV file to begin the analysis.</p>
            <p style='margin-top: 0;'>Alternatively, click the button below to use an example dataset.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        """
        <div style='height:5px'></div>
        """,
        unsafe_allow_html=True
    )
    if st.button('Press to use Example Dataset'):
        st.markdown(
            """
            <div style='background-color: #4b8b3b; padding: 10px; margin-top: 5px;'>
                <p style='margin-bottom: 0;'>Using example dataset.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        
        # Example data
        @st.cache_data
        def load_data():
            url = 'https://raw.githubusercontent.com/SarangGami/EDA-Analysis-WEBSITE-using-pandas-profile-report/main/CSV%20files%20for%20website%20demo/phone_data.csv'
            df = pd.read_csv(url)
            return df
        df = load_data()
        pr = ProfileReport(df, explorative=True)
        st.header('**Input DataFrame**')
        st.write(df)
        st.write('---')
        st.header('**Pandas Profiling Report**')
        st_profile_report(pr)

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden; }
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)
