'''
4. Seja o statement sobre diversidade: “The Python Software Foundation and
the global Python community welcome and encourage participation by everyone.
Our community is based on mutual respect, tolerance, and encouragement,
and we are working to help each other live up to these principles. We want
our community to be more diverse: whoever you are, and whatever your background,
we welcome you.”.

Gere uma lista de palavras deste texto com split(), a seguir
crie uma lista com as palavras que começam ou terminam com uma das letras
“python”. Imprima a lista resultante. Não se esqueça de remover antes os
caracteres especiais e cuidado com maiúsculas e minúsculas. 
'''

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
    if x.startswith(tuple(prefixos)) and x.endswith(tuple(prefixos)):
        resultado.append(x)

print(resultado)



