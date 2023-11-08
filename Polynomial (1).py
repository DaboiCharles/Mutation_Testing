class Polynomial:
    def __init__(self, coefficients):
        """
        Initialize a polynomial with a list of coefficients. The coefficients list should be in descending order of
        the exponent, for example: [3, 0, 2] represents 3x^2 + 2.
        """
        self.coefficients = coefficients

    def __str__(self):
        """
        Return a string representation of the polynomial.
        """
        if len(self.coefficients) == 0:
            return "0"

        terms = []
        for i, coef in enumerate(self.coefficients):
            if coef == 0:
                continue
            term = str(coef)
            if i < len(self.coefficients) - 1:
                if i == len(self.coefficients) - 2:
                    term += "x"
                else:
                    term += "x^" + str(len(self.coefficients) - i - 1)
            terms.append(term)
        return " + ".join(terms)

    def __add__(self, other):
        """
        Add two polynomials and return a new polynomial.
        """
        #normal code
        # max_length = max(len(self.coefficients), len(other.coefficients))
        # padded_self = [0] * (max_length - len(self.coefficients)) + self.coefficients
        # padded_other = [0] * (max_length - len(other.coefficients)) + other.coefficients
        # result_coefficients = [a + b for a, b in zip(padded_self, padded_other)]
        # return Polynomial(result_coefficients)

        # mutation to subtraction
        max_length = max(len(self.coefficients), len(other.coefficients))
        padded_self = [0] * (max_length - len(self.coefficients)) + self.coefficients
        padded_other = [0] * (max_length - len(other.coefficients)) + other.coefficients
        result_coefficients = [a - b for a, b in zip(padded_self, padded_other)]
        return Polynomial(result_coefficients)

        #mutation to mutiplication
        # max_length = max(len(self.coefficients), len(other.coefficients))
        # padded_self = [0] * (max_length - len(self.coefficients)) + self.coefficients
        # padded_other = [0] * (max_length - len(other.coefficients)) + other.coefficients
        # result_coefficients = [a * b for a, b in zip(padded_self, padded_other)]
        # return Polynomial(result_coefficients)

        #mutation to divison
        # max_length = max(len(self.coefficients), len(other.coefficients))
        # padded_self = [0] * (max_length - len(self.coefficients)) + self.coefficients
        # padded_other = [0] * (max_length - len(other.coefficients)) + other.coefficients
        # result_coefficients = [a / b for a, b in zip(padded_self, padded_other)]
        # return Polynomial(result_coefficients)




    def __sub__(self, other):
        """
        Subtract another polynomial from this polynomial and return a new polynomial.
        """
        max_length = max(len(self.coefficients), len(other.coefficients))
        padded_self = [0] * (max_length - len(self.coefficients)) + self.coefficients
        padded_other = [0] * (max_length - len(other.coefficients)) + other.coefficients
        result_coefficients = [a - b for a, b in zip(padded_self, padded_other)]
        return Polynomial(result_coefficients)
    
         #mutation to mutiplication
        # max_length = max(len(self.coefficients), len(other.coefficients))
        # padded_self = [0] * (max_length - len(self.coefficients)) + self.coefficients
        # padded_other = [0] * (max_length - len(other.coefficients)) + other.coefficients
        # result_coefficients = [a * b for a, b in zip(padded_self, padded_other)]
        # return Polynomial(result_coefficients)

        #mutation to divison
        # max_length = max(len(self.coefficients), len(other.coefficients))
        # padded_self = [0] * (max_length - len(self.coefficients)) + self.coefficients
        # padded_other = [0] * (max_length - len(other.coefficients)) + other.coefficients
        # result_coefficients = [a / b for a, b in zip(padded_self, padded_other)]
        # return Polynomial(result_coefficients)

        #mutation to addition
        # max_length = max(len(self.coefficients), len(other.coefficients))
        # padded_self = [0] * (max_length - len(self.coefficients)) + self.coefficients
        # padded_other = [0] * (max_length - len(other.coefficients)) + other.coefficients
        # result_coefficients = [a + b for a, b in zip(padded_self, padded_other)]
        # return Polynomial(result_coefficients)



    def __mul__(self, other):
        """
        Multiply this polynomial by another polynomial and return a new polynomial.
        """
        result_deg = len(self.coefficients) + len(other.coefficients) - 1
        result_coefficients = [0] * result_deg
        for i in range(len(self.coefficients)):
            for j in range(len(other.coefficients)):
                result_coefficients[i + j] += self.coefficients[i] * other.coefficients[j]
        return Polynomial(result_coefficients)

    def evaluate(self, x):
        """
        Evaluate the polynomial for a given value of x.
        """
        result = 0
        for i, coef in enumerate(self.coefficients):
            result += coef * (x ** (len(self.coefficients) - i - 1))
        return result
    
    def get_derivative_coefficients(self):
        """
        Return the coefficients of the derivative polynomial.
        """
        return [i*coeff for (i,coeff) in enumerate(list(reversed(self.coefficients))[:-1])]
        

    def find_root_bisection(self, a, b, epsilon=1e-6, max_iterations=100):
            """
            Find a root (zero) of the polynomial using the bisection method within the interval [a, b].
            :param a: Left boundary of the interval.
            :param b: Right boundary of the interval.
            :param epsilon: Tolerance for the root approximation.
            :param max_iterations: Maximum number of iterations.
            :return: Approximated root within the specified interval.
            """
            if self.evaluate(a) * self.evaluate(b) > 0:
                raise ValueError("The chosen interval does not contain a root.")

            for _ in range(max_iterations):
                c = (a + b) / 2
                print(c)
                if abs(self.evaluate(c)) < epsilon:
                    return c
                if self.evaluate(c) * self.evaluate(a) < 0:
                    b = c
                else:
                    a = c

            raise ValueError("Bisection method did not converge within the maximum number of iterations.")

# Example usage:
poly1 = Polynomial([3, 0, 2])  # Represents 3x^2 + 2
poly2 = Polynomial([1, -1])    # Represents x - 1

print("poly1:", poly1)
print("poly2:", poly2)

poly_sum = poly1 + poly2
print("Sum:", poly_sum)

poly_diff = poly1 - poly2
print("Difference:", poly_diff)

poly_product = poly1 * poly2
print("Product:", poly_product)

x_value = 2
result = poly1.evaluate(x_value)
print(f"Evaluation of poly1 at x={x_value}: {result}")

poly = Polynomial([1, 0, -2])  # Represents x^2 - 2
print(f"Evaluation of poly at a,b: {poly.evaluate(0)}, {poly.evaluate(5)}")
root = poly.find_root_bisection(0, 5)
print(f"Root of {poly} within [0, 5]: {root}")