# References
# https://medium.com/@ashiqgiga07/asymmetric-cryptography-with-python-5eed86772731
#

import base64
import os
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.backends import default_backend
from cryptography.exceptions import AlreadyFinalized
from cryptography.exceptions import InvalidTag
from cryptography.exceptions import UnsupportedAlgorithm
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


class CriptoServer:
    def __init__(self, key_path:str):
        if not os.path.exists(key_path):
            os.mkdir(key_path)

        self._pr_name = 'private_key.pem'
        self._pu_name = 'public_key.pem'

        self._pr_path = f"{key_path}/{self._pr_name}"
        self._pu_path = f"{key_path}/{self._pu_name}"

        if not os.path.isfile(self._pr_path):
            # create keys
            self._key = rsa.generate_private_key(
                backend=default_backend(),
                public_exponent=65537,
                key_size=2048
            )

            with open(self._pr_path, 'wb') as pr:
                pr.write(self._key.private_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PrivateFormat.PKCS8,
                    encryption_algorithm=serialization.NoEncryption()
                ))

            with open(self._pu_path, 'wb') as pu:
                pu.write(self._key.public_key().public_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PublicFormat.SubjectPublicKeyInfo
                ))
        else:
            with open(self._pr_path, 'rb') as key_file:
                self._key = serialization.load_pem_private_key(
                    key_file.read(),
                    password=None,
                    backend=default_backend()
                )

        self._padding = padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )

    def decrypt(self, message: str):
        base64_bytes = message.encode('ascii')
        message_bytes = base64.b64decode(base64_bytes)
        return self._key.decrypt(message_bytes, self._padding).decode('utf-8')

    def get_private(self):
        return self._key

    def get_public(self):
        return self._key.public_key()

    def get_private_path(self):
        return self._pr_path

    def get_public_path(self):
        return self._pu_path

    def get_private_name(self):
        return self._pr_name

    def get_public_name(self):
        return self._pu_name


class CriptoClient:
    def __init__(self, key_path: str):
        self._pu_path = key_path
        if not os.path.isfile(self._pu_path):
            raise Exception(f"We need a public key on {self._pu_path} to continue")

        with open(self._pu_path, 'rb') as key_file:
            self._key = serialization.load_pem_public_key(
                key_file.read(),
                backend=default_backend()
            )

        self._padding = padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )

    def encrypt(self, message: str):
        encrypt = self._key.encrypt(message.encode('utf-8'), self._padding)
        base64_bytes = base64.b64encode(encrypt)
        return base64_bytes.decode('ascii')

    def get_key(self):
        return self._key

    def get_path(self):
        return self._pu_path

class SymmetricCripto:
    def encrypt(secret_key: str, data: str):
        try:            
            secret_key
            kdf = PBKDF2HMAC(
                algorithm=hashes.SHA512(),
                length=32,
                salt=bytes(secret_key, 'utf-8'),
                iterations=10000,
                backend=default_backend()
            )
            key = kdf.derive(secret_key.encode('utf-8'))

            nonce = secret_key.encode('utf-8')

            aesgcm = AESGCM(key)
            cipher_text_bytes = aesgcm.encrypt(
                nonce=nonce,
                data=data.encode('utf-8'),
                associated_data=None
            )
            return base64.urlsafe_b64encode(cipher_text_bytes).decode('utf-8')

        except (UnsupportedAlgorithm, AlreadyFinalized, InvalidTag) as e:
            print(f"Symmetric encryption failed: {str(e)}")

        return None

    def decrypt(secret_key: str, data: str):
        try:
            salt = os.urandom(64)
            kdf = PBKDF2HMAC(
                algorithm=hashes.SHA512(),
                length=32,
                salt=bytes(secret_key, 'utf-8'),
                iterations=10000,
                backend=default_backend()
            )
            key = kdf.derive(secret_key.encode('utf-8'))

            nonce = secret_key.encode('utf-8')

            aesgcm = AESGCM(key)

            decrypted_cipher_text_bytes = aesgcm.decrypt(
                nonce=nonce,
                data=base64.urlsafe_b64decode(data),
                associated_data=None
            )
            return decrypted_cipher_text_bytes.decode('utf-8')
        except (UnsupportedAlgorithm, AlreadyFinalized, InvalidTag) as e:
            print(f"Symmetric decryption failed: {str(e)}")

        return None
        
