import pandas as pd
import numpy as np
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from PIL import Image
df=pd.read_csv("Data/Share Market_Final.csv")
df['Gender'] = df['Gender'].astype('category')
df['Age'] = df['Age'].astype('category')
df['Marital.Status'] = df['Marital.Status'].astype('category')
df['Profession'] = df['Profession'].astype('category')
df['Education'] = df['Education'].astype('category')
df['Income'] = df['Income'].astype('category')
df['State'] = df['State'].astype('category')
df['Future_Perspective'] = df['Future_Perspective'].astype('category')
df['Existing_Loan'] = df['Existing_Loan'].astype('category')
df['Emergency_Fund'] = df['Emergency_Fund'].astype('category')
df['EMI.Loan'] = df['EMI.Loan'].astype('category')
df['Money_Attitude'] = df['Money_Attitude'].astype('category')
df['Financial_Efficacy'] = df['Financial_Efficacy'].astype('category')
df['Retirement'] = df['Retirement'].astype('category')
df['Inv_involved'] = df['Inv_involved'].astype('category')
df['Inv_Type'] = df['Inv_Type'].astype('category')
df['KSM'] = df['KSM'].astype('category')
df['Inv_Motive'] = df['Inv_Motive'].astype('category')
df['Inv_pattern'] = df['Inv_pattern'].astype('category')
df['Equity_Market'] = df['Equity_Market'].astype('category')
df['Demat_Account'] = df['Demat_Account'].astype('category')
df['Stock_opinion'] = df['Stock_opinion'].astype('category')
df['Inv_Advice'] = df['Inv_Advice'].astype('category')
df['Learning_inv'] = df['Learning_inv'].astype('category')
df['Inv_plan'] = df['Inv_plan'].astype('category')
df['Covid_SM'] = df['Covid_SM'].astype('category')
df['FL'] = df['FL'].astype('category')
df['SMI'] = df['SMI'].astype('category')


st.title(":green[_Financial Perspective and Share Market Analysis_]")

def home():
    
    a_link = st.multiselect("choose a link", ['https://yusra.shinyapps.io/Final_project_sm/','https://docs.streamlit.io/library/api-reference/widgets'])
    text='check out this [link]({link})'.format(link=a_link)
    st.markdown(a_link,unsafe_allow_html=True)

    st.subheader("_Financial literacy is defined as education and understanding of various financial areas such as personal finance, corporate finance, financial services, public finance etc. It focuses on the ability to manage personal finance matters in an efficient and effective manner, and it includes the knowledge of making appropriate decisions about personal finance such as investing, insurance, real estate, paying for college, budgeting, retirement and tax planning. (Investopedia). Financial literacy alerts individual to save money for their retirement period._")
    image = Image.open('FS.png')
    st.image(image, caption='Share Market')
def data():
    st.header("Header of Dataframe")
    st.write(df.head())
         
