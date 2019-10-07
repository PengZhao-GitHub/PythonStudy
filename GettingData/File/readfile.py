


def get_domain(email_address):
    return email_address.lower().split('@')[-1]

with open('email_addresses.txt', 'r') as f:
    for line in f:
        if "@" in line:
            print get_domain(line.strip())