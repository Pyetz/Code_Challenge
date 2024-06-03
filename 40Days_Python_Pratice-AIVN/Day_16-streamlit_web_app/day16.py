import streamlit as st
from factorial import factorial

def main():
    st.title("Factorial Calculator")
    n = st.number_input("Enter a number", min_value=0, max_value=900, value=0, step=1)
    if st.button("Calculate"):
        result = factorial(n)
        st.write(f"The factorial of {n} is {result}")
        st.balloons()

if __name__ == "__main__":
    main()