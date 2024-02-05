# What is NumPy?
1. NumPy is a Python library used for working with arrays.

2. It also has functions for working in domain of linear algebra, fourier transform, and matrices.

3. NumPy was created in 2005 by Travis Oliphant. 

4. It is an open source project and you can use it freely.

5. NumPy stands for Numerical Python.

# Installation of NumPy
If you have Python and PIP already installed on a system, then installation of NumPy is very easy.

Install it using this command:

` C:\Users\Your Name>pip install numpy `

# Import NumPy
Once NumPy is installed, import it in your applications by adding the import keyword:

` import numpy `

# NumPy as np
NumPy is usually imported under the np alias

# Create an alias with the as keyword while importing:

`import numpy as np`

# Checking NumPy Version
The version string is stored under __version__ attribute.
`
import numpy as np
print(np.__version__)

`
# Create a NumPy ndarray Object
```
import numpy as np
arr = np.array([1,2,3,4,5,6])
print(arr)
```
#  tuple to create a NumPy array
```
import numpy as np
arr = np.array((1,2,3,4,5,6))
print(arr)
```
#  tuple to create a NumPy array
```
import numpy as np
arr = np.array((1, 2, 3, 4, 5))
print(arr)
```
# Create a 0-D array with value 42
```
import numpy as np
arr = np.array(42)
print(arr)
print(type(arr))
```
# Create a 1-D array containing the values 1,2,3,4,5:
```
import numpy as np
arr = np.array([1,2,3,4,5])
print(arr)
```
# Create a 2-D array containing two arrays with the values 1,2,3 and 4,5,6:
```
import numpy as np
arr = np.array([[1,2,3],[4,5,6]])
print(arr)
```
# Check how many dimensions the arrays
```
import numpy as np
a = np.array(42)
b = np.array([1,2,3,4,5])
c = np.array([[1,2,3],[4,5,6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)
```