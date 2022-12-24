def encriptar(msg : bytearray) -> bytearray:
    # Completar con el proceso de encriptación
    largo = len(msg)
    a = bytearray()
    b = bytearray()
    c = bytearray()
    num = 0
    ans = bytearray()

    for i in range(0, largo, 3):
        a += msg[i].to_bytes(1, byteorder='big')

    for i in range(1, largo, 3):
        b += msg[i].to_bytes(1, byteorder='big')

    for i in range(2, largo, 3):
        c += msg[i].to_bytes(1, byteorder='big')
    
    if len(b) % 2 == 0:
        pos = int(len(b) / 2)
        num += int.from_bytes(b[pos - 1].to_bytes(1, byteorder='big'), byteorder='big')
        num += int.from_bytes(b[pos].to_bytes(1, byteorder='big'), byteorder='big') 
    else:
        pos = int((len(b) - 1) / 2)
        num += int.from_bytes(b[pos].to_bytes(1, byteorder='big'), byteorder='big') 

    num += int.from_bytes(a[0].to_bytes(1, byteorder='big'), byteorder='big')
    num += int.from_bytes(c[len(c) - 1].to_bytes(1, byteorder='big'), byteorder='big')

    if num % 2 == 0:
        numero = 0
        n = numero.to_bytes(1, byteorder='big')
        ans += n + c + a + b 
    else:
        numero = 1
        n = numero.to_bytes(1, byteorder='big')
        ans = n + a + c + b

    return ans


def desencriptar(msg : bytearray) -> bytearray:
    # Completar con el proceso de desencriptación
    largo = len(msg) - 1
    l_a = 0
    l_b = 0
    l_c = 0
    pos = 1
    a = bytearray()
    b = bytearray()
    c = bytearray()
    ans = bytearray()

    for _ in range(0, largo, 3):
        l_a += 1

    for _ in range(1, largo, 3):
        l_b += 1

    for _ in range(2, largo, 3):
        l_c += 1
    
    if msg[0] == 1:
        
        for _ in range(0, l_a):
            a += msg[pos].to_bytes(1, byteorder='big')
            pos += 1
        
        for _ in range(0, l_c):
            c += msg[pos].to_bytes(1, byteorder='big')
            pos += 1
        
        for _ in range(0, l_b):
            b += msg[pos].to_bytes(1, byteorder='big')
            pos += 1
            
    else:
        for _ in range(0, l_c):
            c += msg[pos].to_bytes(1, byteorder='big')
            pos += 1
        
        for _ in range(0, l_a):
            a += msg[pos].to_bytes(1, byteorder='big')
            pos += 1
        
        for _ in range(0, l_b):
            b += msg[pos].to_bytes(1, byteorder='big')
            pos += 1
        
    for i in range(0, l_a - 1):
        ans += a[i].to_bytes(1, byteorder='big')
        ans += b[i].to_bytes(1, byteorder='big')
        ans += c[i].to_bytes(1, byteorder='big')
        
    ans += a[l_a - 1].to_bytes(1, byteorder='big')
        
    if l_a == l_b:
        ans += b[l_a - 1].to_bytes(1, byteorder='big')

    if l_a == l_c:
        ans += c[l_a - 1].to_bytes(1, byteorder='big')
        
    return ans


if __name__ == "__main__":
    # Testear encriptar
    msg_original = bytearray(b'\x05\x08\x03\x02\x04\x03\x05\x09\x05\x09\x01')
    msg_esperado = bytearray(b'\x01\x05\x02\x05\x09\x03\x03\x05\x08\x04\x09\x01')

    msg_encriptado = encriptar(msg_original)
    if msg_encriptado != msg_esperado:
        print("[ERROR] Mensaje escriptado erroneamente")
    else:
        print("[SUCCESSFUL] Mensaje escriptado correctamente")
    
    # Testear desencriptar
    msg_desencriptado = desencriptar(msg_esperado)
    if msg_desencriptado != msg_original:
        print("[ERROR] Mensaje descencriptado erroneamente")
    else:
        print("[SUCCESSFUL] Mensaje descencriptado correctamente")
