import platform
import psutil

def get_os_info():
    print("Operating System:")
    print(platform.system(), platform.release())
    print()

def get_cpu_info():
    print("CPU Information:")
    print(f"Processor: {platform.processor()}")
    print(f"Architecture: {platform.architecture()[0]}")
    print()

def get_memory_info():
    print("Memory Information:")
    mem = psutil.virtual_memory()
    print(f"Total: {format_size(mem.total)}")
    print(f"Available: {format_size(mem.available)}")
    print()

def get_storage_info():
    print("Storage Information:")
    partitions = psutil.disk_partitions()
    for partition in partitions:
        partition_info = psutil.disk_usage(partition.mountpoint)
        print(f"{partition.device} - Total: {format_size(partition_info.total)} | Free: {format_size(partition_info.free)}")
    print()

def get_process_info():
    print("Process Information:")
    for process in psutil.process_iter(['pid', 'name', 'username']):
        print(process.info)
    print()

def format_size(size):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024.0:
            return f"{size:.1f} {unit}"
        size /= 1024.0

def main():
    get_os_info()
    get_cpu_info()
    get_memory_info()
    get_storage_info()
    get_process_info()

if __name__ == "__main__":
    main()



