import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import tkinter
def get_expression():
    """Takes user input and returns a sympy expression."""
    expr_input = st.text_area("Enter a function of x:")
    if expr_input:
        try:
            expr = sp.sympify(expr_input)
            return expr
        except sp.SympifyError:
            st.error("Invalid expression! Please try again.")
            return None
    return None

def plot_expression(expr, label):
    """Plots and displays the given expression."""
    x = sp.symbols('x')
    func = sp.lambdify(x, expr, modules=['numpy'])

    x_vals = np.linspace(-10, 10, 400)
    try:
        y_vals = func(x_vals)
    except Exception as e:
        st.error(f"Error evaluating the function: {e}")
        return

    plt.figure(figsize=(8, 5))
    plt.plot(x_vals, y_vals, label=label, color='teal')
    plt.title('Graph Plotter', fontsize=16)
    plt.xlabel('x', fontsize=12)
    plt.ylabel('y', fontsize=12)
    plt.grid(True)
    plt.legend()

    st.pyplot(plt)

def main():
    st.title("Function Plotter 📈")
    
    expr = get_expression()

    if expr is not None:
        choice = st.radio(
            "What do you want to plot?",
            ("Original Function", "Derivative", "Integral")
        )

        x = sp.symbols('x')

        if choice == "Original Function":
            label = f"f(x) = {expr}"
            st.write(f"Plotting Original Function: {expr}")
            plot_expression(expr, label)

        elif choice == "Derivative":
            derivative = sp.diff(expr, x)
            label = f"f'(x) = {derivative}"
            st.write(f"Derivative: {derivative}")
            plot_expression(derivative, label)

        elif choice == "Integral":
            integral = sp.integrate(expr, x)
            label = f"∫f(x)dx = {integral} + C"
            st.write(f"Integral: {integral} + C")
            plot_expression(integral, label)

if __name__ == "__main__":
    main()
