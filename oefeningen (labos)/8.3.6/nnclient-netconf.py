from ncclient import manager
import xml.dom.minidom

# NETCONF connection parameters
HOST = "192.168.56.101"
PORT = 830
USERNAME = "cisco"
PASSWORD = "cisco123!"

# Connect to the device
m = manager.connect(
    host=HOST,
    port=PORT,
    username=USERNAME,
    password=PASSWORD,
    hostkey_verify=False
)

# -------------------------------------------------
# Part 3 – Show supported YANG capabilities
# -------------------------------------------------
print("# Supported NETCONF Capabilities:\n")
for capability in m.server_capabilities:
    print(capability)

# -------------------------------------------------
# Part 4 – Retrieve full running configuration
# -------------------------------------------------
print("\n# Full running configuration:\n")
netconf_reply = m.get_config(source="running")
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

# -------------------------------------------------
# Retrieve only Cisco IOS-XE Native YANG model
# -------------------------------------------------
netconf_filter = """
<filter>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native"/>
</filter>
"""

print("\n# Filtered running configuration (IOS-XE native):\n")
netconf_reply = m.get_config(source="running", filter=netconf_filter)
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

# -------------------------------------------------
# Part 5 – Change hostname
# -------------------------------------------------
netconf_hostname = """
<config>
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
     <hostname>CSR1kv</hostname>
  </native>
</config>
"""

print("\n# Changing hostname:\n")
netconf_reply = m.edit_config(target="running", config=netconf_hostname)
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

# -------------------------------------------------
# Create Loopback1
# -------------------------------------------------
netconf_loopback = """
<config>
 <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
  <interface>
   <Loopback>
    <name>1</name>
    <description>My NETCONF loopback</description>
    <ip>
     <address>
      <primary>
       <address>10.1.1.1</address>
       <mask>255.255.255.0</mask>
      </primary>
     </address>
    </ip>
   </Loopback>
  </interface>
 </native>
</config>
"""

print("\n# Creating Loopback1:\n")
netconf_reply = m.edit_config(target="running", config=netconf_loopback)
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

# -------------------------------------------------
# Attempt duplicate Loopback (expected failure)
# -------------------------------------------------
netconf_newloop = """
<config>
 <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
  <interface>
   <Loopback>
    <name>2</name>
    <description>Duplicate IP loopback</description>
    <ip>
     <address>
      <primary>
       <address>10.1.1.1</address>
       <mask>255.255.255.0</mask>
      </primary>
     </address>
    </ip>
   </Loopback>
  </interface>
 </native>
</config>
"""

print("\n# Attempting duplicate Loopback (expected error):\n")
try:
    m.edit_config(target="running", config=netconf_newloop)
except Exception as e:
    print("Expected NETCONF error:")
    print(e)

# Close NETCONF session
m.close_session()
