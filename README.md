# Data Science
Data science is a multidisciplinary field that combines elements of statistics, mathematics, computer science, and domain knowledge to extract insights and knowledge from data. It involves using various techniques, such as machine learning, data mining, and predictive analytics, to analyze and interpret large and complex data sets.

Data science can be applied in a wide range of domains, including business, healthcare, finance, social sciences, and more. Some of the common tasks performed by data scientists include data cleansing and preprocessing, exploratory data analysis, feature engineering, model building and validation, and communicating insights to stakeholders.

With the increasing availability of data and computing power, data science has become an essential tool for businesses and organizations to gain a competitive edge and make informed decisions. It is also an exciting and rapidly evolving field with many career opportunities.

## Importance of Data Science

Importance of data science in today's world:

◦ The amount of data being generated is growing exponentially.

◦ Data science provides valuable insights that can be used to drive innovation, improve processes, and 
make informed decisions.

# Python Basics
Python is a high-level, general-purpose programming language that is widely used in many fields, including data science, machine learning, web development, and scientific computing. It was created by Guido van Rossum in the late 1980s and named after the Monty Python comedy group.

## 1 Variables: 
Variables are used to store data. In Python, you can declare a variable and assign a value to it like this:

x = 10

name = "Zahoor"

## 2 Print statement: 
The print() function is used to display output to the console. You can print a variable or a string literal like this:

print(x)

print("Hello, world!")

## 3 Basic operations: 
Python supports basic mathematical operations like addition, subtraction, multiplication, division, and modulus. Here are some examples:

a = 5

b = 3

print(a + b)   # Output: 8

print(a - b)   # Output: 2

print(a * b)   # Output: 15

print(a / b)   # Output: 1.6666666666666667

print(a % b)   # Output: 2

## 4 Conditional statements: 
Conditional statements are used to execute different blocks of code based on certain conditions. In Python, you can use the if-else statement like this:

age = 20

if age >= 18:

    print("You are an adult.")
    
else:

    print("You are a minor.")
    
## 5 Loops: 
Loops are used to execute a block of code multiple times. Python has two types of loops: 'for' and 'while'. Here are some examples:

#### for loop

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:

    print(fruit)

#### while loop

i = 1

while i <= 5:

    print(i)
    i += 1
  
## 6 Functions:
Functions are used to group a set of statements that perform a specific task. In Python, you can define a function using the 'def' keyword. Here is an example:

def my_function(name):

    print("Hello, " + name)
    
my_function("John")

# Numpy
NumPy (Numerical Python) is a Python library for scientific computing that provides support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays. It is a fundamental library for scientific computing in Python and is used in many areas such as machine learning, image processing, signal processing, and more.

Some of the features of NumPy include:

Multi-dimensional arrays: NumPy provides support for creating and manipulating multi-dimensional arrays and matrices.

Fast mathematical operations: NumPy is designed for fast mathematical operations on arrays and matrices using optimized algorithms written in C or Fortran.

Broadcasting: NumPy provides support for broadcasting, which allows arrays of different shapes to be operated on together.

Linear algebra: NumPy provides support for linear algebra operations such as matrix multiplication, decomposition, and solving systems of linear equations.

Fourier transforms: NumPy provides support for Fourier transforms and other spectral analysis functions.

Random number generation: NumPy provides support for generating random numbers from a variety of distributions.

Overall, NumPy is an essential library for scientific computing in Python, and its features make it powerful and versatile for a wide range of tasks.

## 1 Creating a NumPy array:

import numpy as np

#### Create a 1D array
arr1d = np.array([1, 2, 3, 4, 5])

print(arr1d)

#### Create a 2D array
arr2d = np.array([[1, 2, 3], [4, 5, 6]])

print(arr2d)

## 2 Arithmetic operations on NumPy arrays:
import numpy as np

#### Create two arrays
arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

#### Add the two arrays
sum_arr = arr1 + arr2

print(sum_arr)

#### Multiply the two arrays element-wise
prod_arr = arr1 * arr2

print(prod_arr)

## 3 Slicing and indexing NumPy arrays:
import numpy as np

#### Create a 1D array
arr1d = np.array([1, 2, 3, 4, 5])

