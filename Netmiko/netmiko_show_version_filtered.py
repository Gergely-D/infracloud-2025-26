import datetime
print ("Current date and time: ")
print(datetime.datetime.now())
print("Connecting via SSH => show version")
#
from netmiko import ConnectHandler
### VAR

### EXEC
sshCli = ConnectHandler(
    device_type="cisco_ios",
    host="192.168.56.102",
    port="22",
    username="cisco",
    password="cisco123!"
    )
output=sshCli.send_command("show version")
for line in output.splitlines():
    if 'Cisco IOS Software' in line:
        ios_version = line.strip()
    elif 'uptime' in line:
        hostname = line.split()[0]
        sys_uptime = line    
    elif 'interface' in line:
        num_interfaces = line.split()[0]
print("IOS Version")
print(ios_version)
print("Hostname")
print(hostname)
print("System uptime")
print(sys_uptime)
print("Number of Interfaces")
print(num_interfaces)

import pandas as pd

# Maak een DataFrame met de opgehaalde gegevens
data = {
    "Datum": [datetime.datetime.now()],
    "Hostname": [hostname],
    "IOS_Versie": [ios_version],
    "Uptime": [sys_uptime],
    "Interfaces": [num_interfaces]
}

df = pd.DataFrame(data)

# Opslaan naar Excel
excel_file = "cisco_systeeminfo.xlsx"
df.to_excel(excel_file, index=False)

print(f"✅ Gegevens opgeslagen in {excel_file}")