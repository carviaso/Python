import os
import configparser
from cryptography.fernet import Fernet

# Definir la clave de encriptación como variable global
encryption_key = None

# Función para encriptar una cadena
def encrypt_value(value):
    cipher_suite = Fernet(encryption_key)
    encrypted_value = cipher_suite.encrypt(value.encode())
    return encrypted_value.decode()

# Función para desencriptar una cadena
def decrypt_value(encrypted_value):
    cipher_suite = Fernet(encryption_key)
    decrypted_value = cipher_suite.decrypt(encrypted_value.encode())
    return decrypted_value.decode()

# Crear el objeto configparser
config = configparser.ConfigParser()

# Leer la clave de encriptación desde un archivo o cualquier otra fuente
def read_encryption_key():
    global encryption_key
    # Lógica para leer la clave de encriptación
    # Por ejemplo, desde un archivo o una variable de entorno
    encryption_key = b'abcdefghijklmnopqrstuvwxyz123456'  # Ejemplo: clave de encriptación estática


# Cargar la clave de encriptación desde una variable de entorno
def load_encryption_key():
    global encryption_key
    encryption_key = os.environ.get('ENCRYPTION_KEY')


# Agregar valores encriptados al archivo INI
def add_encrypted_values():
    config['Section1'] = {
        'key1': encrypt_value('value1'),
        'key2': encrypt_value('value2')
    }


# Guardar el archivo INI
def save_config_file():
    with open('config.ini', 'w') as config_file:
        config.write(config_file)


# Leer el archivo INI y desencriptar los valores
def read_config_file():
    config.read('config.ini')
    value1_encrypted = config.get('Section1', 'key1')
    value2_encrypted = config.get('Section1', 'key2')

    value1_decrypted = decrypt_value(value1_encrypted)
    value2_decrypted = decrypt_value(value2_encrypted)

    # Imprimir los valores desencriptados
    print(value1_decrypted)
    print(value2_decrypted)


# Llamar a las funciones en el orden adecuado
read_encryption_key()
add_encrypted_values()
save_config_file()
read_config_file()
