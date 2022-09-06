import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.title('welcome to my first penguin data app')
st. write('**starting** the *bulid* of penguin app :penguin:')

st.write('Data is taken from [palmerpenguins](https://gist.github.com/rxaviers/7360908)')
st.header('DATA')
df = pd.read_csv('penguins_extra.csv')
st.write('display a sample of 20 data points', df.sample(20))
species = st.selectbox(f'select species', df.species.unique())
st.write(f'displaying a subdataform from {species}', df[df['species'] == species])

# heading over to plotting
fig, ax = plt.subplots()
ax = sns.scatterplot(data=df, x='bill_length_mm', y='flipper_length_mm', hue='species')
st.pyplot(fig)

st.bar_chart(df.groupby('island')['species'].count())

st.map(df)

csv_var = st.sidebar.file_uploader('upload a csv file', type=['csv'])
if csv_var is not None:
    df = pd.read_csv(csv_var)
    st.write(df)