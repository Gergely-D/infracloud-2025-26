import requests
from datetime import datetime

def main():
    # Huidige datum en tijd ophalen
    now = datetime.now()
    print("Datum en tijd:", now.strftime("%Y-%m-%d %H:%M:%S"))

    try:
        # IP-info ophalen via de API
        response = requests.get("https://api.myip.com", timeout=5)
        response.raise_for_status()  # Controleer op HTTP-fouten

        data = response.json()
        print(f"IP-adres: {data['ip']}")
        print(f"Land: {data['country']}")
        print(f"Landcode: {data['cc']}")

    except requests.RequestException as e:
        print("Fout bij ophalen van IP-info:", e)

if __name__ == "__main__":
    main()
