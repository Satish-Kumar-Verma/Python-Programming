# import array as ar
#
# my_array = ar.array('i', [1, 2, 3, 4, 5])
#
# print(my_array)
#
# print(type(my_array))

# from array import array
#
# my_array = array('I', [1, 2, 3, 4, 5])
#
# print(my_array)

# Can we create an array from an array?

# from array import array
#
# arr1 = array('i', [1, 2, 3, 4, 5])
#
# # arr2 = array(arr1.typecode, (i * 2 for i in arr1))
# arr2 = array(arr1.typecode, (i ** 2 for i in arr1))
#
# print(arr2)


# Indexing and slicing are same as other iterables

# difference between append() and extend() in lists
# li1 = [1, 2, 3, 4, 5]
# a = li1.copy()
# li2 = [2, 4, 6, 8, 10]
# li1.append(li2)
# print(li1)
# a.extend(li2)
# print(a)

# difference between append() and extend() in arrays

# from array import array
#
# arr = array('i', [1, 2, 3, 4, 5])
#
# arr2 = array('i', [])
#
# print(arr)
# print(arr2)
#
# # arr2.append(arr[0])
# # print(arr2)
#
# arr2.extend(arr)
# print(arr2)
#
# arr[0] = 100
# print(arr2)
# print(arr)

from array import array
# arr = array('i', [1, 2, 3, 4, 5])
#
# arr2 = arr
# print(arr2)
# arr2[0] = 100
# print(arr2)
# print(arr)

# arr = array('i', [1, 2, 3, 4, 5])
# my_list = arr.tolist()
# my_string = arr.tobytes()
#
# arr2 = array('i', my_string)
# # my_unicode = arr.tounicode() # you need to use 'u' (typecode) in order to convert the array into unicode
#
# print(arr)
# print(my_list)
# print(my_string)
# print(arr2)
# # print(my_unicode)
#
#
# # how to print the length of an array
#
# print(len(arr))
#
# print(arr.buffer_info())
#
# print(arr.itemsize)
