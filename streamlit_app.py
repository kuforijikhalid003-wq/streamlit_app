# Day 6

import streamlit as st

st.write('# Uploading your Streamlit app on GitHub')

import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

st.header('st.write')
# Example 1

st.write('Hello, *World!* :sunglasses:')

# Example 2

st.write('### Display Numbers ###')
st.write(1234)

# Example 3

st.write('### Display a DataFrame ###')
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})
st.write(df)

# Example 4

st.write('### Accept Multiple Arguments ###')
st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

# Example 5

st.write('### Display Charts ###')
df2  = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a', 'b', 'c']
)

c = alt.Chart(df2).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c']
)

st.write(c)