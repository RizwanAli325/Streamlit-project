import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
df=pd.read_csv('india.csv')
st.set_page_config(layout='wide')
list_of_state=list(df['State'].unique())
list_of_state.insert(0,'Overall india')
# print(list_of_state)

st.sidebar.title('India Data Visulization')
selected_state=st.sidebar.selectbox('Select a State',list_of_state)
primary=st.sidebar.selectbox('Select primary parameter',sorted(df.columns[5:]))
secondary=st.sidebar.selectbox('Select secondary parameter',sorted(df.columns[5:]))
plot=st.sidebar.button('Plot Graph')
if plot:
    st.text('size represent primary parameter')
    st.text('color represent secondary parameter')

    if selected_state=='Overall india':
      fig=px.scatter_mapbox(df,lat='Latitude',lon='Longitude',size=primary,size_max=35,color=secondary,zoom=3,mapbox_style='carto-positron',height=500,width=1200,hover_name='District')
      st.plotly_chart(fig,use_container_width=True)
    else:
     state_df=df[df['State']==selected_state] 
     fig=px.scatter_mapbox(state_df,lat='Latitude',lon='Longitude',size=primary,size_max=35,color=secondary,zoom=3,mapbox_style='carto-positron',height=500,width=1200,hover_name='District')
     st.plotly_chart(fig,use_container_width=True)

