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

# input data
if True:
    file_h ='Data/GTIS/Corn_Trade_Flow.csv'
    rows_per_page=20
    df_h=None

    if ('df_h' in st.session_state):
        df_h=st.session_state['df_h']
    else:
        st.write('Getting data from Google Drive')
        df_h = gd.read_csv(file_h)
        df_h=df_h.drop(columns=['HS4 Code']) 
        st.session_state['df_h'] = gd.read_csv(file_h)
        df_h=st.session_state['df_h']


# Table
if True:
    df=df_h
    if df is not None:    
        statusPanels = {'statusPanels': [
            # { 'statusPanel': 'agTotalAndFilteredRowCountComponent', 'align': 'left' },
            # { 'statusPanel': 'agTotalRowCountComponent', 'align': 'center' },
            { 'statusPanel': 'agFilteredRowCountComponent', 'align': 'left' },
            { 'statusPanel': 'agSelectedRowCountComponent', 'align': 'left' },
            { 'statusPanel': 'agAggregationComponent', 'align': 'left' },
            ]}

        gb = GridOptionsBuilder.from_dataframe(df)
        gb.configure_pagination(paginationAutoPageSize=False, paginationPageSize=rows_per_page)
        gb.configure_default_column(groupable=True, value=True, enableRowGroup=True, aggFunc='sum', editable=True,rowMultiSelectWithClick=False)
        gb.configure_selection('multiple', use_checkbox=False)
        gb.configure_grid_options(enableRangeSelection=True, statusBar=statusPanels)
        gb.configure_side_bar(defaultToolPanel='test')

        # gb.configure_column('trade', headerCheckboxSelection = True, headerCheckboxSelectionFilteredOnly=True)
        # gb.configure_column('analysis_range', headerCheckboxSelection = True)
        gridOptions = gb.build()

        grid_response = AgGrid(df, gridOptions=gridOptions, data_return_mode=DataReturnMode.FILTERED, update_mode=GridUpdateMode.MANUAL, columns_auto_size_mode=ColumnsAutoSizeMode.FIT_CONTENTS, enable_enterprise_modules=True)
        # st.write(grid_response.keys())
        # st.write('selected_rows')
        # st.write(grid_response['selected_rows'])

        selected_rows=grid_response['selected_rows']
        selected_df=pd.DataFrame(grid_response['selected_rows'])