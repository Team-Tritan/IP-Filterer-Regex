import re

string = open("xertz_thing.txt", "r").read()

pattern = r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b"
ip_addresses = re.findall(pattern, string)

print(ip_addresses)
