# ==========================
# Basic Arithmetic
# ==========================
print(5 * 6)      # Multiplication → 30
print(8 / 4)      # Division → 2.0

# ==========================
# Escape Sequences
# ==========================
print("Hello World\nWelcome to Python Programming!")  # \n → New line
print("Python\t\tProgramming")                        # \t → Tab space
print("Python\"Programming\"")                        # \" → Double quote (\" \")
print('Python\'Programming\'')                        # \' → Single quote
print("C:\\Users\\Admin")                             # \\ → Backslash

# ==========================
# Multi-line Comments
# ==========================
"""
This is a comment using triple double quotes
"""
'''
This is a comment using triple single quotes
'''

# ==========================
# Quotes inside Strings
# ==========================
print("Hello \"This is Jackal\"")  # Escaping double quotes inside string

# ==========================
# Printing Multiple Values
# ==========================
print("Hello", 5, 6, 9)            # Default separator is space
print("Hey", 6, 7, sep="-")        # sep → Custom separator
# Output: Hey-6-7

# ==========================
# Controlling End of Print
# ==========================
print("Hello", end="***")          # end → Add something at the end
print("World")                      # Output: Hello***World

# ==========================
# Combined Example
# ==========================
print("Hello Jackal is a \"Good Boy\"\nThat's it")  # Combined escape sequences




print("Values:", 10, 20, 30, sep=" | ", end=" <<< END\n")  # Combined print options