import random
import string 

def gerador_codigo(tamanho=6, caracteres= string.ascii_lowercase+string.digits) : 
    return "".join(random.choice(caracteres) for _ in range(tamanho))
