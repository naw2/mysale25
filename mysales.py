import pandas as pd
import streamlit as st
import plotly.express as px
df = pd.read_csv('all_df.csv')
st.set_page_config(page_title = "My Sales Dashboard", page_icon = ":bar_chart:",layout='wide')
st.sidebar.header("Please filter here")
product_name = st.sidebar.multiselect(
    "Select Product",
    options = df['Product'].unique(),
    default = df['Product'].unique() [:5]
)
city_name = st.sidebar.multiselect(
    "Select City",
    options = df['City'].unique(),
    default = df['City'].unique() [:5]
)
month_name = st.sidebar.multiselect(
    "Select Month",
    options = df['Month'].unique(),
    default = df['Month'].unique() [:5]
)
userOption = df.query("Product == @product_name and City == @city_name and Month == @month_name")
st.title(":bar_chart: Sales Dashboard for 2019")
mytotal = df['Total'].sum()
myproduct = df['Product'].nunique()
a,b = st.columns(2)
with a:
    st.subheader("Total Sales")
    st.subheader(f"US $ {mytotal}")
with b:
    st.subheader("No. of Product")
    st.subheader(f"{myproduct}")
productsale = userOption.groupby('Product') ['Total'].sum().sort_values()
c,d,e = st.columns(3)
fig_productsale = px.bar(
    productsale,
    x = productsale.values,
    y = productsale.index,
    title = "Sales by Product"
)
c.plotly_chart(fig_productsale,use_container_width = True)

fig_citysale =px.pie(
    userOption, 
    values='Total', 
    names='City', 
    title='Sales by City'
)
d.plotly_chart(fig_citysale,use_container_width = True)

monthsale = userOption.groupby('Month') ['Total'].sum().sort_values()
fig_monthsale = px.bar(
    monthsale,
    x = monthsale.values,
    y = monthsale.index,
    title = "Sales by Month"
)
e.plotly_chart(fig_monthsale,use_container_width = True)

f,g = st.columns(2)
fig_line_monthsale = px.line(
    userOption, 
    x = monthsale.values,
    y = monthsale.index,
    title = "Sales by Month" 
)
f.plotly_chart(fig_line_monthsale,use_container_width = True)

fig_scatter_sale = px.scatter(
    userOption, 
    x = 'Total',
    y = 'QuantityOrdered',
    title = "Sales by Item Amount" 
)
g.plotly_chart(fig_scatter_sale,use_container_width = True)