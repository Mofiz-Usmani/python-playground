🔹 What is a Module?

A module is just a Python file that has some code written inside it — like functions, variables, or classes — which you can reuse in your own program.

👉 Think of a module like a toolbox.
You don’t have to make your own tools every time — you can just use the ones already made.

🔸 Types of Modules
1️⃣ Built-in Modules

These come already installed with Python.
You don’t need to download them.

Examples:

import math
print(math.sqrt(16))   # Output: 4.0

import random
print(random.randint(1, 10))  # Prints a random number between 1 and 10


Modules like math, random, and os are built-in.

2️⃣ External Modules

These are not included with Python.
You have to install them using a tool called pip (Python’s package manager).

For example, to install the pandas library:

pip install pandas


After installing, you can use it in your program.

🔹 Using a Module

Once installed, you can import and use it like this:

import pandas

# Read a CSV file named 'words.csv'
df = pandas.read_csv('words.csv')

# Show first few rows
print(df.head())


📘 Here:

pandas is a module used for working with data and tables.

read_csv() is a function inside pandas that reads CSV files.

💡 Why Use Modules?

Because they save time and effort!
Instead of writing code from scratch, you can use existing ones.

Example:
You can use:

import datetime
print(datetime.datetime.now())


instead of writing your own code to get today’s date and time.

✅ In short:
Modules are pre-written code that help you do things faster.
Use import to include them, and use pip install to add new ones.