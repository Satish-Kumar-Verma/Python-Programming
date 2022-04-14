
import logging

# logging.basicConfig(filename="logs.txt", level=logging.ERROR)
#
# logging.critical("Critical ERROR!")
# logging.error("Error!")
# logging.warning("Warning!")
# logging.info("INFO")
# logging.debug("DEBUG")

logging.basicConfig(filename="logs.txt", level=logging.NOTSET)

try:
    a, b = tuple(map(int, input().split()))
    print(a / b)

except Exception as e:
    logging.exception(e)
