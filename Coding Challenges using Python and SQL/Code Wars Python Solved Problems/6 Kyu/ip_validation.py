# Question: IP Validation
# Categories: 6 Kyu

def is_valid_IP(ip_address: str) -> bool:
    ip_address = ip_address.split('.')

    if len(ip_address) != 4 or ip_address == '':
        return False

    for i in range(len(ip_address)):
        if ip_address[i] == '0':
            continue
        
        if not ip_address[i].isnumeric():
            return False
        
        if ip_address[i].startswith('0'):
            return False
        
        if int(ip_address[i]) not in range(256):
            return False

    return True