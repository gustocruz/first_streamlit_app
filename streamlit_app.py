import streamlit
import pandas

streamlit.title('My Mom''s New Healthy Diner')

streamlit.header('Breakfast Favorites')

streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard Boiled Free Range Egg')
streamlit.text('🥑🍞 Avocato Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

#let's add a pick list
streamlis.multiselect("Pick some fruits:", list(my_fruit_list.index))

#display the table on te top page 
streamlit.dataframe(my_fruit_list)
