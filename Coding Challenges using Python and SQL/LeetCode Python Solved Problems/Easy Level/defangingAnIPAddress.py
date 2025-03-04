# 1108.) Defanging an IP Address
# Categories : String

class Solution:
    def defangIPaddr(self, address: str) -> str:
        defanged_ip_add = address.replace('.', '[.]')
    
        return defanged_ip_add
