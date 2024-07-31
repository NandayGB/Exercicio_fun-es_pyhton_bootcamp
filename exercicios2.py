"""Reverso do número. Faça uma função que retorne o reverso de um
número inteiro informado. Por exemplo: 127 -> 721."""

def reverso_numero(numero):
    
    numero_str = str(numero)
    
    numero_reverso_str = numero_str[::-1]
    
    numero_reverso = int(numero_reverso_str)
    
    return numero_reverso

numero = 127
resultado = reverso_numero(numero)
print("O reverso do número é:", resultado)