# Python para Análise de Dados (BI)

Esta aplicação cria uma conexão externa com a API do Banco Central do Brasil para extrair a cotação das moedas [dolar, euro e bitcoin] com geração de arquivo CSV para consumo pessoal ou dashboard de alguma ferramenta de visualização em BI.

### Versão da linguagem [3.11.1]

### Bibliotecas utilizadas

<code>requests</code>, <code>csv</code> e <code>os</code>

### Print do código

![O codigo](https://github.com/Fillipis/api-cotacao-csv/blob/master/img/print-codigo.png)

### Print do resultado do código

![O resultado](https://github.com/Fillipis/api-cotacao-csv/blob/master/img/print-resultado.png)

## Ressalvas: O diretório com arquivo CSV foi criado localmente

Exemplo: <code>C:\:DIRETORIO_LOCAL\csv</code>

## Vídeo de demonstração

https://www.loom.com/share/e60444bfe55c4bc1aced3678dedd8bc2?sid=f5c63218-2010-4299-aea5-795e4a6869e6

## Processo da aplicação

O usuário ou rotina automática executa a aplicação em python, a aplicação se comunica com API, com o retorno da API positivo a geraçao do arquivo de cotação CSV é executada e o arquivo está pronto para ser utilizado sempre que esse processo não se interrompa.

## Vídeo de visualização com Power BI

https://www.loom.com/share/4f3fd75abaa449b99f76274bae080572

🕶️

![Pattern](https://github.com/Fillipis/api-cotacao-csv/blob/master/img/pattern.png)