def fl():
    tab1, tab2, tab3, tab4  = st.tabs(["Financial Literacy", "Demographic", "Financial Perspective", "Findings"])

    with tab1:
        st.header("Financial Literacy")
        fig = px.histogram(df, y='FL', color='FL')
        st.plotly_chart(fig)
        g = df['FL']
        df1 = pd.concat([g.value_counts(),
        g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
        st.table(df1)
       
    with tab2:
        st.header("Demographic Variable")
        options=st.selectbox('select the Demographic variable', ["Gender", "Age", "Marital.Status", "Profession", "Education", "Income", "State"], key="options")
        if options == 'Gender':
            st.header("Financial Literacy Vs Gender")
            fig = px.histogram(df, y='FL', color='Gender')
            st.plotly_chart(fig)
           
            g = df.groupby('Gender')['FL']
            df1 = pd.concat([g.value_counts(),
            g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
            st.table(df1)
        elif options == 'Age':
            st.header("Financial Literacy Vs Age")
            fig = px.histogram(df, color='Age', y='FL')
            st.plotly_chart(fig)
            g = df.groupby('Age')['FL']
            df1 = pd.concat([g.value_counts(),
            g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
            st.table(df1)
        elif options == 'Marital.Status':
            st.header("Financial Literacy Vs Marital Status")
            fig = px.histogram(df, color='Marital.Status', y='FL')
            st.plotly_chart(fig)
            g = df.groupby('Marital.Status')['FL']
            df1 = pd.concat([g.value_counts(),
            g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
            st.table(df1)
        elif options == 'Profession':
            st.header("Financial Literacy Vs Profession")
            fig = px.histogram(df, color='Profession', y='FL')
            st.plotly_chart(fig)
            g = df.groupby('Profession')['FL']
            df1 = pd.concat([g.value_counts(),
            g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
            st.table(df1)
        elif options == 'Education':
            st.header("Financial Literacy Vs Education")
            fig = px.histogram(df, color='Education', y='FL')
            st.plotly_chart(fig)
            g = df.groupby('Education')['FL']
            df1 = pd.concat([g.value_counts(),
            g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
            st.table(df1)
        elif options == 'Income':
            st.header("Financial Literacy Vs Income")
            fig = px.histogram(df, color='Income', y='FL')
            st.plotly_chart(fig)
            g = df.groupby('Income')['FL']
            df1 = pd.concat([g.value_counts(),
            g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
            st.table(df1)
        elif options == 'State':
            st.header("Financial Literacy Vs State")
            fig = px.histogram(df, color='State', y='FL')
            st.plotly_chart(fig)
            g = df.groupby('State')['FL']
            df1 = pd.concat([g.value_counts(),
            g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
            st.table(df1)
    with tab3:
            st.header("Financial Perspective Vs Demographic Variable")
            options1=st.selectbox('select the Financial Perspective variable', ["Future_Perspective", "Existing_Loan", "Emergency_Fund", "EMI.Loan", "Money_Attitude", "Financial_Efficacy", "Retirement"], key="options1")
            options2=st.selectbox('select the Demographic variable', ["None", "Gender", "Age", "Marital.Status", "Profession", "Education", "Income", "State"], key="options2")
            if options1 == 'Future_Perspective' and options2 == 'None':
                st.header("Future Perspective Vs Financial Literacy")
                fig = px.histogram(df, x='FL', color='Future_Perspective')
                st.plotly_chart(fig)
                g=df[['FL', 'Future_Perspective']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
                
            if options1 == 'Future_Perspective' and options2 == 'Gender':
                st.header("Future Perspective Vs Gender")
                fig = px.histogram(df, x='FL', color='Future_Perspective', facet_col='Gender')
                st.plotly_chart(fig)
                g=df[['FL', 'Gender', 'Future_Perspective']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)


            elif options1 == 'Future_Perspective' and options2 == 'Age':
                st.header("Future perspective Vs Age")
                fig = px.histogram(df, x='FL', color='Future_Perspective', facet_col='Age')
                st.plotly_chart(fig)
                g=df[['FL', 'Age', 'Future_Perspective']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
            elif options1 == 'Future_Perspective' and options2 == 'Marital.Status':
                st.header("Future perspective Vs Marital Status")
                fig = px.histogram(df, x='FL', color='Marital.Status', facet_col='Future_Perspective')
                st.plotly_chart(fig)
                g=df[['FL', 'Marital.Status', 'Future_Perspective']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
            elif options1 == 'Future_Perspective' and options2 == 'Profession':
                st.header("Future perspective Vs Profession")
                fig = px.histogram(df, x='FL', color='Profession', facet_col='Future_Perspective')
                st.plotly_chart(fig)
                g=df[['FL', 'Profession', 'Future_Perspective']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
            elif options1 == 'Future_Perspective' and options2 == 'Education':
                st.header("Future perspective Vs Education")
                fig = px.histogram(df, x='FL', color='Education', facet_col='Future_Perspective')
                st.plotly_chart(fig)
                g=df[['FL', 'Education', 'Future_Perspective']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
            elif options1 == 'Future_Perspective' and options2 == 'Income':
                st.header("Future perspective Vs Income")
                fig = px.histogram(df, x='FL', color='Future_Perspective', facet_col='Income')
                st.plotly_chart(fig)
                g=df[['FL', 'Income', 'Future_Perspective']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
            elif options1 == 'Future_Perspective' and options2 == 'State':
                st.header("Future perspective Vs State")
                fig = px.histogram(df, x='FL', color='Future_Perspective', facet_col='State')
                st.plotly_chart(fig)
                g=df[['FL', 'State', 'Future_Perspective']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
            elif options1 == 'Existing_Loan' and options2 == 'None':
                st.header("Existing Loan Vs Financial Literacy")
                fig = px.histogram(df, x='FL', color='Existing_Loan')
                st.plotly_chart(fig)
                g=df[['FL', 'Existing_Loan']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
            elif options1 == 'Existing_Loan' and options2 == 'Gender':
                st.header("Existing Loan Vs Gender")
                fig = px.histogram(df, x='FL', color='Existing_Loan', facet_col='Gender')
                st.plotly_chart(fig)
               
                g=df[['FL', 'Gender', 'Existing_Loan']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
            elif options1 == 'Existing_Loan' and options2 == 'Age':
                st.header("Existing Loan Vs Age")
                fig = px.histogram(df, x='FL', color='Age', facet_col='Existing_Loan')
                st.plotly_chart(fig)
                g=df[['FL', 'Age', 'Existing_Loan']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
            elif options1 == 'Existing_Loan' and options2 == 'Marital.Status':
                st.header("Existing Loan Vs Marital Status")
                fig = px.histogram(df, x='FL', color='Marital.Status', facet_col='Existing_Loan')
                st.plotly_chart(fig)
                g=df[['FL', 'Marital.Status', 'Existing_Loan']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
            elif options1 == 'Existing_Loan' and options2 == 'Profession':
                st.header("Existing Loan Vs Profession")
                fig = px.histogram(df, x='FL', color='Profession', facet_col='Existing_Loan')
                st.plotly_chart(fig)
               
                g=df[['FL', 'Profession', 'Existing_Loan']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
            elif options1 == 'Existing_Loan' and options2 == 'Education':
                st.header("Existing Loan Vs Education")
                fig = px.histogram(df, x='FL', color='Education', facet_col='Existing_Loan')
                st.plotly_chart(fig)
               
                g=df[['FL', 'Education', 'Existing_Loan']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
               
            elif options1 == 'Existing_Loan' and options2 == 'Income':
                st.header("Existing Loan Vs Income")
                fig = px.histogram(df, x='FL', color='Income', facet_col='Existing_Loan')
                st.plotly_chart(fig)
               
                g=df[['FL', 'Income', 'Existing_Loan']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
            elif options1 == 'Existing_Loan' and options2 == 'State':
                st.header("Existing Loan Vs State")
                fig = px.histogram(df, x='FL', color='State', facet_col='Existing_Loan')
                st.plotly_chart(fig)
               
                g=df[['FL', 'State', 'Existing_Loan']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
            elif options1 == 'Emergency_Fund' and options2 == 'None':
                st.header("Emergency Fund Vs Financial Literacy")
                fig = px.histogram(df, x='FL', color='Emergency_Fund')
                st.plotly_chart(fig)
                g=df[['FL', 'Emergency_Fund']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)  
            elif options1 == 'Emergency_Fund' and options2 == 'Gender':
                st.header("Emergency Fund Vs Gender")
                fig = px.histogram(df, x='FL', color='Gender', facet_col='Emergency_Fund')
                st.plotly_chart(fig)
               
                g=df[['FL', 'Gender', 'Emergency_Fund']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
            elif options1 == 'Emergency_Fund' and options2 == 'Age':
                st.header("Emergency Fund Vs Age")
                fig = px.histogram(df, x='FL', color='Age', facet_col='Emergency_Fund')
                st.plotly_chart(fig)
               
                g=df[['FL', 'Age', 'Emergency_Fund']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
            elif options1 == 'Emergency_Fund' and options2 == 'Marital.Status':
                st.header("Emergency Fund Vs Marital Status")
                fig = px.histogram(df, x='FL', color='Marital.Status', facet_col='Emergency_Fund')
                st.plotly_chart(fig)
               
                g=df[['FL', 'Marital.Status', 'Emergency_Fund']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
            elif options1 == 'Emergency_Fund' and options2 == 'Profession':
                st.header("Emergency Fund Vs Profession")
                fig = px.histogram(df, x='FL', color='Profession', facet_col='Emergency_Fund')
                st.plotly_chart(fig)
               
                g=df[['FL', 'Profession', 'Emergency_Fund']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
            elif options1 == 'Emergency_Fund' and options2 == 'Education':
                st.header("Emergency Fund Vs Education")
                fig = px.histogram(df, x='FL', color='Education', facet_col='Emergency_Fund')
                st.plotly_chart(fig)
               
                g=df[['FL', 'Education', 'Emergency_Fund']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
            elif options1 == 'Emergency_Fund' and options2 == 'Income':
                st.header("Emergency Fund Vs Income")
                fig = px.histogram(df, x='FL', color='Income', facet_col='Emergency_Fund')
                st.plotly_chart(fig)
               
                g=df[['FL', 'Income', 'Emergency_Fund']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
            elif options1 == 'Emergency_Fund' and options2 == 'State':
                st.header("Emergency Fund Vs State")
                fig = px.histogram(df, x='FL', color='State', facet_col='Emergency_Fund')
                st.plotly_chart(fig)
               
                g=df[['FL', 'State', 'Emergency_Fund']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
            elif options1 == 'EMI.Loan' and options2 == 'None':
                st.header("EMI Loan Vs Financial Literacy")
                fig = px.histogram(df, x='FL', color='EMI.Loan')
                st.plotly_chart(fig)
                g=df[['FL', 'EMI.Loan']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
            elif options1 == 'EMI.Loan' and options2 == 'Gender':
                st.header("EMI Loan Vs Gender")
                fig = px.histogram(df, x='FL', color='EMI.Loan', facet_col='Gender')
                st.plotly_chart(fig)
               
                g=df[['FL', 'Gender', 'EMI.Loan']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
            elif options1 == 'EMI.Loan' and options2 == 'Age':
                st.header("EMI Loan Vs Age")
                fig = px.histogram(df, x='FL', color='EMI.Loan', facet_col='Age')
                st.plotly_chart(fig)
               
                g=df[['FL', 'Age', 'EMI.Loan']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
            elif options1 == 'EMI.Loan' and options2 == 'Marital.Status':
                st.header("EMI Loan Vs Marital Status")
                fig = px.histogram(df, x='FL', color='Marital.Status', facet_col='EMI.Loan')
                st.plotly_chart(fig)
               
                g=df[['FL', 'Marital.Status', 'EMI.Loan']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
               
            elif options1 == 'EMI.Loan' and options2 == 'Profession':
                st.header("EMI Loan Vs Profession")
                fig = px.histogram(df, x='FL', color='Profession', facet_col='EMI.Loan')
                st.plotly_chart(fig)
               
                g=df[['FL', 'Profession', 'EMI.Loan']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
               
            elif options1 == 'EMI.Loan' and options2 == 'Education':
                st.header("EMI Loan Vs Education")
                fig = px.histogram(df, x='FL', color='Education', facet_col='EMI.Loan')
                st.plotly_chart(fig)
               
                g=df[['FL', 'Education', 'EMI.Loan']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
            elif options1 == 'EMI.Loan' and options2 == 'Income':
                st.header("EMI Loan Vs Income")
                fig = px.histogram(df, x='FL', color='EMI.Loan', facet_col='Income')
                st.plotly_chart(fig)
               
                g=df[['FL', 'Income', 'EMI.Loan']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
            elif options1 == 'EMI.Loan' and options2 == 'State':
                st.header("EMI Loan Vs State")
                fig = px.histogram(df, x='FL', color='State', facet_col='EMI.Loan')
                st.plotly_chart(fig)
               
                g=df[['FL', 'State', 'EMI.Loan']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
            elif options1 == 'Money_Attitude' and options2 == 'None':
                st.header("Money Attitude Vs Financial Literacy")
                fig = px.histogram(df, x='FL', color='Money_Attitude')
                st.plotly_chart(fig)
                g=df[['FL', 'Money_Attitude']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
            elif options1 == 'Money_Attitude' and options2 == 'Gender':
                st.header("Money Attitude Vs Gender")
                fig = px.histogram(df, x='FL', color='Money_Attitude', facet_col='Gender')
                st.plotly_chart(fig)
               
                g=df[['FL', 'Gender', 'Money_Attitude']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
               
            elif options1 == 'Money_Attitude' and options2 == 'Age':
                st.header("Money Attitude Vs Age")
                fig = px.histogram(df, x='FL', color='Age', facet_col='Money_Attitude')
                st.plotly_chart(fig)
               
                g=df[['FL', 'Age', 'Money_Attitude']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
            elif options1 == 'Money_Attitude' and options2 == 'Marital.Status':
                st.header("Money Attitude Vs Marital Status")
                fig = px.histogram(df, x='FL', color='Marital.Status', facet_col='Money_Attitude')
                st.plotly_chart(fig)
               
                g=df[['FL', 'Marital.Status', 'Money_Attitude']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
            elif options1 == 'Money_Attitude' and options2 == 'Profession':
                st.header("Money Attitude Vs Profession")
                fig = px.histogram(df, x='FL', color='Profession', facet_col='Money_Attitude')
                st.plotly_chart(fig)
               
                g=df[['FL', 'Profession', 'Money_Attitude']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
            elif options1 == 'Money_Attitude' and options2 == 'Education':
                st.header("Money Attitude Vs Education")
                fig = px.histogram(df, x='FL', color='Education', facet_col='Money_Attitude')
                st.plotly_chart(fig)
               
                g=df[['FL', 'Education', 'Money_Attitude']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
            elif options1 == 'Money_Attitude' and options2 == 'Income':
                st.header("Money Attitude Vs Income")
                fig = px.histogram(df, x='FL', color='Money_Attitude', facet_col='Income')
                st.plotly_chart(fig)
               
                g=df[['FL', 'Income', 'Money_Attitude']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
            elif options1 == 'Money_Attitude' and options2 == 'State':
                st.header("Money Attitude Vs State")
                fig = px.histogram(df, x='FL', color='State', facet_col='Money_Attitude')
                st.plotly_chart(fig)
               
                g=df[['FL', 'State', 'Money_Attitude']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
            elif options1 == 'Financial_Efficacy' and options2 == 'None':
                st.header("Financial_Efficacy Vs Financial Literacy")
                fig = px.histogram(df, x='FL', color='Financial_Efficacy')
                st.plotly_chart(fig)
                g=df[['FL', 'Financial_Efficacy']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
            elif options1 == 'Financial_Efficacy' and options2 == 'Gender':
                st.header("Financial Efficacy Vs Gender")
                fig = px.histogram(df, x='FL', color='Financial_Efficacy', facet_col='Gender')
                st.plotly_chart(fig)
               
                g=df[['FL', 'Gender', 'Financial_Efficacy']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
            elif options1 == 'Financial_Efficacy' and options2 == 'Age':
                st.header("Financial Efficacy Vs Age")
                fig = px.histogram(df, x='FL', color='Age', facet_col='Financial_Efficacy')
                st.plotly_chart(fig)
               
                g=df[['FL', 'Age', 'Financial_Efficacy']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
            elif options1 == 'Financial_Efficacy' and options2 == 'Marital.Status':
                st.header("Financial Efficacy Vs Marital Status")
                fig = px.histogram(df, x='FL', color='Marital.Status', facet_col='Financial_Efficacy')
                st.plotly_chart(fig)
               
                g=df[['FL', 'Marital.Status', 'Financial_Efficacy']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
            elif options1 == 'Financial_Efficacy' and options2 == 'Profession':
                st.header("Financial Efficacy Vs Profession")
                fig = px.histogram(df, x='FL', color='Profession', facet_col='Financial_Efficacy')
                st.plotly_chart(fig)
               
                g=df[['FL', 'Profession', 'Financial_Efficacy']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
            elif options1 == 'Financial_Efficacy' and options2 == 'Education':
                st.header("Financial Efficacy Vs Education")
                fig = px.histogram(df, x='FL', color='Education', facet_col='Financial_Efficacy')
                st.plotly_chart(fig)
               
                g=df[['FL', 'Education', 'Financial_Efficacy']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
            elif options1 == 'Financial_Efficacy' and options2 == 'Income':
                st.header("Financial Efficacy Vs Income")
                fig = px.histogram(df, x='FL', color='Financial_Efficacy', facet_col='Income')
                st.plotly_chart(fig)
               
                g=df[['FL', 'Income', 'Financial_Efficacy']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
            elif options1 == 'Financial_Efficacy' and options2 == 'State':
                st.header("Financial Efficacy Vs State")
                fig = px.histogram(df, x='FL', color='State', facet_col='Financial_Efficacy')
                st.plotly_chart(fig)
               
                g=df[['FL', 'State', 'Financial_Efficacy']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
            elif options1 == 'Retirement' and options2 == 'None':
                st.header("Retirement Vs Financial Literacy")
                fig = px.histogram(df, x='FL', color='Retirement')
                st.plotly_chart(fig)
                g=df[['FL', 'Retirement']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
            elif options1 == 'Retirement' and options2 == 'Gender':
                st.header("Retirement Vs Gender")
                fig = px.histogram(df, x='FL', color='Retirement', facet_col='Gender')
                st.plotly_chart(fig)
               
                g=df[['FL', 'Gender', 'Retirement']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
            elif options1 == 'Retirement' and options2 == 'Age':
                st.header("Retirement Vs Age")
                fig = px.histogram(df, x='FL', color='Age', facet_col='Retirement')
                st.plotly_chart(fig)
               
                g=df[['FL', 'Age', 'Retirement']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
            elif options1 == 'Retirement' and options2 == 'Marital.Status':
                st.header("Retirement Vs Marital Status")
                fig = px.histogram(df, x='FL', color='Marital.Status', facet_col='Retirement')
                st.plotly_chart(fig)
               
                g=df[['FL', 'Marital.Status', 'Retirement']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
            elif options1 == 'Retirement' and options2 == 'Profession':
                st.header("Retirement Vs Profession")
                fig = px.histogram(df, x='FL', color='Profession', facet_col='Retirement')
                st.plotly_chart(fig)
               
                g=df[['FL', 'Profession', 'Retirement']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
            elif options1 == 'Retirement' and options2 == 'Education':
                st.header("Retirement Vs Education")
                fig = px.histogram(df, x='FL', color='Education', facet_col='Retirement')
                st.plotly_chart(fig)
               
                g=df[['FL', 'Education', 'Retirement']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
            elif options1 == 'Retirement' and options2 == 'Income':
                st.header("Retirement Vs Income")
                fig = px.histogram(df, x='FL', color='Retirement', facet_col='Income')
                st.plotly_chart(fig)
               
                g=df[['FL', 'Income', 'Retirement']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
            elif options1 == 'Retirement' and options2 == 'State':
                st.header("Retirement Vs State")
                fig = px.histogram(df, x='FL', color='State', facet_col='Retirement')
                st.plotly_chart(fig)
               
                g=df[['FL', 'State', 'Retirement']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
    with tab4:
        st.subheader("*In general majority of the people believe they have good financial knowledge.")
        st.subheader("*By observing the given data we can notice that more number of females claim to have slightly better or average financial knowledge compare to males.")
        st.subheader("*With regards to profession students tend to have better financial knowledge when compared to other professions.")
        st.subheader("*In the education catagory University students who claim to have good financial knowledge are higher in count than the rest.")
        st.subheader("*In terms of location Tamil Nadu has recorded highest number of survey responses.")
        st.subheader("*The data shows that higher number of females tend to allot 0-25% of their income for their future.")
        st.subheader("*The plot shows that majority of the people with good/average financial knowledge do not have any existing loans.")
        st.subheader("*Unusually people who seem to have good/average financial knowledge do not necessarily have any emergency fund.")
        st.subheader("*Survey participants who have good financial understanding generally avoid paying/getting into EMI/Loan.")
        st.subheader("*The data collection shows that when it comes to handling finances the common perception among people is neutral.")
        st.subheader("*Peoples perception when it comes to saving money to buy something special is not very different as they tend to both agree/disagree.")
        st.subheader("*The survey participants who believe to have average financial knowledge seems to have neutral opinion when it comes to saving money for retirement.")

def sm():
    tab1, tab2, tab3, tab4  = st.tabs(["Share Market", "Demographic", "Stock Perspective", "Findings"])

    with tab1:
        st.header("Share Market")
        fig = px.histogram(df, y='SMI', color='SMI')
        st.plotly_chart(fig)
        g = df['SMI']
        df1 = pd.concat([g.value_counts(),
        g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
        st.table(df1)
       
    with tab2:
        st.header("Demographic Variable")
        options3=st.selectbox('select the Demographic variable', ["Gender", "Age", "Marital.Status", "Profession", "Education", "Income", "State"], key="options3")
        if options3 == 'Gender':
            st.header("Share Market Vs Gender")
            fig = px.histogram(df, color='Gender', y='SMI')
            st.plotly_chart(fig)
           
            g = df.groupby('Gender')['SMI']
            df1 = pd.concat([g.value_counts(),
            g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
            st.table(df1)
           
        elif options3 == 'Age':
            st.header("Share Market Vs Age")
            fig = px.histogram(df, color='Age', y='SMI')
            st.plotly_chart(fig)
           
            g = df.groupby('Age')['SMI']
            df1 = pd.concat([g.value_counts(),
            g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
            st.table(df1)
           
        elif options3 == 'Marital.Status':
            st.header("Share Market Vs Marital Status")
            fig = px.histogram(df, color='Marital.Status', y='SMI')
            st.plotly_chart(fig)
           
            g = df.groupby('Marital.Status')['SMI']
            df1 = pd.concat([g.value_counts(),
            g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
            st.table(df1)
           
           
        elif options3 == 'Profession':
            st.header("Share Market Vs Profession")
            fig = px.histogram(df, color='Profession', y='SMI')
            st.plotly_chart(fig)
           
            g = df.groupby('Profession')['SMI']
            df1 = pd.concat([g.value_counts(),
            g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
            st.table(df1)
           
        elif options3 == 'Education':
            st.header("Share Market Vs Education")
            fig = px.histogram(df, color='Education', y='SMI')
            st.plotly_chart(fig)
           
            g = df.groupby('Education')['SMI']
            df1 = pd.concat([g.value_counts(),
            g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
            st.table(df1)
           
           
        elif options3 == 'Income':
            st.header("Share Market Vs Income")
            fig = px.histogram(df, color='Income', y='SMI')
            st.plotly_chart(fig)
           
            g = df.groupby('Income')['SMI']
            df1 = pd.concat([g.value_counts(),
            g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
            st.table(df1)
           
        elif options3 == 'State':
            st.header("Share Market Vs State")
            fig = px.histogram(df, color='State', y='SMI')
            st.plotly_chart(fig)
           
            g = df.groupby('State')['SMI']
            df1 = pd.concat([g.value_counts(),
            g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
            st.table(df1)
           
    with tab3:
        st.header("Stock Perspective Vs Demographic Variables")
        options4=st.selectbox('select the Stock Perspective variable', ["Inv_involved", "Inv_Type", "KSM", "Inv_Motive", "Inv_pattern", "Equity_Market", "Demat_Account", "Stock_opinion", "Inv_Advice", "Learning_inv", "Inv_plan", "Covid_SM"], key="options4")
        options5=st.selectbox('select the Demographic variable', ["None", "Gender", "Age", "Marital.Status", "Profession", "Education", "Income", "State"], key="options5")
        if options4 == 'Inv_involved' and options5 == 'None':
                st.header("Investment involved Vs Share Market Interest")
                fig = px.histogram(df, x='SMI', color='Inv_involved')
                st.plotly_chart(fig)
                g=df[['SMI', 'Inv_involved']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
        elif options4 == 'Inv_involved' and options5 == 'Gender':
                st.header("Investment involved Vs Gender")
                fig = px.histogram(df, x='SMI', color='Inv_involved', facet_col='Gender')
                st.plotly_chart(fig)
               
                g=df[['SMI', 'Gender', 'Inv_involved']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
        elif options4 == 'Inv_involved' and options5 == 'Age':
                st.header("Investment involved Vs Age")
                fig = px.histogram(df, x='SMI', color='Age', facet_col='Inv_involved')
                st.plotly_chart(fig)
               
                g=df[['SMI', 'Age', 'Inv_involved']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
        elif options4 == 'Inv_involved' and options5 == 'Marital.Status':
                st.header("Investment involved Vs Marital Status")
                fig = px.histogram(df, x='SMI', color='Marital.Status', facet_col='Inv_involved')
                st.plotly_chart(fig)
               
                g=df[['SMI', 'Marital.Status', 'Inv_involved']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
        elif options4 == 'Inv_involved' and options5 == 'Profession':
                st.header("Investment involved Vs Profession")
                fig = px.histogram(df, x='SMI', color='Profession', facet_col='Inv_involved')
                st.plotly_chart(fig)
               
                g=df[['SMI', 'Profession', 'Inv_involved']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
        elif options4 == 'Inv_involved' and options5 == 'Education':
                st.header("Investment involved Vs Education")
                fig = px.histogram(df, x='SMI', color='Education', facet_col='Inv_involved')
                st.plotly_chart(fig)
               
                g=df[['SMI', 'Education', 'Inv_involved']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
        elif options4 == 'Inv_involved' and options5 == 'Income':
                st.header("Investment involved Vs Income")
                fig = px.histogram(df, x='SMI', color='Income', facet_col='Inv_involved')
                st.plotly_chart(fig)
               
                g=df[['SMI', 'Income', 'Inv_involved']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
        elif options4 == 'Inv_involved' and options5 == 'State':
                st.header("Investment involved Vs State")
                fig = px.histogram(df, x='SMI', color='State', facet_col='Inv_involved')
                st.plotly_chart(fig)
               
                g=df[['SMI', 'State', 'Inv_involved']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
        elif options4 == 'Inv_Type' and options5 == 'None':
                st.header("Investment Type Vs Share Market Interest")
                fig = px.histogram(df, x='SMI', color='Inv_Type')
                st.plotly_chart(fig)
                g=df[['SMI', 'Inv_Type']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
        elif options4 == 'Inv_Type' and options5 == 'Gender':
                st.header("Investment Type Vs Gender")
                fig = px.histogram(df, x='SMI', color='Inv_Type', facet_col='Gender')
                st.plotly_chart(fig)
               
                g=df[['SMI', 'Gender', 'Inv_Type']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
        elif options4 == 'Inv_Type' and options5 == 'Age':
                st.header("Investment Type Vs Age")
                fig = px.histogram(df, x='SMI', color='Inv_Type', facet_col='Age')
                st.plotly_chart(fig)
               
                g=df[['SMI', 'Age', 'Inv_Type']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
        elif options4 == 'Inv_Type' and options5 == 'Marital.Status':
                st.header("Investment Type Vs Marital Status")
                fig = px.histogram(df, x='SMI', color='Inv_Type', facet_col='Marital.Status')
                st.plotly_chart(fig)
               
                g=df[['SMI', 'Marital.Status', 'Inv_Type']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
        elif options4 == 'Inv_Type' and options5 == 'Profession':
                st.header("Investment Type Vs Profession")
                fig = px.histogram(df, x='SMI', color='Profession', facet_col='Inv_Type')
                st.plotly_chart(fig)
               
                g=df[['SMI', 'Profession', 'Inv_Type']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
        elif options4 == 'Inv_Type' and options5 == 'Education':
                st.header("Investment Type Vs Education")
                fig = px.histogram(df, x='SMI', color='Education', facet_col='Inv_Type')
                st.plotly_chart(fig)
               
                g=df[['SMI', 'Education', 'Inv_Type']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
        elif options4 == 'Inv_Type' and options5 == 'Income':
                st.header("Investment Type Vs Income")
                fig = px.histogram(df, x='SMI', color='Inv_Type', facet_col='Income')
                st.plotly_chart(fig)
               
                g=df[['SMI', 'Income', 'Inv_Type']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
        elif options4 == 'Inv_Type' and options5 == 'State':
                st.header("Investment Type Vs State")
                fig = px.histogram(df, x='SMI', color='Inv_Type', facet_col='State')
                st.plotly_chart(fig)
               
                g=df[['SMI', 'State', 'Inv_Type']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
        elif options4 == 'KSM' and options5 == 'None':
                st.header("Knowledge about Stock Market Vs Share Market Interest")
                fig = px.histogram(df, x='SMI', color='KSM')
                st.plotly_chart(fig)
                g=df[['SMI', 'KSM']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
        elif options4 == 'KSM' and options5 == 'Gender':
                st.header("Knowledge about Stock Market Vs Gender")
                fig = px.histogram(df, x='SMI', color='KSM', facet_col='Gender')
                st.plotly_chart(fig)
               
                g=df[['SMI', 'Gender', 'KSM']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
        elif options4 == 'KSM' and options5 == 'Age':
                st.header("Knowledge about Stock Market Vs Age")
                fig = px.histogram(df, x='SMI', color='Age', facet_col='KSM')
                st.plotly_chart(fig)
               
                g=df[['SMI', 'Age', 'KSM']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
        elif options4 == 'KSM' and options5 == 'Marital.Status':
                st.header("Knowledge about Stock Market Vs Marital Status")
                fig = px.histogram(df, x='SMI', color='Marital.Status', facet_col='KSM')
                st.plotly_chart(fig)
               
                g=df[['SMI', 'Marital.Status', 'KSM']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
        elif options4 == 'KSM' and options5 == 'Profession':
                st.header("Knowledge about Stock Market Vs Profession")
                fig = px.histogram(df, x='SMI', color='Profession', facet_col='KSM')
                st.plotly_chart(fig)
               
                g=df[['SMI', 'Profession', 'KSM']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
        elif options4 == 'KSM' and options5 == 'Education':
                st.header("Knowledge about Stock Market Vs Education")
                fig = px.histogram(df, x='SMI', color='Education', facet_col='KSM')
                st.plotly_chart(fig)
               
                g=df[['SMI', 'Education', 'KSM']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
        elif options4 == 'KSM' and options5 == 'Income':
                st.header("Knowledge about Stock Market Vs Income")
                fig = px.histogram(df, x='SMI', color='Income', facet_col='KSM')
                st.plotly_chart(fig)
               
                g=df[['SMI', 'Income', 'KSM']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
        elif options4 == 'KSM' and options5 == 'State':
                st.header("Knowledge about Stock Market Vs State")
                fig = px.histogram(df, x='SMI', color='State', facet_col='KSM')
                st.plotly_chart(fig)
               
                g=df[['SMI', 'State', 'KSM']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
        elif options4 == 'Inv_Motive' and options5 == 'None':
                st.header("Investment Motive Vs Share Market Interest")
                fig = px.histogram(df, x='SMI', color='Inv_Motive')
                st.plotly_chart(fig)
                g=df[['SMI', 'Inv_Motive']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)   
        elif options4 == 'Inv_Motive' and options5 == 'Gender':
                st.header("Investment Motive Vs Gender")
                fig = px.histogram(df, x='SMI', color='Inv_Motive', facet_col='Gender')
                st.plotly_chart(fig)
               
                g=df[['SMI', 'Gender', 'Inv_Motive']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
        elif options4 == 'Inv_Motive' and options5 == 'Age':
                st.header("Investment Motive Vs Age")
                fig = px.histogram(df, x='SMI', color='Inv_Motive', facet_col='Age')
                st.plotly_chart(fig)
               
                g=df[['SMI', 'Age', 'Inv_Motive']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
        elif options4 == 'Inv_Motive' and options5 == 'Marital.Status':
                st.header("Investment Motive Vs Marital Status")
                fig = px.histogram(df, x='SMI', color='Inv_Motive', facet_col='Marital.Status')
                st.plotly_chart(fig)
               
                g=df[['SMI', 'Marital.Status', 'Inv_Motive']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
        elif options4 == 'Inv_Motive' and options5 == 'Profession':
                st.header("Investment Motive Vs Profession")
                fig = px.histogram(df, x='SMI', color='Profession', facet_col='Inv_Motive')
                st.plotly_chart(fig)
               
                g=df[['SMI', 'Profession', 'Inv_Motive']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
        elif options4 == 'Inv_Motive' and options5 == 'Education':
                st.header("Investment Motive Vs Education")
                fig = px.histogram(df, x='SMI', color='Education', facet_col='Inv_Motive')
                st.plotly_chart(fig)
               
                g=df[['SMI', 'Education', 'Inv_Motive']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
        elif options4 == 'Inv_Motive' and options5 == 'Income':
                st.header("Investment Motive Vs Income")
                fig = px.histogram(df, x='SMI', color='Inv_Motive', facet_col='Income')
                st.plotly_chart(fig)
               
                g=df[['SMI', 'Income', 'Inv_Motive']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
        elif options4 == 'Inv_Motive' and options5 == 'State':
                st.header("Investment Motive Vs State")
                fig = px.histogram(df, x='SMI', color='State', facet_col='Inv_Motive')
                st.plotly_chart(fig)
               
                g=df[['SMI', 'State', 'Inv_Motive']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
        elif options4 == 'Inv_pattern' and options5 == 'None':
                st.header("Investment Pattern Vs Share Market Interest")
                fig = px.histogram(df, x='SMI', color='Inv_pattern')
                st.plotly_chart(fig)
                g=df[['SMI', 'Inv_pattern']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
        elif options4 == 'Inv_pattern' and options5 == 'Gender':
                st.header("Investment Pattern Vs Gender")
                fig = px.histogram(df, x='SMI', color='Gender', facet_col='Inv_pattern')
                st.plotly_chart(fig)
               
                g=df[['SMI', 'Gender', 'Inv_pattern']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
        elif options4 == 'Inv_pattern' and options5 == 'Age':
                st.header("Investment Pattern Vs Age")
                fig = px.histogram(df, x='SMI', color='Age', facet_col='Inv_pattern')
                st.plotly_chart(fig)
               
                g=df[['SMI', 'Age', 'Inv_pattern']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
        elif options4 == 'Inv_pattern' and options5 == 'Marital.Status':
                st.header("Investment Pattern Vs Marital Status")
                fig = px.histogram(df, x='SMI', color='Marital.Status', facet_col='Inv_pattern')
                st.plotly_chart(fig)
               
                g=df[['SMI', 'Marital.Status', 'Inv_pattern']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
        elif options4 == 'Inv_pattern' and options5 == 'Profession':
                st.header("Investment Pattern Vs Profession")
                fig = px.histogram(df, x='SMI', color='Profession', facet_col='Inv_pattern')
                st.plotly_chart(fig)
               
                g=df[['SMI', 'Profession', 'Inv_pattern']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
        elif options4 == 'Inv_pattern' and options5 == 'Education':
                st.header("Investment Pattern Vs Education")
                fig = px.histogram(df, x='SMI', color='Education', facet_col='Inv_pattern')
                st.plotly_chart(fig)
               
                g=df[['SMI', 'Education', 'Inv_pattern']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
        elif options4 == 'Inv_pattern' and options5 == 'Income':
                st.header("Investment Pattern Vs Income")
                fig = px.histogram(df, x='SMI', color='Income', facet_col='Inv_pattern')
                st.plotly_chart(fig)
               
                g=df[['SMI', 'Income', 'Inv_pattern']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
        elif options4 == 'Inv_pattern' and options5 == 'State':
                st.header("Investment Pattern Vs State")
                fig = px.histogram(df, x='SMI', color='State', facet_col='Inv_pattern')
                st.plotly_chart(fig)
               
                g=df[['SMI', 'State', 'Inv_pattern']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
        elif options4 == 'Equity_Market' and options5 == 'None':
                st.header("Equity Market Vs Share Market Interest")
                fig = px.histogram(df, x='SMI', color='Equity_Market')
                st.plotly_chart(fig)
                g=df[['SMI', 'Equity_Market']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
        elif options4 == 'Equity_Market' and options5 == 'Gender':
                st.header("Equity Market Vs Gender")
                fig = px.histogram(df, x='SMI', color='Equity_Market', facet_col='Gender')
                st.plotly_chart(fig)
               
                g=df[['SMI', 'Gender', 'Equity_Market']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
        elif options4 == 'Equity_Market' and options5 == 'Age':
                st.header("Equity Market Vs Age")
                fig = px.histogram(df, x='SMI', color='Age', facet_col='Equity_Market')
                st.plotly_chart(fig)
               
                g=df[['SMI', 'Age', 'Equity_Market']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
        elif options4 == 'Equity_Market' and options5 == 'Marital.Status':
                st.header("Equity Market Vs Marital Status")
                fig = px.histogram(df, x='SMI', color='Marital.Status', facet_col='Equity_Market')
                st.plotly_chart(fig)
               
                g=df[['SMI', 'Marital.Status', 'Equity_Market']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
        elif options4 == 'Equity_Market' and options5 == 'Profession':
                st.header("Equity Market Vs Profession")
                fig = px.histogram(df, x='SMI', color='Profession', facet_col='Equity_Market')
                st.plotly_chart(fig)
               
                g=df[['SMI', 'Profession', 'Equity_Market']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
        elif options4 == 'Equity_Market' and options5 == 'Education':
                st.header("Equity Market Vs Education")
                fig = px.histogram(df, x='SMI', color='Education', facet_col='Equity_Market')
                st.plotly_chart(fig)
               
                g=df[['SMI', 'Education', 'Equity_Market']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
        elif options4 == 'Equity_Market' and options5 == 'Income':
                st.header("Equity Market Vs Income")
                fig = px.histogram(df, x='SMI', color='Income', facet_col='Equity_Market')
                st.plotly_chart(fig)
               
                g=df[['SMI', 'Income', 'Equity_Market']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
        elif options4 == 'Equity_Market' and options5 == 'State':
                st.header("Equity Market Vs State")
                fig = px.histogram(df, x='SMI', color='State', facet_col='Equity_Market')
                st.plotly_chart(fig)
               
                g=df[['SMI', 'State', 'Equity_Market']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
        elif options4 == 'Demat_Account' and options5 == 'None':
                st.header("Demat Account Vs Share Market Interest")
                fig = px.histogram(df, x='SMI', color='Demat_Account')
                st.plotly_chart(fig)
                g=df[['SMI', 'Demat_Account']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
        elif options4 == 'Demat_Account' and options5 == 'Gender':
                st.header("Demat Account Vs Gender")
                fig = px.histogram(df, x='SMI', color='Gender', facet_col='Demat_Account')
                st.plotly_chart(fig)
               
                g=df[['SMI', 'Gender', 'Demat_Account']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
        elif options4 == 'Demat_Account' and options5 == 'Age':
                st.header("Demat Account Vs Age")
                fig = px.histogram(df, x='SMI', color='Age', facet_col='Demat_Account')
                st.plotly_chart(fig)
               
                g=df[['SMI', 'Age', 'Demat_Account']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
        elif options4 == 'Demat_Account' and options5 == 'Marital.Status':
                st.header("Demat Account Vs Marital Status")
                fig = px.histogram(df, x='SMI', color='Marital.Status', facet_col='Demat_Account')
                st.plotly_chart(fig)
               
                g=df[['SMI', 'Marital.Status', 'Demat_Account']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
        elif options4 == 'Demat_Account' and options5 == 'Profession':
                st.header("Demat Account Vs Profession")
                fig = px.histogram(df, x='SMI', color='Profession', facet_col='Demat_Account')
                st.plotly_chart(fig)
               
                g=df[['SMI', 'Profession', 'Demat_Account']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
        elif options4 == 'Demat_Account' and options5 == 'Education':
                st.header("Demat Account Vs Education")
                fig = px.histogram(df, x='SMI', color='Education', facet_col='Demat_Account')
                st.plotly_chart(fig)
               
                g=df[['SMI', 'Education', 'Demat_Account']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
        elif options4 == 'Demat_Account' and options5 == 'Income':
                st.header("Demat Account Vs Income")
                fig = px.histogram(df, x='SMI', color='Income', facet_col='Demat_Account')
                st.plotly_chart(fig)
               
                g=df[['SMI', 'Income', 'Demat_Account']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
        elif options4 == 'Demat_Account' and options5 == 'State':
                st.header("Demat Account Vs State")
                fig = px.histogram(df, x='SMI', color='State', facet_col='Demat_Account')
                st.plotly_chart(fig)
               
                g=df[['SMI', 'State', 'Demat_Account']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
        elif options4 == 'Stock_opinion' and options5 == 'None':
                st.header("Stock opinion Vs Share Market Interest")
                fig = px.histogram(df, x='SMI', color='Stock_opinion')
                st.plotly_chart(fig)
                g=df[['SMI', 'Stock_opinion']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
        elif options4 == 'Stock_opinion' and options5 == 'Gender':
                st.header("Stock opinion Vs Gender")
                fig = px.histogram(df, x='SMI', color='Stock_opinion', facet_col='Gender')
                st.plotly_chart(fig)
               
                g=df[['SMI', 'Gender', 'Stock_opinion']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
        elif options4 == 'Stock_opinion' and options5 == 'Age':
                st.header("Stock opinion Vs Age")
                fig = px.histogram(df, x='SMI', color='Stock_opinion', facet_col='Age')
                st.plotly_chart(fig)
               
                g=df[['SMI', 'Age', 'Stock_opinion']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
        elif options4 == 'Stock_opinion' and options5 == 'Marital.Status':
                st.header("Stock opinion Vs Marital Status")
                fig = px.histogram(df, x='SMI', color='Marital.Status', facet_col='Stock_opinion')
                st.plotly_chart(fig)
               
                g=df[['SMI', 'Marital.Status', 'Stock_opinion']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
        elif options4 == 'Stock_opinion' and options5 == 'Profession':
                st.header("Stock opinion Vs Profession")
                fig = px.histogram(df, x='SMI', color='Profession', facet_col='Stock_opinion')
                st.plotly_chart(fig)
               
                g=df[['SMI', 'Profession', 'Stock_opinion']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
        elif options4 == 'Stock_opinion' and options5 == 'Education':
                st.header("Stock opinion Vs Education")
                fig = px.histogram(df, x='SMI', color='Education', facet_col='Stock_opinion')
                st.plotly_chart(fig)
               
                g=df[['SMI', 'Education', 'Stock_opinion']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
        elif options4 == 'Stock_opinion' and options5 == 'Income':
                st.header("Stock opinion Vs Income")
                fig = px.histogram(df, x='SMI', color='Stock_opinion', facet_col='Income')
                st.plotly_chart(fig)
               
                g=df[['SMI', 'Income', 'Stock_opinion']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
        elif options4 == 'Stock_opinion' and options5 == 'State':
                st.header("Stock opinion Vs State")
                fig = px.histogram(df, x='SMI', color='State', facet_col='Stock_opinion')
                st.plotly_chart(fig)
               
                g=df[['SMI', 'State', 'Stock_opinion']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
        elif options4 == 'Inv_Advice' and options5 == 'None':
                st.header("Investment Advice Vs Share Market Interest")
                fig = px.histogram(df, x='SMI', color='Inv_Advice')
                st.plotly_chart(fig)
                g=df[['SMI', 'Inv_Advice']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
        elif options4 == 'Inv_Advice' and options5 == 'Gender':
                st.header("Investment Advice Vs Gender")
                fig = px.histogram(df, x='SMI', color='Inv_Advice', facet_col='Gender')
                st.plotly_chart(fig)
               
                g=df[['SMI', 'Gender', 'Inv_Advice']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
        elif options4 == 'Inv_Advice' and options5 == 'Age':
                st.header("Investment Advice Vs Age")
                fig = px.histogram(df, x='SMI', color='Age', facet_col='Inv_Advice')
                st.plotly_chart(fig)
               
                g=df[['SMI', 'Age', 'Inv_Advice']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
        elif options4 == 'Inv_Advice' and options5 == 'Marital.Status':
                st.header("Investment Advice Vs Marital Status")
                fig = px.histogram(df, x='SMI', color='Marital.Status', facet_col='Inv_Advice')
                st.plotly_chart(fig)
               
                g=df[['SMI', 'Marital.Status', 'Inv_Advice']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
        elif options4 == 'Inv_Advice' and options5 == 'Profession':
                st.header("Investment Advice Vs Profession")
                fig = px.histogram(df, x='SMI', color='Profession', facet_col='Inv_Advice')
                st.plotly_chart(fig)
               
                g=df[['SMI', 'Profession', 'Inv_Advice']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
        elif options4 == 'Inv_Advice' and options5 == 'Education':
                st.header("Investment Advice Vs Education")
                fig = px.histogram(df, x='SMI', color='Education', facet_col='Inv_Advice')
                st.plotly_chart(fig)
               
                g=df[['SMI', 'Education', 'Inv_Advice']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
        elif options4 == 'Inv_Advice' and options5 == 'Income':
                st.header("Investment Advice Vs Income")
                fig = px.histogram(df, x='SMI', color='Inv_Advice', facet_col='Income')
                st.plotly_chart(fig)
               
                g=df[['SMI', 'Income', 'Inv_Advice']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
               
               
        elif options4 == 'Inv_Advice' and options5 == 'State':
                st.header("Investment Advice Vs State")
                fig = px.histogram(df, x='SMI', color='State', facet_col='Inv_Advice')
                st.plotly_chart(fig)
               
                g=df[['SMI', 'State', 'Inv_Advice']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
        elif options4 == 'Learning_inv' and options5 == 'None':
                st.header("Learning about Investment Vs Share Market Interest")
                fig = px.histogram(df, x='SMI', color='Learning_inv')
                st.plotly_chart(fig)
                g=df[['SMI', 'Learning_inv']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
        elif options4 == 'Learning_inv' and options5 == 'Gender':
                st.header("Learning about Investment Vs Gender")
                fig = px.histogram(df, x='SMI', color='Gender', facet_col='Learning_inv')
                st.plotly_chart(fig)
               
                g=df[['SMI', 'Gender', 'Learning_inv']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
               
        elif options4 == 'Learning_inv' and options5 == 'Age':
                st.header("Learning about Investment Vs Age")
                fig = px.histogram(df, x='SMI', color='Age', facet_col='Learning_inv')
                st.plotly_chart(fig)
               
                g=df[['SMI', 'Age', 'Learning_inv']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
        elif options4 == 'Learning_inv' and options5 == 'Marital.Status':
                st.header("Learning about Investment Vs Marital Status")
                fig = px.histogram(df, x='SMI', color='Marital.Status', facet_col='Learning_inv')
                st.plotly_chart(fig)
               
                g=df[['SMI', 'Marital.Status', 'Learning_inv']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
        elif options4 == 'Learning_inv' and options5 == 'Profession':
                st.header("Learning about Investment Vs Profession")
                fig = px.histogram(df, x='SMI', color='Profession', facet_col='Learning_inv')
                st.plotly_chart(fig)
               
                g=df[['SMI', 'Profession', 'Learning_inv']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
        elif options4 == 'Learning_inv' and options5 == 'Education':
                st.header("Learning about Investment Vs Education")
                fig = px.histogram(df, x='SMI', color='Education', facet_col='Learning_inv')
                st.plotly_chart(fig)
               
                g=df[['SMI', 'Education', 'Learning_inv']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
        elif options4 == 'Learning_inv' and options5 == 'Income':
                st.header("Learning about Investment Vs Income")
                fig = px.histogram(df, x='SMI', color='Income', facet_col='Learning_inv')
                st.plotly_chart(fig)
               
                g=df[['SMI', 'Income', 'Learning_inv']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
        elif options4 == 'Learning_inv' and options5 == 'State':
                st.header("Learning about Investment Vs State")
                fig = px.histogram(df, x='SMI', color='State', facet_col='Learning_inv')
                st.plotly_chart(fig)
               
                g=df[['SMI', 'State', 'Learning_inv']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
        elif options4 == 'Inv_plan' and options5 == 'None':
                st.header("Investment plan Vs Share Market Interest")
                fig = px.histogram(df, x='SMI', color='Inv_plan')
                st.plotly_chart(fig)
                g=df[['SMI', 'Inv_plan']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
        elif options4 == 'Inv_plan' and options5 == 'Gender':
                st.header("Investment plan Vs Gender")
                fig = px.histogram(df, x='SMI', color='Inv_plan', facet_col='Gender')
                st.plotly_chart(fig)
               
                g=df[['SMI', 'Gender', 'Inv_plan']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
        elif options4 == 'Inv_plan' and options5 == 'Age':
                st.header("Investment plan Vs Age")
                fig = px.histogram(df, x='SMI', color='Inv_plan', facet_col='Age')
                st.plotly_chart(fig)
               
                g=df[['SMI', 'Age', 'Inv_plan']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
        elif options4 == 'Inv_plan' and options5 == 'Marital.Status':
                st.header("Investment plan Vs Marital Status")
                fig = px.histogram(df, x='SMI', color='Marital.Status', facet_col='Inv_plan')
                st.plotly_chart(fig)
               
                g=df[['SMI', 'Marital.Status', 'Inv_plan']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
        elif options4 == 'Inv_plan' and options5 == 'Profession':
                st.header("Investment plan Vs Profession")
                fig = px.histogram(df, x='SMI', color='Profession', facet_col='Inv_plan')
                st.plotly_chart(fig)
               
                g=df[['SMI', 'Profession', 'Inv_plan']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
        elif options4 == 'Inv_plan' and options5 == 'Education':
                st.header("Investment plan Vs Education")
                fig = px.histogram(df, x='SMI', color='Education', facet_col='Inv_plan')
                st.plotly_chart(fig)
               
                g=df[['SMI', 'Education', 'Inv_plan']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
        elif options4 == 'Inv_plan' and options5 == 'Income':
                st.header("Investment plan Vs Income")
                fig = px.histogram(df, x='SMI', color='Inv_plan', facet_col='Income')
                st.plotly_chart(fig)
               
                g=df[['SMI', 'Income', 'Inv_plan']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
        elif options4 == 'Inv_plan' and options5 == 'State':
                st.header("Investment plan Vs State")
                fig = px.histogram(df, x='SMI', color='State', facet_col='Inv_plan')
                st.plotly_chart(fig)
               
                g=df[['SMI', 'State', 'Inv_plan']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
        elif options4 == 'Covid_SM' and options5 == 'None':
                st.header("Covid Stock Market Vs Share Market Interest")
                fig = px.histogram(df, x='SMI', color='Covid_SM')
                st.plotly_chart(fig)
                g=df[['SMI', 'Covid_SM']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
        elif options4 == 'Covid_SM' and options5 == 'Gender':
                st.header("Covid Stock Market Vs Gender")
                fig = px.histogram(df, x='SMI', color='Covid_SM', facet_col='Gender')
                st.plotly_chart(fig)
               
                g=df[['SMI', 'Gender', 'Covid_SM']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
        elif options4 == 'Covid_SM' and options5 == 'Age':
                st.header("Covid Stock Market Vs Age")
                fig = px.histogram(df, x='SMI', color='Covid_SM', facet_col='Age')
                st.plotly_chart(fig)
               
                g=df[['SMI', 'Age', 'Covid_SM']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
        elif options4 == 'Covid_SM' and options5 == 'Marital.Status':
                st.header("Covid Stock Market Vs Marital Status")
                fig = px.histogram(df, x='SMI', color='Marital.Status', facet_col='Covid_SM')
                st.plotly_chart(fig)
               
                g=df[['SMI', 'Marital.Status', 'Covid_SM']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
        elif options4 == 'Covid_SM' and options5 == 'Profession':
                st.header("Covid Stock Market Vs Profession")
                fig = px.histogram(df, x='SMI', color='Profession', facet_col='Covid_SM')
                st.plotly_chart(fig)
               
                g=df[['SMI', 'Profession', 'Covid_SM']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
        elif options4 == 'Covid_SM' and options5 == 'Education':
                st.header("Covid Stock Market Vs Education")
                fig = px.histogram(df, x='SMI', color='Education', facet_col='Covid_SM')
                st.plotly_chart(fig)
               
                g=df[['SMI', 'Education', 'Covid_SM']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
        elif options4 == 'Covid_SM' and options5 == 'Income':
                st.header("Covid Stock Market Vs Income")
                fig = px.histogram(df, x='SMI', color='Covid_SM', facet_col='Income')
                st.plotly_chart(fig)
               
                g=df[['SMI', 'Income', 'Covid_SM']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
               
        elif options4 == 'Covid_SM' and options5 == 'State':
                st.header("Covid Stock Market Vs State")
                fig = px.histogram(df, x='SMI', color='State', facet_col='Covid_SM')
                st.plotly_chart(fig)
               
                g=df[['SMI', 'State', 'Covid_SM']]
                df1 = pd.concat([g.value_counts(),
                g.value_counts(normalize=True).mul(100)],axis=1, keys=('counts','percentage'))
                st.table(df1)
    with tab4:
        st.subheader("*The survey responses show that people do have an interest to a certain degree in investing into the share market.")
        st.subheader("*Males show a higher level of interest in the share market compared to females.")
        st.subheader("*With regards to profession a higher number of students tend to show interest to a certain degree in the share market.")
        st.subheader("*In the education catagory the majority of responses are University students who show a little interest in the share market.")
        st.subheader("*In terms of location Tamil Nadu has recorded highest number of survey responses.")
        st.subheader("*The data shows that despite people having a little interest in the share market they do not have any type of investment/Stock/bond account in reserve.")
        st.subheader("*The plot shows that majority of the people who are not interested in the stock market also have not made any kind of investments.")
        st.subheader("*People who have basic financial understanding show some what of an interest in the share market whereas those who have no knowledge at all do not show any interest in the share market.")
        st.subheader("*Survey participants who show little interest in the stock market tend to prefer investing for the future.")
        st.subheader("*The data collection shows that more people generally prefer to invest in the long term.")
        st.subheader("*Majority of people who are not interested in the stock market also show no interest in the equity market.")
        st.subheader("*Survey participants who show little or no interest in the stock market do not have a demat account.")
        st.subheader("*People who show some sort of interest in stock market generally have an unbiassed/neutral opinion.")
        st.subheader("*People generally seek advice from their friends/family with regards to investments.")
        st.subheader("*Survey responses show that people generally have a neutral/open minded opinion of investing in the share market during covid.")

side = st.sidebar.radio('Select what you want to display:', ['Home', 'Data Header', 'Financial Literacy', 'Share Market'])
if side == 'Home':
 home()
elif side == 'Data Header':
 data()
elif side == 'Financial Literacy':
 fl()
elif side == 'Share Market':
 sm()