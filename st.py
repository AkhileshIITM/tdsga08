import streamlit as st

st.write("""
# Finding the Largest of 3 Numbers
""")

st.header('Give me those 3 number')


num1 = st.number_input("First Number")
num2 = st.number_input("Second Number")
num3 = st.number_input("Third Number")

if num1> num2: 
	if num1>num3:
		ans = num1
	else:
		ans = num3
elif num3 > num2:
	ans = num3
else:
	ans = num2	

st.write(str(ans) + """ is the Largest value""")
