import itertools

def traduzir(numeros):
    arr = []

    for x in numeros:
        arr.append(dict[int(x)])

    pro = list(itertools.product(*arr))

    res = []
    for x in pro:
        a = ''.join(x)
        if a in palavras: res.append(a)
    return res

file = open('br.txt', 'r')
pa = file.read().split('\n')
palavras = {x:0 for x in pa}

dict = {2:["a","b","c"],3:["d","e","f"],4:["g","h","i"],5:["j","k","l"],6:["m","n","o"],7:["p","q","r","s"],8:["t","u","v"],9:["w","x","y","z"]}


frase = input("Digite os numeros, palavras separadas por espaço: ")

a = frase.split()
r = [traduzir(x) for x in a]

print(r)





