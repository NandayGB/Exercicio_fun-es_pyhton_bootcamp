"""Crie um programa que leia quanto dinheiro uma pessoa tem na
carteira, e calcule quanto poderia comprar de cada moeda estrangeira.
Considere a tabela de conversão abaixo:
Dólar Americano: R$ 4,91
Peso Argentino: R$ 0,02
Dólar Australiano: R$ 3,18
Dólar Canadense: R$ 3,64
Franco Suiço: R$ 0,42
Euro: R$ 5,36
Libra esterlina: R$ 6,21"""

def calcular_valor_em_moeda(dinheiro, taxa_cambio):
    return dinheiro / taxa_cambio

def main():
    print("Bem-vindo ao conversor de moedas!")

    dinheiro = float(input("Digite quanto dinheiro você tem na carteira (em R$): "))

    taxas_cambio = {
        "Dólar Americano": 4.91,
        "Peso Argentino": 0.02,
        "Dólar Australiano": 3.18,
        "Dólar Canadense": 3.64,
        "Franco Suiço": 0.42,
        "Euro": 5.36,
        "Libra Esterlina": 6.21
    }

    for moeda, taxa in taxas_cambio.items():
        valor_em_moeda = calcular_valor_em_moeda(dinheiro, taxa)
        print(f"Com R$ {dinheiro:.2f}, você pode comprar {valor_em_moeda:.2f} {moeda}")

if __name__ == "__main__":
    main()