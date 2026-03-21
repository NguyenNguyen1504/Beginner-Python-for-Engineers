from math import degrees

import matplotlib.pyplot as plt
from matplotlib.pyplot import title


def evaluate_polynomial(coefficients, x):
    highest_degree = len(coefficients) - 1
    degrees_list = [highest_degree - i for i in range(highest_degree + 1)]
    terms = [coefficient * x**degree for (degree, coefficient) in zip(degrees_list,coefficients)]
    result = sum(terms)

    return result

def polynomial_to_string(coefficients):
    highest_degree = len(coefficients) - 1
    degrees_list = [highest_degree - i for i in range(highest_degree + 1)]
    terms = [str(coefficient)+("x^"+str(degree))*(degree != 0) for (degree, coefficient) in zip(degrees_list, coefficients) if coefficient != 0]

    return " + ".join(terms)

def plot_polynomial(coefficients):
    # Generate x values
    x_values = [i for i in range(-100, 101)]
    # Generate y values using the polynomial
    y_values = [evaluate_polynomial(coefficients,x) for x in x_values]
    # Generate the title
    graph_title = polynomial_to_string(coefficients)
    # Create the plot
    fig, ax = plt.subplots()
    ax.set_title(f"Plot of {graph_title}")
    ax.plot(x_values,y_values)
    plt.show()


def main():
    try:
        coefficients = list(map(float, input("Enter the polynomial coefficients (space-separated):\n").split()))
        plot_polynomial(coefficients)
    except ValueError:
        print("Invalid input. Please enter a list of space-separated numbers.")


if __name__ == "__main__":
    main()