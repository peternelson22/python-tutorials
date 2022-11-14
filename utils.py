from cryptography.fernet import Fernet
from prime import *

user = name
passwd = password

key = Fernet.generate_key()
keygen = Fernet(key)

eu = keygen.encrypt(user.encode())
ep = keygen.encrypt(passwd.encode())

owner = '***NELSON***'
name = '$MaVerick Vault**'