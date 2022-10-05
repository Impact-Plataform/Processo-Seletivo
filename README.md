# Plataforma Impact - Teste de aceitação
Olá! Criamos um pequeno teste, para servir como validação inicial para os novos alunos da Plataforma Impact.

Nosso objetivo com esse teste é saber se vc está preparado para começar a estudar e se desenvolver cada vez mais!

Siga as instruções abaixo e caso você consiga fazer esse pequeno código funcionar, ele irá nos enviar sua inscrição e vamos conversar!

## DICAS
### Terminal
Caso tenha alguma dificuldade sobre o que é um [terminal](http://impactwiki.duckdns.org/pt-br/conteudos/linux/terminal) ([Linux](http://impactwiki.duckdns.org/pt-br/conteudos/linux/historia)) ou um prompt de comando (Windows), tente entender como realizar as operações básicas primeiro, como executar comando ou navegar pelos diretórios.

Mais informações sobre como operar um terminal Linux podem ser encontradas nesse [link](https://www.techtudo.com.br/noticias/2012/04/aprenda-os-comandos-basicos-do-linux.ghtml)

### Um computador (ambiente) para usar no teste
No teste, é pedido que sejam instalados alguns componentes no computador. Caso não queira instalar nada em seu computador, você pode tentar usar um ambiente web (um computador com linux rodando e acessível pelo seu browser) usando o [KillerCoda](https://killercoda.com/playgrounds/scenario/ubuntu). Com esse link você terá acesso a um computador com linux totalmente funcional por cerca de 60 minutos.

### Um editor de textos (fontes) para usar no teste
Recomendamos o uso do [Visual Studio Code](https://code.visualstudio.com/), que é um editor de textos e códigos muito completo, mas dependendo de como você escolher realizar esse teste talvez não tenha acesso a ele diretamente e pode querer tentar um editor diretamente no terminal, nesse caso, recomendamos o uso do [micro](https://micro-editor.github.io/). Para instalar esse ótimo editor, no <b>Linux</b>, use o seguinte comando:

```
curl https://getmic.ro | bash
```

#### Comandos importantes do micro editor
* CTRL + S: Salva o documento
* CTRL + Q: Sair do editor

No <b>windows</b>, você pode usar o notepad se preferir para editar os arquivos

## Instruções
### Instale o [git ](https://pt.wikipedia.org/wiki/Git)
Siga as intruções do site oficial do git e instale em seu computador essa ferramenta, ela é necessária para que você tenha acesso ao programa de teste
* [Windows](https://git-scm.com/download/windows)
* [Linux](https://git-scm.com/download/linux)

Caso queira saber mais sobre essa poderosa ferramenta, o artigo da [Wikipedia](https://pt.wikipedia.org/wiki/Git) pode dar uma boa noção, mas em poucas palavras, é uma ferramenta largamente utilizada no mercado para controle de versão e repositório de arquivos fonte.

### Agora clone o repositório
"Clonar o repositório" é como usualmente dizemos quando queremos pegar um código fonte e baixar para o nosso computador, é um passo importante do nosso teste.

Primeiro crie uma pasta/diretório em algum local do seu computador, recomendamos usar uma pasta dedicada para isso, com um nome intuítivo, como "git", por exemplo, é recomendado que essa pasta fique em algum lugar de fácil acesso para o seu usuário, ou em seu home (<b>c:\users\\<SEU USUÁRIO>\git</b> no Windows ou <b>\home\\<SEU USUÁRIO>\git</b> no Linux).

Execute um <b>comando de cada vez</b> no seu terminal/prompt de comando para conseguir baixar todos os arquivos do teste
#### Windows: 
```  
cd %HOMEPATH%
md git
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

Fique atento em qual pasta você está no momento, os comandos a seguir só irão funcionar se forem executados no local correto.

No Windows, o caminho aparece na aprte esquerda do prompt de comando e deve ser algo como:
```
C:\Users\USUARIO\git\Processo-Selevito>
```

No Linux, isso varia um pouco de acordo com o tipo de terminal que você está usando, mas exsite um comando que pode te ajudar aqui, o <b>pwd</b>, veja como deve ser a saída desse comando:
```
$> pwd
/home/USUARIO/git/Processo-Seletivo
```

### Vamos alterar alguns pontos para fazer esse programa funcionar?
Usando o seu [editor de texto/códigos preferido](https://code.visualstudio.com/), vá até o arquivo client.py, que está na pasta app, dentro do repositório que você acabou de baixar (<b>app/client.py</b>), é nele que precisamos colocar algumas informações importantes!

Você precisa alterar algumas linhas específicas para sabermos quem é você e saber se você consegue seguir corretamente essas instruções:

|Linha|Descrição|Valor no arquivo|Novo valor|
|:-:|:--|:--|:--|
|**28**|Caminho para buscar a chave de criptografia|```key_url = '## URL PARA BAIXAR A CHAVE DE CRIPTOGRAFIA ##'```|```key_url = 'http://impact-server.com/key'```|
|**55**|Precisamos do seu nome|```'name': "SEU NOME",```|```'name': "fulano afim de estudar",```|
|**56**|Precisamos do seu e-mail|```'email': "SEU EMAIL",```|```'email': "fulano@email.com",```|
|**57**|Precisamos do seu telefone|```'phone': "SEU TELEFONE COM DDD",```|```'phone': "(21) 98888-7777",```|
|**7**0|Caminho para que esse programa consiga nos enviar os resultados e seus dados|```post_url = '## URL PARA ENVIAR O TESTE ##'```|```post_url = 'http://impact-server.com/apply'```|

Após alterar o cógigo, ainda há um passo importante nesse teste, queremos saber de você, por que quer estudar conosco, nos conte quais razões te trouxeram aqui, para isso você precisa escrever tudo o que achar relevante no arquivo <b>etc/essay.txt</b> no diretório da aplicação. Note que sem isso a coisa toda não vai funcionar

#### Dica
Não se esqueça de salvar os arquivos ANTES de tentar executar os programas

### Agora vamos tentar executar esse código aí
#### Primeiro, precisamos instalar o Python3
Siga as instruções no site oficial do python que tudo vai dar certo!
* [Windows](https://python.org.br/instalacao-windows/): No Windows 10 ou 11, caso tenha dificuldades, é possível instalar o Python pela loja de aplicativos do Windows (Microsoft Store) sem problemas
* [Linux](https://python.org.br/instalacao-linux/): A Maioria das distribuições já possui python por padrão, mas siga as instruções do site.

Com o python instalado, vamos preparar o ambiente para executar esse teste, para isso precisamos executar o pip (gerenciador de pacotes do python), no diretório onde você baixou os arquivos (fez o clone, lembra?), execute o seguinte comando:
```
pip3 install -r requirements.txt
```

Agora, se tudo até aqui deu certo e você conseguiu seguir as instruções, nos envie esses dados executando a seguinte linha de comando no terminal (Linux) ou Prompt de Comando (Windows):
```
python3 app/client.py
```

Agora é só aguardar que assim que possível iremos entrar em contato!

Muita sorte aí! qualquer dúvida nos procurem por favor!!