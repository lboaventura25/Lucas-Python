from math import sqrt
import sys 


def main(valores):
    """Retorna a (media, desvpad) do conjunto de números fornecido."""
    cont = 0.0
    media = 0.0
    variancia = 0.0

    for number in valores:
        media += number
        cont += 1
        
    media /= cont
    
    for number in valores:
        variancia += (((number - media)**2)/ cont)
        
    desvpad = sqrt(variancia)

    return media, desvpad

if __name__ == "__main__":
    n = int(sys.argv[-1])
    main()
