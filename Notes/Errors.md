# Syntax Errors

These type of errors are ones that occur when you run your code
and then it **breaks**.

Syntax errors are relatively easy to *spot* and *fix*.

**Syntax** errors occur when we don't follow the **rules** of the
language completely.

# Semantic Errors

Semantic errors occur when our code doesn't **MEAN** what we
intend it to **MEAN**.

These errors, in Mr. Ubial's opinion, are FAR MORE challenging
to spot and fix.

```python
user_response = input("Do you like to eat food? ")

if user_response == "yes":
	print("You are a human.")
else:
	print("You must be some sort of robot.")
```

The problem with the code above is subtle. What I (Mr. Ubial) mean
is that EVERY ANSWER OF YES should go into the YES block.

One way to solve this problem is to use [[Strings#String Methods|string methods]].
We can use `.lower()` to fix this error.

```python
user_response = input("Do you like to eat food? ")

if user_response.lower() == "yes":
	print("You are a human.")
else:
	print("You must be some sort of robot.")
```