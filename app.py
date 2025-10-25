import streamlit as st

# --- Define your functions ---
def greet():
    return "👋 Hello there! Welcome to the Streamlit demo."

def add_numbers(a, b):
    return f"The sum of {a} and {b} is {a + b}."

def multiply_numbers(a, b):
    return f"The product of {a} and {b} is {a * b}."

def show_info():
    return "ℹ️ Streamlit helps you create web apps easily with Python!"

# --- Streamlit App Layout ---
st.set_page_config(page_title="Simple Streamlit App", page_icon="🚀")

st.title("🚀 Simple Streamlit App with Buttons and Functions")

st.write("Click a button below to perform an action:")

# --- Input fields for numeric functions ---
a = st.number_input("Enter first number:", value=0)
b = st.number_input("Enter second number:", value=0)

# --- Buttons and their actions ---
if st.button("Say Hello"):
    st.success(greet())

if st.button("Add Numbers"):
    st.info(add_numbers(a, b))

if st.button("Multiply Numbers"):
    st.warning(multiply_numbers(a, b))

if st.button("About Streamlit"):
    st.write(show_info())

# --- Footer ---
st.write("---")
st.caption("Created with ❤️ using Streamlit")
