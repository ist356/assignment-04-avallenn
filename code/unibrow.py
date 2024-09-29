'''
Solution unibrow.py
'''
import pandas as pd
import streamlit as st
import pandaslib as pl
from pandaslib import get_column_names, get_columns_of_type, get_unique_values, get_file_extension, load_file

st.title("UniBrow")
st.caption("The Universal data browser")

file = st.file_uploader("Upload a file", type=['csv', 'xlsx', 'json'])
if file:
    file_path = get_file_extension(file.name)
    df = load_file(file, file_path)
    columns = get_column_names(df)
    selected_columns = st.multiselect("Select columns to display", columns)
    if st.checkbox("Filter data"):
        type_columns = get_columns_of_type(df, 'object')
        filter_columns = st.selectbox("Select column to filter", type_columns)
        if filter_columns:
            values = get_unique_values(df, filter_columns)
            value = st.selectbox("Select value to filter on", values)
            df_show = df[df[filter_columns] == value][selected_columns]
    else:
        df_show = df[selected_columns]

    st.dataframe(df_show)

