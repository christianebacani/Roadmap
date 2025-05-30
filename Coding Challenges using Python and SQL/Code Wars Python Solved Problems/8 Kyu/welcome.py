# Question: Welcome!
# Categories: 8 Kyu

def greet(user_language: str) -> str:
    list_of_welcome_languages = [ 
        ("english", "Welcome"), 
        ("czech", "Vitejte"), 
        ("danish", "Velkomst"), 
        ("dutch", "Welkom"), 
        ("estonian", "Tere tulemast"), 
        ("finnish", "Tervetuloa"), 
        ("flemish", "Welgekomen"), 
        ("french", "Bienvenue"), 
        ("german", "Willkommen"), 
        ("irish", "Failte"), 
        ("italian", "Benvenuto"), 
        ("latvian", "Gaidits"), 
        ("lithuanian", "Laukiamas"), 
        ("polish", "Witamy"), 
        ("spanish", "Bienvenido"), 
        ("swedish", "Valkommen"), 
        ("welsh", "Croeso")
    ]

    for i in range(len(list_of_welcome_languages)):
        language = list_of_welcome_languages[i][0]
        welcome = list_of_welcome_languages[i][1]

        if user_language == language:
            return welcome
    
    return 'Welcome'