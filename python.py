python
import math

def quadratic_roots(a, b, c):
  """Calculates the roots of a quadratic equation.

  Args:
    a: The coefficient of the x^2 term.
    b: The coefficient of the x term.
    c: The constant term.

  Returns:
    A tuple of the two roots of the equation.
  """

  # Check if the equation has real roots.
  discriminant = b**2 - 4*a*c
  if discriminant < 0:
    return None

  # Calculate the roots.
  root1 = (-b + math.sqrt(discriminant)) / (2*a)
  root2 = (-b - math.sqrt(discriminant)) / (2*a)

  return root1, root2


# Get the input from the user.
a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))

# Calculate the roots.
roots = quadratic_roots(a, b, c)

# Print the roots.
if roots is not None:
  print("The roots of the equation are:", roots)
else:
  print("The equation has no real roots.")