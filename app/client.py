from http import HTTPStatus
import json
from ulid import ULID
from os.path import exists
import requests
from cripto import CriptoClient

# check and create my ID if needed
my_id_file = "./etc/myId.key"
my_id = str(ULID())

try:
    if not exists(my_id_file):
        with open(my_id_file, 'w') as f:
            f.write(my_id)
    else:
        with open(my_id_file, 'r') as f:
            my_id = f.read()

    print(f"SEU ID {my_id}")    
except Exception as e:
    print(f"## Ocorreu um erro ao tentar gerar seu ID: {str(e)}")

headers = {'id': my_id}    


# get public key to encrypt data
key_url = '## URL PARA BAIXAR A CHAVE DE CRIPTOGRAFIA ##'
key_file = "./etc/serverKey.pub"

try:    
    if not exists(key_file):
        key = requests.get(key_url)
        with open(key_file, 'wb') as file:
            file.write(key.content)

except Exception as e:
    print(f"## Ocorreu um erro ao tentar recuperar a chave de criptografia: {str(e)}")
    print(f"## Verifique a URL da chave -> {key_url}")

cripto = CriptoClient(key_file)

# load essay
essay = ""
try:    
    with open("./etc/essay.txt", "r") as e:
        essay = e.read()
except Exception as e:
    print(f"## Ocorreu um erro ao tentar carregar sua redacao: {str(e)}")
    print('## Verifique se sua redacao esta no arquivo ./etc/essay.txt')


# get user info
info = {
    'name': "SEU NOME",
    'email': "SEU EMAIL",
    'phone': "SEU TELEFONE COM DDD",
    'id': my_id,
    'essay': essay
}

print(f"Dados que serao enviados: {json.dumps(info)}")

# prepare data
body = {
    "apply": cripto.encrypt(json.dumps(info))
}

# send data
post_url = '## URL PARA ENVIAR O TESTE ##'

print(f"Tentando executar o envio das informações para {post_url}\nRequest:\n\tHeaders={headers}\n\tBody: {body}")

try:
    response = requests.post(post_url, json=body, headers=headers)
    print(f"HTTP Status Code: {response.status_code}")

    if response.status_code == HTTPStatus.OK:
        print('Legal, seu teste foi aceito! aguarde um contato do pessoal da plataforma nos dados que vc acabou de nos enviar!')
    else:
        print('## Ocorreu um erro ao tentar enviar o seu teste, por favor revise as instrucoes e tente novamente')

except Exception as e:
    print(f"## Ocorreu um erro ao tentar enviar seu teste: {str(e)}")
    print(f"## Verifique a URL para enviar -> {post_url}")

print('Fim do programa')
