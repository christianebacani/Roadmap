# Question: Catalog
# Categories: 6 Kyu

def catalog(s: str, article: str) -> str:
    s = s.split('</prod>')

    for i in range(len(s)):
        s[i] = s[i].strip()
    
    result = []

    for i in range(len(s)):
        if article not in s[i]:
            continue

        product = s[i]
        product = product.replace('<prx>', ', prx: ').replace('</prx>', '')
        product = product.replace('<qty>', ', qty: ').replace('</qty>', '')
        product = product.replace('<prod><name>', 'product_name: ')
        product = product.replace('</name>', '')

        # Format: product_name: ladder, prx: 112, qty: 12
        result.append(product)
    
    for i in range(len(result)):
        product = result[i]
        product = str(product).split(', ')

        product[0] = product[0].replace('product_name: ', '')
        product[0] = product[0] + ' >'

        product[1] = product[1].replace('prx: ', 'prx: $')

        product = ' '.join(product)
        result[i] = product

    result = '\r\n'.join(result)

    if result == '':
        return 'Nothing'
    
    return result