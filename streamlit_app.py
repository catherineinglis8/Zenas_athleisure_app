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

st.write(df)
st.stop()


st.write("Pick a sweatsuit color of style:")
my_dataframe = session.table("ZENAS_ATHLEISURE_DB.PRODUCTS.catalog_for_website").select(col('COLOR_OR_STYLE'),col('DIRECT_URL'))
st.dataframe(data=my_dataframe, use_container_width=True)
st.stop()

#Convert the Snowpark Dataframe to a Pandas Dataframe so we can use the LOC function
pd_df = my_dataframe.to_pandas()
#st.dataframe(pd_df)
#st.stop()

ingredients_list = st.multiselect('Choose up to 5 ingredients:',my_dataframe, max_selections = 5)
if ingredients_list:
    ingredients_string = ''

    for fruit_chosen in ingredients_list:
        ingredients_string += fruit_chosen + ' '

        search_on=pd_df.loc[pd_df['FRUIT_NAME'] == fruit_chosen, 'SEARCH_ON'].iloc[0]
        #st.write('The search value for ', fruit_chosen,' is ', search_on, '.')

        st.subheader(fruit_chosen + ' Nutrition Information')
        fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + search_on)
        fv_df = st.dataframe(data=fruityvice_response.json(),use_container_width=True)
   # st.write(ingredients_string)

    my_insert_stmt = """ insert into smoothies.public.orders(ingredients, name_on_order)
            values ('""" + ingredients_string + """','"""+ name_on_order +"""')"""

    
    #st.write(my_insert_stmt)
    # if ingredients_string:
    time_to_insert = st.button("Submit Order")
    if time_to_insert:
        session.sql(my_insert_stmt).collect()
        st.success('Your Smoothie is ordered!', icon="✅")



