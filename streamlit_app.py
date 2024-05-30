import streamlit as st
import snowflake.connector
#my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
my_cnx = snowflake.connector.connect(
user = catherineinglis,
password = "CiGdr1*6",
account = "QS89075.ca-central.aws",
warehouse = "compute_wh",
database = "ZENAS_ATHLEISURE_DB",
schema = "PRODUCTS")
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(),CURRENT_REGION()")
my_data_row = my_cur.fetchone()
st.text("Hello from Snowflake:")
st.text(my_data_row)


