#-loopback maken
from netmiko import ConnectHandler
IP_ADDRESS = "192.168.56.102" 
sshCli = ConnectHandler(
    device_type="cisco_ios",
    host=IP_ADDRESS,
    port=22,
    
    username="cisco",
    password="cisco123!"
    )
config_commands = (
    'interface loopback 501' , 'ip address 10.1.0.105 255.255.255.0'
    )
print("=== HUIDIGE INTERFACE STATUS (voor configuratie) ===")
output = sshCli.send_command("show ip interface brief")
print(output)

print("=== INTERFACE CONFIGURATIE WORDT TOEGEPAST ===")
output = sshCli.send_config_set(config_commands)
print(output)

print("=== INTERFACE STATUS NA CONFIGURATIE ===")
output = sshCli.send_command("show ip interface brief")
print(output)
