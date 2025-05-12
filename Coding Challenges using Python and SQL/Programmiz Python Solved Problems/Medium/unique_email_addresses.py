# Question Name: Write a function to count the number of unique email addresses
# Categories: Medium

def count_unique_emails(emails: list[str]) -> int:
    return len(set(emails))