import threading
import time

# print("Start program")
#
# def takeNap():
#     time.sleep(5)
#     print("Wake up!!!")
#
# thread_obj = threading.Thread(target=takeNap)
# thread_obj.start()
#
# print("End of program")

thread_obj = threading.Thread(target=print,args=["dogs","cats","frogs"],kwargs={"sep": " & "})
thread_obj.start()
print("haha")