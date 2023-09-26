In Python, lists are a collection of items  
We store values inside of lists  
The values of the items can be of different [[Types]]  
**Order matters** in a list

# Creating a List
To make a list, we use brackets \[\] to surround our list  
We separate the individual items with commas

```python
some_list = ["Jimmy", "Sara", "Frederique"]
```

# Access Elements in the List
We can access the individual things from lists using **bracket notation**  
In the example below, we'll use bracket notation to access "Sara"  

```python
some_list[1]          # "Sara"
some_list[0]          # "Jimmy"
some_list[2]          # "Frederique"
some_list[-1]         # "Frederique"  counts from the end
some_list[-2]         # "Sara"
```

Inside the brackets, we give the *index* of the item we want  
Python uses **0-index** counting, which means we start counting at 0