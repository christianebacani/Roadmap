# 929.) Unique Email Addresses
# Categories: Array, Hash Table, String

class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        distinct_addresses = []

        for i in range(len(emails)):
            local_name = ''

            for j in range(len(emails[i])):
                if emails[i][j] in ['@', '+']:
                    break

                else:
                    local_name += emails[i][j]

            domain_name = '@' + str(emails[i]).split('@')[1]
            local_name = local_name.replace('.', '')
            email_address = local_name + domain_name

            if email_address not in distinct_addresses:
                distinct_addresses.append(email_address)

        return len(distinct_addresses)