# Array is a collection of items of same type. Syntax : array ( datatype , valuelist )
# We need to import array from array module to create array in python.

#       Type code         C Type
#         'b'         signed integer
#         'B'         unsigned integer
#         'u'         Unicode character
#         'h'         signed integer
#         'H'         unsigned integer
#         'i'         signed integer
#         'I'         unsigned integer
#         'l'         signed integer
#         'L'         unsigned integer
#         'q'         signed integer
#         'Q'         unsigned integer
#         'f'         floating point
#         'd'         floating point
import array as arr

a = arr.array('i', [1, 2, 3, 4]) # It is the array of integers
b = arr.array('f', [1.2, 4.5, 2e3]) # It is the array of floats

print(a)
print(b)
print(type(a))

# To learn more about array please refer Numpy pdf.
