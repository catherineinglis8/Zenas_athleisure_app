import streamlit as st
import snowflake.connector
import pandas as pd

st.title("Zena\'s Amazing Athleisure Catalog")

#Connect to snowflake
my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor()

#run a snowflake quert to put it all in a var called my_catalog
my_cur.execute("SELECT COLOR_OR_STYLE FROM catalog_for_website")
my_catalog = my_cur.fetchall()

#Put the data into a panda dataframe
df = pd.DataFrame(my_catalog)
color_list = df[0].values.tolist()

#st.write(df)
#st.stop()
color_selected = st.selectbox("Pick a sweatsuit color or style:",list(color_list))
st.stop()
caption = 'Our warm, comfortable, ' + color_selected + 'sweatsuit!'

my_cur.execute("SELECT direct_url, price, size_list, upsell_product_desc FROM catalog_for_website where color_or_style = '" + option + "';")
df2 = my_cur.fetchone()

#display photo with caption
st.image(df[0],widght = 400,caption = product_caption)
#display writing






