def palabra_unica(frase):
    frase_unica=[]
    
    for i in frase:
        if i not in frase_unica:
            frase_unica.append(i)
       
    frase_unica.sort()
    return frase_unica


resultado=palabra_unica("papaleta")
print(resultado)