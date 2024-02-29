import json
import os 

diretorio_atual, ___DUMMY = os.path.split(os.path.abspath(__file__))
print(diretorio_atual)
caminho_dados = os.path.join(diretorio_atual, 'dados.json')
    

def main():

    with open(caminho_dados) as arquivo_dados:
        dados = json.load(arquivo_dados)

    dia_com_maior_valor = max(dados, key=lambda x: x['valor'])

    dias_com_valores_diferentes_de_zero = [dia for dia in dados if dia['valor'] != 0]

    dia_com_menor_valor = min(dias_com_valores_diferentes_de_zero, key=lambda x: x['valor'])

    soma_valores = sum(dia['valor'] for dia in dias_com_valores_diferentes_de_zero)

    media = soma_valores / len(dias_com_valores_diferentes_de_zero)

    dias_maiores_que_a_media = [dia for dia in dados if dia['valor'] > media]


    print("O menor valor do mes foi: " + str(dia_com_menor_valor['valor']))
    print("O maior valor do mes foi: " + str(dia_com_maior_valor['valor']))
    print("Numero de dias no mes em que o valor de faturamento diario foi superior a media mensal: " + str(len(dias_maiores_que_a_media)))




if __name__ == '__main__':
    main()