#### Slice the array to get the first three elements
arr_slice = arr1d[:3]

print(arr_slice)

#### Access a specific element of the array
elem = arr1d[2]

print(elem)

#### Create a 2D array
arr2d = np.array([[1, 2, 3], [4, 5, 6]])

#### Slice the array to get the second row
row = arr2d[1, :]

print(row)

#### Access a specific element of the array
elem = arr2d[0, 1]

print(elem)

## 4 Using built-in NumPy functions:
import numpy as np

#### Create a 1D array
arr1d = np.array([1, 2, 3, 4, 5])

#### Compute the mean of the array
mean = np.mean(arr1d)

print(mean)

#### Compute the standard deviation of the array
std_dev = np.std(arr1d)

print(std_dev)

#### Create a 2D array
arr2d = np.array([[1, 2, 3], [4, 5, 6]])

#### Compute the maximum value of the array
max_val = np.max(arr2d)

print(max_val)

#### Compute the determinant of the array
det = np.linalg.det(arr2d)

print(det)

# Pandas
Pandas is a popular open-source library in Python that provides high-performance data manipulation and analysis tools. It is built on top of the NumPy library and is particularly well-suited for working with structured data.

Here are some key features and functionalities of Pandas:

## Data Structures: 
Pandas introduces two primary data structures, namely Series and DataFrame.

## Series: 
A one-dimensional array-like object that can hold any data type. It is similar to a column in a spreadsheet or a database table.

## DataFrame: 
A two-dimensional tabular data structure that consists of rows and columns. It is similar to a spreadsheet or a SQL table and is the primary data structure used in Pandas. DataFrames allow efficient handling of structured data and provide various operations for data manipulation.

## Data Manipulation: 
Pandas provides a wide range of functions and methods for data manipulation, including:

#### Reading and writing data: 
Pandas can read data from various file formats, such as CSV, Excel, SQL databases, and more. It also supports writing data to these formats.

#### Selection and filtering: 
Pandas allows you to select specific data based on conditions, filter rows or columns, and perform boolean indexing.

#### Data cleaning: 
It provides tools for handling missing data, removing duplicates, and transforming data.

#### Data transformation: 
Pandas offers powerful functions for sorting, grouping, aggregating, merging, and reshaping data.

#### Handling dates and times: 
Pandas has extensive support for working with dates, times, and time series data.

## Data Analysis: 
Pandas includes various statistical and analytical functions for data exploration and analysis, such as:

#### Descriptive statistics: 
Pandas can calculate various statistics like mean, median, standard deviation, etc., for numerical columns.

#### Data visualization: 
It integrates well with other libraries, such as Matplotlib and Seaborn, to create informative plots and visualizations.

#### Time series analysis: 
Pandas provides tools for time-based operations, such as resampling, time shifting, and rolling window calculations.

#### Integration with other libraries: 
Pandas seamlessly integrates with other scientific computing libraries in Python, such as NumPy, Matplotlib, and scikit-learn. This allows you to leverage the strengths of each library for different tasks.

# Univariant and Bivariant
## Univariate Analysis:
Univariate analysis involves examining a single variable or feature in a dataset. This type of analysis aims to understand the distribution, central tendency, and spread of the variable. 
### Example of Univariate Analysis in Python using Pandas and Matplotlib:
import pandas as pd
import matplotlib.pyplot as plt

#### Load data into a DataFrame
data = pd.read_csv('data.csv')

#### Compute basic statistics
print(data.describe())

#### Create a histogram
plt.hist(data['variable'], bins=10)
plt.show()

## Bivariate Analysis:
Bivariate analysis involves analyzing the relationship between two variables in a dataset. It aims to understand how the variables interact or correlate with each other.
### Example of Bivariate Analysis in Python using Pandas and Seaborn:
import pandas as pd
import seaborn as sns

#### Load data into a DataFrame
data = pd.read_csv('data.csv')

#### Compute correlation matrix
correlation_matrix = data.corr()

#### Create a heatmap of correlations
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.show()

These examples demonstrate basic usage for univariate and bivariate analysis in Python using popular libraries. Remember that the specific implementation may vary depending on your dataset and the analysis goals you have in mind.

























