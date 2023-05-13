import jwt

payload_data = {
    "sub": "4242",
    "name": "Jessica Temporal",
    "nickname": "Jess"
}

my_secret = 'my_super_secret'

# first import the module
from cryptography.hazmat.primitives import serialization
# read and load the key
private_key = open('.ssh/id_rsa', 'r').read()
print(private_key)
key = serialization.load_ssh_private_key(private_key.encode(), password=b'')

new_token = jwt.encode(
    payload=payload_data,
    key=key,
    algorithm='RS256'
)

print(new_token)