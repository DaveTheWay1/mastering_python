
# * 1. Immutable vs Mutable Types
# Tuple vs List:
# Tuples are immutable, and thus they are generally more memory-efficient than lists, which are mutable and require additional space to allow modifications.
# Example: A tuple (1, 2, 3) will take up less memory than a list [1, 2, 3].
# * 2. Numbers
# Integer vs Float:
# Integers typically consume less memory than floats due to the additional precision stored in floats.
# Example: 5 (integer) takes less memory than 5.0 (float).
# * 3. String:
# Strings are immutable, and their memory usage grows with the number of characters. In Python, strings are stored as sequences of Unicode code points, which may take more memory compared to some other languages.
# Example: "a" takes less memory than "apple".
# * 4. Dictionary vs Set:
# Dictionaries store key-value pairs and need extra memory for both the keys and values. They are generally larger than sets, which store only keys.
# Example: A set {1, 2, 3} takes less memory than a dictionary {1: 'a', 2: 'b', 3: 'c'}.
# * 5. Custom Objects:
# Objects that you create with Python classes generally take up more memory than simpler data structures, as they include additional overhead for attributes and methods.
# Example: A custom class object will take more memory than a list or a tuple storing the same data.
# 
# ! Memory Efficiency Chart (Estimated Comparison)
# Data Structure	Estimated Memory Usage (Ascending Order)
# * int	Least
# * float	Slightly more than int
# * tuple	More than float but less than list
# * list	More than tuple
# * set	More than list
# * dictionary	More than set
# * custom class object	Most

# * Memory Profiling in Python
# ? To measure memory usage precisely, you can use tools like:
# sys.getsizeof(): Measures the size of an object in bytes.
# memory_profiler: Helps track memory usage over time, especially in large programs.
# pympler: Provides detailed memory usage of objects.
# Here's an example using sys.getsizeof():

# python
# Copy code
# import sys

# my_list = [1, 2, 3]
# my_tuple = (1, 2, 3)

# print("List memory:", sys.getsizeof(my_list))  # Prints memory used by list
# print("Tuple memory:", sys.getsizeof(my_tuple))  # Prints memory used by tuple