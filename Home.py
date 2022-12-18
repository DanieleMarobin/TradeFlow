# https://share.streamlit.io/

# https://share.streamlit.io/danielemarobin/monitor/main/Home.py

# Bloomberg API installing process
# https://discuss.streamlit.io/t/installing-packages-from-the-web/27537

# pipreqs --encoding=utf8

import streamlit as st
from datetime import datetime as dt

import numpy as np
import pandas as pd

import GDrive as gd

from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode, DataReturnMode, ColumnsAutoSizeMode, JsCode, AgGridTheme

st.set_page_config(page_title="Trade Flow",layout="wide",initial_sidebar_state="expanded")

st.markdown("# Trade Flow")
st.sidebar.markdown("# Trade Flow")

file_h ='Data/GTIS/Corn_Trade_Flow.csv'
df_h = gd.read_csv(file_h)

st.dataframe(df_h)