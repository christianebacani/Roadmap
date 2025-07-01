# 1800A - Is It a Cat?

import re

t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    s = input().strip()
    s = s.lower()

    if re.search(r'^(m){1,}(e){1,}(o){1,}(w){1,}$', s):
        print('YES')
    
    else:
        print('NO')