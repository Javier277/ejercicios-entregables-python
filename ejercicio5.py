def norm(s:str):
     return s.strip().lower()

bad = set()
with open("bad_words.txt", encoding="utf-8") as f:
    for line in f:
        w = line.strip()
        if w:
            bad.add(norm(w))

entrada= input("Introduce una palabra: ")
# 4. Validación: si está vacía o contiene espacios
# Nota: entrada.strip() verifica si está vacía o solo contenía espacios
if not entrada.strip() or " " in entrada.strip():
    print("Introduce una sola palabra (sin espacios).")
else:
    # 5. Normalizar y comprobar pertenencia en el set
    palabra_normalizada = norm(entrada)

    if palabra_normalizada in bad:
        print("NO CORRECTA")
    else:
        print("CORRECTA") 