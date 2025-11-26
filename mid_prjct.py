import streamlit as st
import pandas as pd 
import plotly.express as px 
st.set_page_config(layout='wide')
df = pd.read_csv('D:/Data/Mid_Project/Data Set/medicines_data_updated_1.csv')
mst_drg = df['Drugname'].value_counts().head(10).reset_index()
cont = df.groupby(['Category', 'Region', 'Form', 'Company'])['Drugname'].count().reset_index()

st.markdown("<h1 style = 'text-align : center ; color : green;' > Medicines From Egyption Market </h1>" , unsafe_allow_html=True)
category = st.sidebar.multiselect('Filter by Category', options=df['Category'].unique())
category = df['Category'].unique() if category == [] else category
df = df[df['Category'].isin(category)]

col1, col2 = st.columns(2)
col1.metric('Total Sales', f'{int(df['Price'].sum()) : ,}')
col2.metric('Total Qantities', f'{df['Category'].count() : ,}')

tab1, tab2, tab3, tab4 = st.tabs(['Category', 'Company', 'Form', 'Region'])

with tab1 :
    st.plotly_chart(px.histogram(data_frame=df, x='Category', y='Price', text_auto=True, title='Total Sales per Category').update_xaxes(categoryorder='total descending'))
    st.plotly_chart(px.pie(data_frame=df, names='Category', values='Price', title='Percentages are Proportionate for all Category'))
    st.plotly_chart(px.histogram(data_frame=df, x='Category', y='Price', text_auto=True, color='Region', barmode='group',title='Total Sales per Region over Category').update_xaxes(categoryorder='total descending'))
    st.plotly_chart(px.histogram(data_frame=df, x='Category', y='Price', text_auto=True, color='Company', barmode='group', title='Total Sales per Company over Category').update_xaxes(categoryorder='total descending'))
    st.plotly_chart(px.histogram(data_frame=df, x='Category', y='Price', text_auto=True, color='Form', barmode='group', title='Total Sales per Form over Category').update_xaxes(categoryorder='total descending'))
    st.plotly_chart(px.histogram(data_frame=cont, x='Category', y='Drugname', color='Company', barmode='group', text_auto=True, title='Most Ordered Quantities per Company'))
with tab2 :
    st.plotly_chart(px.histogram(data_frame=df, x='Company', y='Price', text_auto=True, title='Total Sales per Company').update_xaxes(categoryorder='total descending'))
    st.plotly_chart(px.histogram(data_frame=df, x='Company', y='Price', text_auto=True, color='Category', barmode='group', title='Total Sales per Category over Company').update_xaxes(categoryorder='total descending'))
    st.plotly_chart(px.histogram(data_frame=df, x='Company', y='Price', text_auto=True, color='Region', barmode='group', title='Total Sales per Region over Company').update_xaxes(categoryorder='total descending'))
    st.plotly_chart(px.histogram(data_frame=df, x='Company', y='Price', text_auto=True, color='Form', barmode='group', title='Total Sales per Form over Company').update_xaxes(categoryorder='total descending'))
with tab3 : 
    st.plotly_chart(px.histogram(data_frame=df, x='Form', y='Price', text_auto=True, title='Total Sales per Form').update_xaxes(categoryorder='total descending'))
    st.plotly_chart(px.histogram(data_frame=df, x='Form', y='Price', text_auto=True, color='Category', barmode='group', title='Total Sales per Category over Form').update_xaxes(categoryorder='total descending'))
    st.plotly_chart(px.histogram(data_frame=df, x='Form', y='Price', text_auto=True, color='Company',barmode='group', title='Total Sales per Company over Form').update_xaxes(categoryorder='total descending'))
    st.plotly_chart(px.histogram(data_frame=df, x='Form', y='Price', text_auto=True, color='Region', barmode='group', title='Total Sales per Region over Form').update_xaxes(categoryorder='total descending'))
    st.plotly_chart(px.histogram(data_frame=cont, x='Category', y='Drugname', color='Form', barmode='group', text_auto=True, title='Most Ordered Quantities per Form'))
    st.plotly_chart(px.histogram(data_frame=mst_drg, x='Drugname', y='count', text_auto=True, title='Quantities of Top 10 Drugs Mostly Sold'))
with tab4 :
    st.plotly_chart(px.histogram(data_frame=df, x='Region', y='Price', text_auto=True, title='Total Sales per Region').update_xaxes(categoryorder='total descending'))
    st.plotly_chart(px.histogram(data_frame=df, x='Region', y='Price', text_auto=True, color='Category', barmode='group', title='Total Sales per Category over Region').update_xaxes(categoryorder='total descending'))
    st.plotly_chart(px.histogram(data_frame=df, x='Region', y='Price', text_auto=True, color='Company', barmode='group', title='Total Sales per Company over Region').update_xaxes(categoryorder='total descending'))
    st.plotly_chart(px.histogram(data_frame=df, x='Region', y='Price', text_auto=True, color='Form', barmode='group', title='Total Sales per Form over Region').update_xaxes(categoryorder='total descending'))
    st.plotly_chart(px.histogram(data_frame=cont, x='Category', y='Drugname', color='Region', barmode='group', text_auto=True, title='Most Ordered Quantities per Region'))
