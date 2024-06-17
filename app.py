import streamlit as st
import pandas as pd

st.title('plan contable')

df= pd.read_excel('planContable.xlsx')

st.write(df)