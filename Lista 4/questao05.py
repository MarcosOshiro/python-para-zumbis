'''
5. Seja o mesmo texto acima “splitado”. Calcule quantas palavras possuem uma
das letras “python” e que tenham mais de 4 caracteres. Não se esqueça de
transformar maiúsculas para minúsculas e de remover antes os caracteres
especiais
'''
import re

texto = "The Python Software Foundation and the global Python community \
welcome and encourage participation by everyone. Our community is based on \
mutual respect, tolerance, and encouragement, and we are working to help each \
other live up to these principles. We want our community to be more diverse: \
whoever you are, and whatever your background, we welcome you."

resultado = []
k = 0
texto.split(' ')
texto2 = ""
while k < len(texto):
    if texto[k] in ",.;/<>:?!@#$%&*()_+=-][{}´`~^ºª§\|°":
        texto2 = texto2 + ""
    else:
        texto2 = texto2 + texto[k]
    k += 1

palavras = texto2.split(' ')
prefixos = ["P","p","Y","y","T","t","H","h","O","o","N","n"]
for x in palavras:
    if len(x) > 3:
        u = 0
        for u in range(len(x)):
            if u not in ("P","p","Y","y","T","t","H","h","O","o","N","n"):
                if x not in resultado:
                    resultado.append(x)
        u +=1

print('São, ' +str(len(resultado))+' palavras')



