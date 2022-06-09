import threading


print("Let us find the current thread!")

print(threading.current_thread().__getattribute__('name'))

if threading.current_thread() == threading.main_thread():
    print("This is the main thread!")

else:
    print("This is not the main thread!")
