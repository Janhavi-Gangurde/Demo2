import os
import platform

def process_related_sys_calls():
    print("Process Related System Calls:")
    if platform.system() == "Windows":
        print("Sorry, fork is not available on Windows.")
    else:
        pid = os.fork()
        if pid > 0:
            print("Parent Process (PID: {})".format(os.getpid()))
            os.wait()  
            print("Parent Process Exiting")
        elif pid == 0:
            print("Child Process (PID: {})".format(os.getpid()))
            print("Child Process Exiting")

def file_related_sys_calls():
    print("\nFile Related System Calls:")
    file_descriptor = os.open("example.txt", os.O_CREAT | os.O_WRONLY)
    os.write(file_descriptor, b"Hello, this is a sample text.")
    os.close(file_descriptor)

    file_descriptor = os.open("example.txt", os.O_RDONLY)
    data = os.read(file_descriptor, 100)
    print("Read from file:", data.decode())
    os.close(file_descriptor)

def protection_related_sys_call():
    print("\nProtection Related System Call:")
    with open("example_file.txt", "w") as file:
        file.write("This is a sample file.")

    current_permissions = os.stat("example_file.txt").st_mode
    new_permissions = current_permissions | 0o100
    os.chmod("example_file.txt", new_permissions)
    print("File permissions updated.")

if __name__ == "__main__":
    process_related_sys_calls()
    file_related_sys_calls()
    protection_related_sys_call()
