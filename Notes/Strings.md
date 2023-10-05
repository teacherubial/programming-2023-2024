# Format Strings
We can evaluate inside of strings using *f-strings*.  
To create an f-string, we put an `f` before the opening quote.

```python
fave_food = input("What's your favourite food? ")
print(f"Ooooooo, {fave_food} sounds good!")
```

# String Methods

[[Methods]] are functions that we can use on [[Objects]].

String methods allow us to modify and work with strings.

Say for example, we want to make all characters of a string
lowercase.

```python
mr_ubial_yelling = "PLEASE PUSH YOUR CHAIRS IN"

print(mr_ubial_yelling.lower())  # lowercases the letters
```

The `.lower()` method takes a string and converts all UPPERCASE
characters to lowercase.

We can use `.lower()` to help with [[Errors#Semantic Errors|errors]].
