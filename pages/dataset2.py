import streamlit as st
from matplotlib import image
import pandas as pd
import plotly.express as px
st.header("covid :red[india]")
df=pd.read_csv("E:\\VK\\datasets\\covid.india.csv")
st.dataframe(df)
Nam = st.selectbox("Select the Name of state:", df['State/UTs'].unique())
col1,col2=st.columns(2)
fig_1 = px.box(df[df['State/UTs'] == Nam], x="Deaths",y="Active",title="Deaths vs Active")
col1.plotly_chart(fig_1, use_container_width=True)
fig_2 = px.box(df[df['State/UTs'] == Nam], x="Population",y="Discharged",title="Population vs Discharged")
col2.plotly_chart(fig_2, use_container_width=True)
