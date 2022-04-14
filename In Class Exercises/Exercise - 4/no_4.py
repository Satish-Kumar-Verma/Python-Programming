tp = tuple(input("Tuple : ").split())

tp_list = list(tp)

tp_list.remove(tp[0])
tp_list.remove(tp[4])
tp_list.remove(tp[5])

tp = tuple(tp_list)
print(tp)