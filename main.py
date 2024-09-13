import requests
import csv
import os

if __name__ == "__main__":
    # boas vindas
    print("Olá, mundo! \n @fillipi.dev - Python para análise de dados.")

    # GET api "economia.awesomeapi.com.br"
    response = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    # validando STATUS
    status_code = response.status_code

    if(status_code != 200):
        print("Falha de comunicação com a API: \n https://economia.awesomeapi.com.br")

    # Caso a comunicacao com a API esteja OK!
    conteudo = response.json()

    # Diretorio arquivo CSV
    directory = r'C:\python\applications\api-cotacao-csv\csv'
    file_path = os.path.join(directory, 'cotacao.csv')

    # Criar o diretório se ele não existir
    os.makedirs(directory, exist_ok=True)

    # Montando arquivo CSV com as Chaves de cada Moeda da API
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ['code', 'codein', 'name', 'high', 'low', 'varBid', 'pctChange', 'bid', 'ask', 'timestamp', 'create_date']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        # Iterar sobre a lista de moedas: USD-BRL, EUR-BRL e BTC-BRL
        for moeda in ['USDBRL', 'EURBRL', 'BTCBRL']:
            if moeda in conteudo:
                writer.writerow(conteudo[moeda])

    print(f"Arquivo CSV criado com sucesso em {file_path}")