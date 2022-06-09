from threading import Thread, current_thread, Lock
from time import sleep

lock_1 = Lock() # Train - Lock
lock_2 = Lock() # Compartment - Lock


def book_ticket():
    lock_1.acquire()
    print("Book-ticket locked the train.")
    print("Book-ticket wants to lock on compartment.")
    sleep(2)

    lock_2.acquire()
    print("Book-ticket locked the compartment.")
    lock_1.release()
    lock_2.release()
    print("Booking ticket is done!")


def cancel_ticket():
    lock_2.acquire()
    print("Cancel-ticket locked the compartment!")
    print("Cancel-ticket wants to lock on train.")
    sleep(2)

    lock_1.acquire()
    print("Cancel-ticket locked the train!")

    lock_1.release()
    lock_2.release()
    print("Cancelling ticket is done!")


t1 = Thread(target=book_ticket)
t2 = Thread(target=cancel_ticket)

t1.start()
t2.start()
