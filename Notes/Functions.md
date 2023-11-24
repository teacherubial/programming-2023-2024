---
tags:
  - programming
  - notes
---
# Function

A function is a block of code that can be reused over and over again.

We can input data to the function. We can refer to the data as **parameters**.

We use the term **arguments** to describe the ACTUAL data that we put
into the function.

```python
def area_of_a_square(sidelength: float):
	"""Calculates the area of a square.
	Results are in units squared.
	
	Params:
	
	sidelength - length of one side of the square"""

	area = sidelength ** 2
	
	print(f"The area of a square with side length = {sidelength} is: {area} square units")

area_of_a_square(12.2)  # 12.2 is the argument

```