#Valid email addresses must follow these rules:
import re


# It must have the username@websitename.extension format type.
# The username can only contain letters, digits, dashes and underscores .
# The website name can only have letters and digits .
# The extension can only contain letters .
# The maximum length of the extension is 3.

# function with regex

def fun(s):
    pattern = r"^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$"
    return bool(re.match(pattern, s))


def filter_mail(emails):
    return list(filter(fun, emails))


n = int(input().strip())
emails =[input().strip() for _ in range(n)]

filtered_emails = filter_mail(emails)

# order by alphabetical order
filtered_emails.sort()
print(filtered_emails)


