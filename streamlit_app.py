import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header('st.write', anchor='st.write', help='st.write is the Swiss army knife of Streamlit commands. It does different things depending on what you give it.')

st.subheader('helloooooooooo')

st.caption("A caption with _italics_ and **bold** :blue[colors]")

st.text("This is some text.")

st.latex(r''' e^{i\pi} + 1 = 0 ''')

st.code("""def hello():
    print(\"Hello, Streamlit!\")""", language='python')


#example 1

st.write("Hello,  the *World!* :sunglasses:")

#example 2

st.write(1234)

#example 3

df = pd.DataFrame({
    'première colonne' : [1,2,3,4],
    'deuxième colonne' : [10,20,30,40]
})

st.write(df)

#example 4

st.write("Ci-dessoud se trouve un Dataframe :",df,"se trouve un dataframe.")

#example 5

df2 = pd.DataFrame(
    np.random.randn(200,3),
    columns = ['a','b','c']
    )

c= alt.Chart(df2).mark_circle().encode(
    x='a', y='b',size='c',color="b",tooltip=['a','b','c']
)

st.write(c)

