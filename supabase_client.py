from supabase import create_client
import streamlit as st

# Ye credentials Streamlit Cloud secrets me honi chahiye
SUPABASE_URL = st.secrets["SUPABASE_URL"]
SUPABASE_KEY = st.secrets["SUPABASE_KEY"]

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

