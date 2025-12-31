import streamlit as st
import pandas as pd
from supabase_config import supabase

st.title("Perfume SaaS Dashboard")

# --- Add New Product ---
st.header("Add New Product")
name = st.text_input("Product Name")
price = st.number_input("Price", min_value=0.0)
if st.button("Add Product"):
    if name:
        data = {"name": name, "price": price}
        supabase.table("products").insert(data).execute()
        st.success(f"Product {name} added!")
    else:
        st.error("Product name is required")

# --- Show All Products ---
st.header("All Products")
res = supabase.table("products").select("*").execute()
df = pd.DataFrame(res.data)
st.dataframe(df)

# --- Update Product Price ---
st.header("Update Product Price")
product_id = st.number_input("Product ID", min_value=1)
new_price = st.number_input("New Price", min_value=0.0)
if st.button("Update Price"):
    supabase.table("products").update({"price": new_price}).eq("id", product_id).execute()
    st.success("Price updated")

# --- Delete Product ---
st.header("Delete Product")
delete_id = st.number_input("Product ID to Delete", min_value=1)
if st.button("Delete Product"):
    supabase.table("products").delete().eq("id", delete_id).execute()
    st.success("Product deleted")

