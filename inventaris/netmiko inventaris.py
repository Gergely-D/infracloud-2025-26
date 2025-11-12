import datetime
print ("Current date and time: ")
print (datetime.datetime.now())
print("connecting via SSH => show version")
from netmiko import ConnectHandler
sshCli = ConnectHandler(
    device_type="cisco_ios",
    host="10.102.34.4",
    port="22",
    username="cisco",
    password="cisco123!"
    )
output=sshCli.send_command("show version")
print(output)