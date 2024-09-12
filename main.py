import requests

if __name__ == "__main__":
    # boas vindas
    print("Olá, mundo! \n @fillipi.dev - Python para análise de dados.")

    # GET api "economia.awesomeapi.com.br"
    response = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    # validando STATUS
    status_code = response.status_code

    if(status_code != 200):
        print("Falha de comunicação com a API: \n https://economia.awesomeapi.com.br")

    if(status_code == 200):
        conteudo = response.json()
        print(f"Data e hora da consulta: {conteudo['USDBRL']['create_date']}")
        print('++++++++++++++++++++++++++')
        # Iterando sobre as chaves e exibindo os valores específicos
        # conteudo['USDBRL']: Acessa o dicionário JSON interno associado à chave 'USDBRL'.
        # .items(): Retorna uma lista de tuplas contendo os pares (chave, valor) do dicionário.
        for key, value in conteudo['USDBRL'].items():
            if key in ['code', 'name', 'high', 'low']:
                print(f"{key}: {value}")
        for key, value in conteudo['EURBRL'].items():
            if key in ['code', 'name', 'high', 'low']:
                print(f"{key}: {value}")
        for key, value in conteudo['BTCBRL'].items():
            if key in ['code', 'name', 'high', 'low']:
                print(f"{key}: {value}")
        print('++++++++++++++++++++++++++')