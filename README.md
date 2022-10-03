# Plataforma Impact - Teste de aceitação
Olá! Criamos um pequeno teste, para servir como validação inicial para os novos alunos da Plataforma Impact.

Nosso objetivo com esse teste é saber se vc está preparado para começar a estudar e se desenvolver cada vez mais!

Siga as instruções abaixo e caso você consiga fazer esse pequeno código funcionar, ele irá nos enviar sua inscrição e vamos conversar!

## Instruções
### Instale o git 
Siga as intruções do site oficial do git e instale em seu computador essa ferramenta, ela é necessária para que você tenha acesso ao programa de teste
* [Windows](https://git-scm.com/download/windows)
* [Linux](https://git-scm.com/download/linux)

### Agora clone o repositório
"Clonar o repositório" é como usualmente dizemos quando queremos pegar um código fonte e baixar para o nosso computador, é um passo importante do nosso teste:

Primeiro crie uma pasta/diretório em algum local do seu computador, recomendamos usar uma pasta dedicada para isso, com um nome intuítivo, como "git", por exemplo.

Execute um comando de cada vez no seu terminal/prompt de comando para conseguir baixar todos os arquivos do teste
#### Windows: 
```  
cd %HOMEPATH%
mkdir git
cd git
git clone http://github.com/Impact-Plataform/Processo-Seletivo.git
cd Processo-Seletivo/ 
```

#### Linux: 
```  
cd ~
mkdir git
cd git
git clone http://github.com/Impact-Plataform/Processo-Seletivo.git
cd Processo-Seletivo/ 
```

### Vamos alterar alguns pontos para fazer esse programa funcionar?
Usando o seu editor de texto/códigos preferidos, vá até o arquivo <b>app/client.py</b>, é nele que precisamos colocar algumas informações importantes!

Você precisa alterar algumas linhas específicas para sabermos quem é você e saber se você consegue seguir corretamente essas instruções:

|Linha|Descrição|Valor no arquivo|Novo valor|
|:-:|:-:|:-:|:-:|
|22|Caminho para buscar a chave de criptografia|key_url = '## URL PARA BAIXAR A CHAVE DE CRIPTOGRAFIA ##'|key_url = 'http://impact-server.com/key'|
|38|Precisamos do seu nome|'name': "SEU NOME",|'name': "fulano afim de estudar",|
|39|Precisamos do seu e-mail|'email': "SEU EMAIL",|'email': "fulano@email.com",|
|34|Precisamos do seu telefone|'phone': "SEU TELEFONE COM DDD",|'phone': "(21) 98888-7777",|
|51|Caminho para que esse programa consiga nos enviar os resultados e seus dados|post_url = '## URL PARA ENVIAR O TESTE ##'|post_url = 'http://impact-server.com/apply'|

Após alterar o cógigo, ainda há um passo importante nesse teste, queremos saber de você, por que quer estudar conosco, nos conte quais razões te trouxeram aqui, para isso você precisa escrever tudo o que achar relevante no arquivo <b>etc/essay.txt</b> no diretório da aplicação. Note que sem isso a coisa toda não vai funcionar

### Agora vamos tentar executar esse código aí
#### Primeiro, precisamos instalar o Python3
Siga as instruções no site oficial do python que tudo vai dar certo!
* [Windows](https://python.org.br/instalacao-windows/)
* [Linux](https://python.org.br/instalacao-linux/)

Com o python instalado, vamos preparar o ambiente para executar esse teste, para isso precisamos executar o pip (gerenciador de pacotes do python), no diretório onde você baixou os arquivos (fez o clone, lembra?), execute o seguinte comando:
```
pip3 install -r requirements.txt
```

Agora, se tudo até aqui deu certo e você conseguiu seguir as instruções, nos envie esses dados executando a seguinte linha de comando no terminal (Linux) ou Prompt de Comando (Windows):
```
python3 app/client.py
```

Agora é só aguardar que assim que possível iremos entrar em contato!

Muita sorte aí! quqlquer dúvida nos procurem por favor!!