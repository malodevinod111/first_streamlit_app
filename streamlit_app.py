import streamlit
import pandas
streamlit.title("My Parent New Helthy Diner")
streamlit.header('🍞 Breakfast Menu')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.multiselect("Pick some fruits: ",my_fruit_list.index+1)
streamlit.dataframe(my_fruit_list)
