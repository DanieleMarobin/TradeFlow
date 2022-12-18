# https://share.streamlit.io/

# https://share.streamlit.io/danielemarobin/monitor/main/Home.py

# Bloomberg API installing process
# https://discuss.streamlit.io/t/installing-packages-from-the-web/27537

# pipreqs --encoding=utf8

import streamlit as st

st.set_page_config(page_title="Trade Flow",layout="wide",initial_sidebar_state="expanded")

st.markdown("# Trade Flow")
st.markdown("---")

link='Trade Flow: [Trade Flow](https://danielemarobin-tradeflow-home-edl64h.streamlit.app/)'
st.markdown(link,unsafe_allow_html=True)
st.markdown(link)

st.write(link)

st.sidebar.markdown("# Trade Flow")