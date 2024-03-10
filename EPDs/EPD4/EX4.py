f = open("archivo2.txt", "w")

texto = "p"
while texto != "FIN":
    texto = input("Testo archivo: ")

    f.write(texto)

f.close()
