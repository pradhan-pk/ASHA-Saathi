# # frontend/pages/login.py
# import streamlit as st

# # Dummy users for testing (will be replaced by backend/API later)
# DUMMY_USERS = {
#     "asha001": {"name": "Seema Devi", "password": "asha123"},
#     "asha002": {"name": "Radha Kumari", "password": "asha456"},
# }

# def show():
#     st.title("🔐 ASHA-Sathi Login")

#     st.write("Please login with your ASHA ID")

#     username = st.text_input("ASHA ID")
#     password = st.text_input("Password", type="password")

#     if st.button("Login"):
#         user = DUMMY_USERS.get(username)
#         if user and user["password"] == password:
#             st.session_state["user"] = {
#                 "id": username,
#                 "name": user["name"]
#             }
#             st.success(f"Welcome, {user['name']} 👋")
#             st.rerun()
#         else:
#             st.error("Invalid ASHA ID or Password")

import streamlit as st
from data.dummy_data import USERS

def show():
    st.title("🔐 ASHA-Sathi Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        user = USERS.get(username)
        if user and user["password"] == password:
            st.session_state["user"] = user
            st.success(f"Welcome, {user['name']}!")
            st.query_params["page"]="Dashboard"
            st.rerun()
        else:
            st.error("Invalid credentials")
