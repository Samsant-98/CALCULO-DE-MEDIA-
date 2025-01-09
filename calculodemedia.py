media.py
print("Esse programa calcula a media")
nota1 = raw_input("Digite a primeira nota: ")
nota2 = raw_input("Digite a segunda nota: ")
media = (float(nota1) + float(nota2))/2
if media > 6:
    print("PARABENS, VOCE ESTA APROVADO")
else:
    print("VOCE ESTA REPROVADO")
print("ESSA SUA MEDIA: %s" % media)
Comment
