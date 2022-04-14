

# class Testing:
#     def __init__(self, var):
#         self.__my_private_var = var
#         self._protected = var + 4
#
#     def __get_val(self):
#         return self.__my_private_var
#
#     def get_value(self):
#         return self.__my_private_var
#
#     def get_pro(self):
#         return self._protected

# t = Testing(5)
# print(t.__my_private_var)
# print(t.my_private_var)
# print(t.__get_val())

# print(t.get_value())
# print(t._protected)


class Test:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name


t = Test("Hi")

print(t.get_name())
print(t._name)
