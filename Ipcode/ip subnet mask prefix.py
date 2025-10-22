netmask_prefix = {
    '255.255.255.255': '/32',
    '255.255.255.254': '/31',
    '255.255.255.252': '/30',
    '255.255.255.248': '/29',
}
def get_number_ip_addresses(p_prefix):
    pbits = 32-int(p_prefix[1:])
    return 2 ** pbits

def get_number_ip_hosts(p_prefix):
    p_bits = get_number_ip_addresses(p_prefix)
    return pbits - 2

def get_net_prefix(p_subnet_mask):
    try:
        prefix = netmask_prefix[p_subnet_mask]
        return prefix
    except:
        return "wrong input: garbage in, garbage out"
result = get_net_prefix('255.255.255.254')
print(result)