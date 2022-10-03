from http import HTTPStatus
import json
from ulid import ULID
from os.path import exists
import requests
from cripto import CriptoClient

# check and create my ID if needed
my_id_file = "./etc/myId.key"
my_id = str(ULID())
if not exists(my_id_file):
    with open(my_id_file, 'w') as f:
        f.write(my_id)
else:
    with open(my_id_file, 'r') as f:
        my_id = f.read()

print(f"SEU ID {my_id}")
headers = {'id': my_id}

# get public key to encrypt data
key_url = '## URL PARA BAIXAR A CHAVE DE CRIPTOGRAFIA ##'
key_file = "./etc/serverKey.pub"

if not exists(key_file):
    key = requests.get(key_url)
    with open(key_file, 'wb') as file:
        file.write(key.content)

cripto = CriptoClient(key_file)

# load essay
with open("./etc/essay.txt", "r") as e:
    essay = e.read()

# get user info
info = {
    'name': "SEU NOME",
    'email': "SEU EMAIL",
    'phone': "SEU TELEFONE COM DDD",
    'id': my_id,
    'essay': essay
}

# prepare data
body = {
    "apply": cripto.encrypt(json.dumps(info))
}

# send data
post_url = '## URL PARA ENVIAR O TESTE ##'

print(f"Request:\n\tHeaders={headers}\n\tBody: {body}")

response = requests.post(post_url, json=body, headers=headers)
print(f"HTTP Status Code: {response.status_code}")

if response.status_code == HTTPStatus.OK:
    print('Legal, seu teste foi aceito! aguarde um contato do pessoal da plataforma!')
