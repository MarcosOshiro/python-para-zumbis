def ip_ok(ip):
    ip = ip.split('.')
    for byte in ip:
        if int(byte) > 255:
            return False
    return True
arq = open('IPS.txt')
validos = open('Válidos.txt', 'w')
invalidos = open('Inválidos.txt', 'w')
for linha in arq.readlines():
    if ip_ok(linha):
        validos.write(linha)
    else:
        invalidos.write(linha)
arq.close()
validos.close()
invalidos.close()

#split de nada é erro no programa (escrevei assim pq se eu precisar consultar isso eu vou ter que pensar um pouco e não só ver e executar... #chupaeumesmo
