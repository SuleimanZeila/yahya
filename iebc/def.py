import streamlit as st
import pandas as pd

st.set_page_config(page_title='Election Analysis',page_icon="chart_with_upwards_trend",)

st.title("2022 Election Data Analysis.")

col1, col2 = st.columns(2)

dfward = pd.read_excel("Book1.xlsx",sheet_name='Sheet2')

dfpoling=pd.read_excel("Book1.xlsx",sheet_name='df')

with st.form("my_form"):

	ward_select = col1.selectbox('Choose your ward',dfward)

	dfpolingFl = dfpoling[dfpoling['WARDS'].str.match(ward_select)]

	poling_select = col2.selectbox('Choose your poling station',dfpolingFl['POLING_STATION'])

	col3, col4,col5,col6,col7 = st.columns(5)

	regNo = col3.number_input("Registered Voters",min_value=0)
	rejVotes = col4.number_input("Rejected Voters",min_value=0)
	desValues = col5.number_input("Desputed Votes",min_value=0)
	valid = col6.number_input("Valid Votes Casted",min_value=0)
	###waiting for confirmation
	rejOb = col7.number_input("Rejection Objected",min_value=0)
	st.markdown(" ")
	st.markdown(" ")



	st.subheader("Data for Candidates.")
	col8, col9, col10 = st.columns(3)

	hon_Farah = col8.number_input("Hon Farah Maalim", min_value=0)
	kheyrow = col9.number_input("Kheyrow", min_value=0)
	a_Issack = col10.number_input("Ahmed Issack", min_value=0)
	st.markdown('')
	st.markdown('')

	submitted = st.form_submit_button("Submit")
	if submitted:
		dfup = pd.read_excel("Book3.xlsx",sheet_name='general')
		regNo >= (rejVotes + desValues+ valid +rejOb )
		valid == (hon_Farah+kheyrow+a_Issack)
		infoo = [ward_select,poling_select, regNo, rejVotes, desValues, valid , rejOb]
		dfup.loc[len(dfup)] = infoo
		##saving the input values
		writer = pd.ExcelWriter("dday.xlsx", engine='xlsxwriter')
		dfup.to_excel(writer,sheet_name = 'general', index=False)
		writer.save() 


footer="""
 <style>
 @import url('https://fonts.googleapis.com/css2?family=Cormorant+SC:wght@700&display=swap');
 .css-12ttj6m{
 border:none;
 }
 .css-1cpxqw2{
 background-color:#17A2B8;
 color:#fff;
 }
 .css-1cpxqw2:hover{
 background-color:#fff;
 color:skyblue;
 border:1px solid #17A2B8;
 }
 .css-10trblm{
 text-align:center;
 font-family: 'Cormorant SC', serif;
 margin-bottom:34px;
 margin-top:-35px;
 }
 </style>
 """
st.markdown(footer,unsafe_allow_html=True) 