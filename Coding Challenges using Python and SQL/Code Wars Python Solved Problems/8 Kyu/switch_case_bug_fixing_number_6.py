# Question: Switch/Case - Bug Fixing #6
# Categories: 8 Kyu

def eval_object(v: dict[str, int]) -> int:
    operation = {
        '+': v['a'] + v['b'],
        '-': v['a'] - v['b'],
        '*': v['a'] * v['b'],
        '/': v['a'] / v['b'],
        '%': v['a'] % v['b'],
        '**': v['a'] ** v['b']
    }

    return operation[v['operation']]