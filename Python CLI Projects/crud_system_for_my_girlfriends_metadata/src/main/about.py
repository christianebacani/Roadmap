'''
    About Module
'''
def about_page() -> None:
    '''
        CLI-Based About Page
    '''
    # Display header
    header = 'About Rica\'s Metadata CLI Manager'
    print(f'\t\t{header}')

    print()

    # Display text body
    body = [
        'Welcome to Rica\'s Metadata CLI Manager—a command-line-based CRUD (Create, Read, Update, Delete)',
        'system designed to organize and manage metadata in a structured star schema. This tool allows you to',
        'effortlessly create, edit, and delete tables while maintaining the integrity of your existing star schema,',
        'which stores meaningful metadata about my amazing girlfriend, Rica'
    ]
    for text_body in body:
        print(f'\t\t{text_body}')
    
    print()
    print('\t\tKey Features:')
    print()

    key_features = [
        '✨ Create New Tables – Define and add new metadata tables to Rica\'s star schema.',
        '✏️  Edit Existing Tables – Modify table structures or update metadata entries with ease.',
        '🗑️  Delete Tables – Remove outdated or unnecessary tables while preserving schema consistency.',
        '🔍 Star Schema Support – Ensures data relationships remain intact for efficient querying and analysis.'
    ]
    
    for key_feature in key_features:
        print(f'\t\t{key_feature}')

    input('\n\t\tPress any key to exit: ')