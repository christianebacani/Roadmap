import pandas as pd

def find_invalid_ips(logs: pd.DataFrame) -> pd.DataFrame:
    output_df = pd.DataFrame(columns=['ip', 'invalid_count'])
    ip_lst = list(set(logs['ip']))

    for ip in ip_lst:
        containsNumGreaterThan255 = False
        containsLeadingZero = False
        notEqualToFourOctets = False
        octets = ip.split('.')

        for octet in octets:
            if int(octet) > 255:
                containsNumGreaterThan255 = True

            if octet[0] == '0':
                containsLeadingZero = True
        
        if len(octets) != 4:
            notEqualToFourOctets = True
        
        if (any([containsNumGreaterThan255, containsLeadingZero, notEqualToFourOctets])):
            invalid_count = 0
            for inner_ip in list(logs['ip']):
                if ip == inner_ip:
                    invalid_count += 1

            output_df = pd.concat([output_df, pd.DataFrame({'ip' : ip, 'invalid_count' : invalid_count}, index=[0])], ignore_index=True)
    
    output_df.sort_values(by=['invalid_count', 'ip'], ascending=[False, False], inplace=True)

    return output_df