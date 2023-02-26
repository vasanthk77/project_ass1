import streamlit as st
from matplotlib import image
import pandas as pd
import plotly.express as px
image=image.imread("project_ass1/resources/R.jfif")
st.image(image)
df=pd.read_csv("project_ass1/resources/pokemon.csv")
st.dataframe(df)
Nam = st.selectbox("Select the Name of Pokemon:", df['Name'].unique())
col1,col2=st.columns(2)
fig_1 = px.box(df[df['Name'] == Nam], x="Speed",title="speed of the pokemon")
col1.plotly_chart(fig_1, use_container_width=True)
fig_2 = px.box(df[df['Name'] == Nam], x="Defense",title="Defense of the pokemon")
col2.plotly_chart(fig_2, use_container_width=True)

