
import streamlit as st

def add(num1: float, num2: float) -> float:
    return num1 + num2

def subtract(num1: float, num2: float) -> float:
    return num1 - num2

def multiply(num1: float, num2: float) -> float:
    return num1 * num2

def divide(num1: float, num2: float) -> float:
    if num2 == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return num1 / num2

def main():
    st.title("Simple Calculator")

    # Inject custom CSS
    st.markdown("""
        <style>
        div.stButton > button {
            background-color: green;
            color: white;
        }
        div.stButton > button:disabled {
            background-color: red;
            color: white;
        }
                div.stButton > button:hover {
            background-color: blue;
            color: white;
        }
                div.stButton > button:disabled:hover {
            background-color: darkred;
            color: white;
        }
                </style>
        """, unsafe_allow_html=True)

    num1 = st.number_input("Enter first number", value=0.0)
    num2 = st.number_input("Enter second number", value=0.0)

    operation = st.selectbox("Select operation", ("Add", "Subtract", "Multiply", "Divide"))

    result = None
    button_disabled = (num1 == 0.0 and num2 == 0.0)
    if st.button("Calculate", disabled=button_disabled):
        try:
            if operation == "Add":
                result = add(num1, num2)
            elif operation == "Subtract":
                result = subtract(num1, num2)
            elif operation == "Multiply":
                result = multiply(num1, num2)
            elif operation == "Divide":
                result = divide(num1, num2)
        except ZeroDivisionError as e:
            st.error(f"Error: {e}")
        except Exception as e:
            st.error(f"An unexpected error occurred: {e}")

    if result is not None:
        st.success(f"Result: {result}")

if __name__ == "__main__":
    main()
