import streamlit as st
import pandas as pd
from src.analytics import *

st.sidebar.title("Filters (Coming Soon)")
st.title("📊 E-Commerce Analytics Dashboard")

# 🔥 Top Selling Products
st.header("🔥 Top Selling Products")
data1 = top_selling_products()
df1 = pd.DataFrame(data1, columns=["Product", "Total Sold"])
st.dataframe(df1)
st.bar_chart(df1.set_index("Product"))

# 💰 Top Users
st.header("💰 Top Users")
data2 = top_users()
df2 = pd.DataFrame(data2, columns=["User", "Total Spent"])
st.dataframe(df2)
st.bar_chart(df2.set_index("User"))

# 📈 Revenue by Category
st.header("📈 Revenue by Category")
data3 = revenue_by_category()
df3 = pd.DataFrame(data3, columns=["Category", "Revenue"])
st.dataframe(df3)
st.bar_chart(df3.set_index("Category"))

# ⭐ Best Rated Products
st.header("⭐ Best Rated Products")
data4 = best_rated_products()
df4 = pd.DataFrame(data4, columns=["Product", "Rating"])
st.dataframe(df4)
st.bar_chart(df4.set_index("Product"))
