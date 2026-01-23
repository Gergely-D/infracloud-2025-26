import sys
import requests

def main():
    print("Python executable:", sys.executable)
    print("Requests version:", requests.__version__)

    r = requests.get("https://httpbin.org/get", timeout=10)
    print("HTTP status:", r.status_code)
    print("Origin:", r.json().get("origin"))

if __name__ == "__main__":
    main()
