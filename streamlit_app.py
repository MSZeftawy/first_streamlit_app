# this is part of Snowflake badge 2 certificate

import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title("My Mom's New Healthy Diner")

streamlit.header ('Breakfast Favorites')


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

streamlit.header('Fruityvice Fruit Advice!')

# a function to get fruit data from fruityvice
def get_fruityvice_data(this_fruit_choice):
  # get response from API
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choise)
   
  # normalise the json resonse
  fruityvice_normalised = pandas.json_normalize(fruityvice_response.json())
  
  return fruityvice_normalised

try:
  fruit_choise = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choise:
    streamlit.error("Please select a fruit to get information.")
  
  else:
    back_from_function = get_fruityvice_data(fruit_choise)
    
    # output json response as a table
    streamlit.dataframe(back_from_function)
    #streamlit.write('The user entered',fruit_choise)


    # streamlit.text(fruityvice_response.json()) # to output data on display

except URLError as e:
  streamlit.error()


streamlit.header("The fruit load list contains:")
# connecting snowflake function
def get_fruit_load_list():
with my_cnx.cursor() as my_cur:  
  # my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
  my_cur.execute("SELECT * from fruit_load_list")
  return my_cur.fetchall()
# streamlit.text("Hello from Snowflake:")

# a button to load the fruit list
if streamlit.button('Get Fruit Load List'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows = get_fruit_load_list()
  streamlit.dataframe(my_data_rows)

# allow the end user to add a fruit to the list
add_my_fruit = streamlit.text_input('What fruit would you like to add?','Kiwi')
streamlit.write ('The user entered', add_my_fruit)
my_cur.execute("insert into fruit_load_list values ('add_my_fruit')")
