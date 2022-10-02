# Plataforma Impact - Teste de aceitação
## Instruções

* Instale o git 
  * Windows
    ```
    https://git-scm.com/download/windows
    ```
  * Linux
    ```
    https://git-scm.com/download/linux
    ```
* Clone o repositório
  ```  
  cd /Desktop
  git clone git@github.com:Impact-Plataform/Processo-Seletivo.git
  cd Processo-Seletivo/ 
  ```
* Alterar app/client.py
  * URL DA CHAVE -> http://localhost:5000/key
  * LINHA 37 -> Nome
  * LINHA 38 -> Email
  * LINHA 39 -> Telefone com DDD **(ex: 21987438328)**
  * URL DO POST -> http://localhost:5000/apply
* Instalar o Python3
  * Windows
    ```
    https://git-scm.com/download/windows
    ```
  * Linux
    ```
    sudo apt-get update && apt-get install python3.6
    ```

* Executar o pip
  ```
  pip3 install -r requirements.txt
  ```
* Preencher /etc/essay.txt com um texto do pq vc gostaria de entrar na Plataforma
* Run app
  * Abra o terminal e execute:
  ```
  ./run.sh
  ```
* Enviar os dados
