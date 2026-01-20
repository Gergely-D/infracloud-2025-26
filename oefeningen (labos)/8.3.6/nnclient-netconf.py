from ncclient import manager
import xml.dom.minidom

HOST = "192.168.56.102"
PORT = 830
USERNAME = "cisco"
PASSWORD = "cisco123!"

def pretty(xml_str: str) -> str:
    return xml.dom.minidom.parseString(xml_str).toprettyxml()

# Connect (extra opties vermijden SSH key/agent issues + langere timeout)
m = manager.connect(
    host=HOST,
    port=PORT,
    username=USERNAME,
    password=PASSWORD,
    hostkey_verify=False,
    allow_agent=False,
    look_for_keys=False,
    timeout=120,
    device_params={"name": "csr"},
)

# -------------------------------------------------
# Part 3 – Show supported YANG capabilities
# -------------------------------------------------
print("# Supported NETCONF Capabilities:\n")
for capability in m.server_capabilities:
    print(capability)

# -------------------------------------------------
# Part 4 – Retrieve configuration (safe approach)
# -------------------------------------------------
print("\n# Running configuration retrieval:\n")

# Kleine filter (veilig) – voorkomt timeouts
small_filter = """
<filter>
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <hostname/>
  </native>
</filter>
"""

try:
    # Sommige images geven "application protocol error" op get-config running
    netconf_reply = m.get_config(source="running")
    print("# get-config running succeeded\n")
    print(pretty(netconf_reply.xml))
except Exception as e:
    print("# get-config running failed; using filtered <get> instead")
    print(f"Reason: {e}\n")
    netconf_reply = m.get(filter=small_filter)
    print(pretty(netconf_reply.xml))

# -------------------------------------------------
# Retrieve only Cisco IOS-XE Native YANG model (filtered)
# -------------------------------------------------
# Let op: <native/> zonder children kan nog groot zijn; beperk tot hostname + interface
netconf_filter = """
<filter>
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <hostname/>
    <interface/>
  </native>
</filter>
"""

print("\n# Filtered configuration (IOS-XE native - hostname + interface):\n")
netconf_reply = m.get(filter=netconf_filter)
print(pretty(netconf_reply.xml))

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
print(pretty(netconf_reply.xml))

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
print(pretty(netconf_reply.xml))

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
    print("Unexpected: duplicate loopback succeeded (should fail).")
except Exception as e:
    print("Expected NETCONF error:")
    print(e)

m.close_session()
