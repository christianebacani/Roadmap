# Question: Unix command line `ls -l` extract the file type
# Categories: 7 Kyu

def linux_type(file_attribute: str) -> str:
    command_and_file_type = {
        '-': 'file',
        'd': 'directory',
        'l': 'symlink',
        'c': 'character_file',
        'b': 'block_file',
        'p': 'pipe',
        's': 'socket',
        'D': 'door'
    }

    return command_and_file_type[file_attribute[0]]