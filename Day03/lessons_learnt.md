# What have I learnt from AoC day 3 in Python?

- You can have factory methods, and static methods in general, by using `@classmethod` before a class method definition and then the first parameter is `cls` rather than `self`

```py
    @classmethod
    def from_string(cls, input: str):
```

- To refer to the type of this class in the method signatures you need to either `from future import annotations` at the top of your file, or put the class name in quotes to mark it as a 'forward'

- There are a number of global functions for common operations:

  - len() for the length of a list or string

  - sum() to sum the values of every element in a list

  - ord() to get the ascii value of a character

- Using slicing it is easy to split a list into groups of three:

```py
# split the list into groups of 3
groups = [
all_rucksack_data[i : i + 3] for i in range(0, len(all_rucksack_data), 3)
]
```

- No method overloading in Python, so only one method with each name, including `__init__`

  - So factory methods have to be explicit class methods, not hidden in an overloaded constructor
