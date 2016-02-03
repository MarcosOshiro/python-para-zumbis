'''
Questão D. Daniela é uma pessoa muito supersticiosa. Para ela, um número é
sortudo se ele contém o dígito 2 mas não o dígito 7. Então, na opinião dela,
quantos números sortudos existem entre 18644 e 33087, incluindo os extremos?
'''

a = 18644
sorte = 0
for a in list(range(18644, 33087)):
    if '2' in str(a):
        if '7' not in str(a):
            sorte += 1
    a += 1
print (sorte)
