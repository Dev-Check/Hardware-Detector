import psutil
import platform


memory_info = psutil.virtual_memory()

cpu_freq = psutil.cpu_freq()

os = platform.system()


def cpuinfo():
    name = platform.processor() 
    architecture = platform.architecture() 
    machine_type = platform.machine()  
    freq = psutil.cpu_freq()
    return name, architecture, machine_type, freq

cpu = cpuinfo()
print (f"Machine's given name: {platform.node()}")
print(f"Operating System: {os}\n")
print(f"CPU Info: Name = {cpu[0]}, Architecture = {cpu[1][0]}, Machine = {cpu[2]}")
print("CPU Freq:", cpu[3][0]/1000 , "hz")
print(f"Memory: Total = {memory_info.total / (1024 ** 3):.2f} GB, Available = {memory_info.available / (1024 ** 3):.2f} GB, Used = {memory_info.percent}%")
