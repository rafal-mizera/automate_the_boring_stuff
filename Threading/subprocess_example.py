import subprocess

calc_process = subprocess.Popen("C:\\Windows\\System32\\calc.exe")
print(calc_process.poll() == None)
print(calc_process.wait())
print(calc_process.poll())

subprocess.Popen([r"C:\Users\RMZ\AppData\Local\Programs\Python\Python38-32\python.exe","thread_demo.py"])

file = open("hello.txt","w")
file.write("hello!")
file.close()

subprocess.Popen(["start","hello.txt"],shell=True)