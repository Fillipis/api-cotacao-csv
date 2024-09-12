import requests

if __name__ == "__main__":
    # boas vindas
    print("Olá, mundo! \n @fillipi.dev - Python para análise de dados.")

    # consultando api "economia.awesomeapi.com.br"
    response = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    # validando alguns status
    status_code = response.status_code

    if(status_code != 200):
        print("Falha de comunicação com a API: \n https://economia.awesomeapi.com.br")

    if(status_code == 200):
        content = response.json()
        print(content)