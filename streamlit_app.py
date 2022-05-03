# this is part of Snowflake badge 2 certificate

import streamlit
import pandas
import requests

streamlit.title('My Parents New Healthy Diner')

streamlit.header ('Breakfast Menu')


streamlit.text ('🥣 Omega 3 & Blueberry Oatmeal')

streamlit.text ('🥗 Kale, Spinach, & Rocket Smoothie')

streamlit.text ('🐔 Hard-Boiled Free-Range Egg')

streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

my_fruit_list = my_fruit_list.set_index('Fruit')

# adding a pick list
fruits_selected = streamlit.multiselect("Pick some Fruits:", list(my_fruit_list.index))

fruits_to_show = my_fruit_list.loc[fruits_selected]

# display the table on the page
streamlit.dataframe(fruits_to_show)

# get response from API
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json()) # to output data on display

# normalise the json resonse
fruityvice_normalised = pandas.json_normalize(fruityvice_response.json())

# output json response as a table
streamlit.dataframe(fruityvice_normalised)

