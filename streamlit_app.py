# Day 13

import platform
import numpy as np
import pandas as pd
import streamlit as st

st.title("☁️ Cloud Dev Test")
st.write("If you can see this, your cloud environment works!")

st.subheader("Environment info")
st.write("Python version:", platform.python_version())
st.write("OS:", platform.system())

st.subheader("Interactive check")
n = st.slider("Number of points", 10, 200, 50)
data = pd.DataFrame(np.random.randn(n, 3), columns=["a", "b", "c"])
st.line_chart(data)

c = alt.Chart(df2).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c']
)

st.write(c)
