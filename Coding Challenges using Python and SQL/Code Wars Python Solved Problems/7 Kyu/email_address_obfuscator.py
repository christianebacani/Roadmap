# Question: Email Address Obfuscator
# Categories: 7 Kyu

def obfuscate(email: str) -> str:
    email = email.replace('@', ' [at] ')
    email = email.replace('.' , ' [dot] ')
    return email