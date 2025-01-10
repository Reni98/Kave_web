taborneve = input("Adja meg a tábor nevét :")
kaloriak = []
db = 1
while True:
    kaloria = int(input(f"Adjon meg egy napi kalóriaértéket (jelenlegi adatok száma: {db}):"))
    kaloriak.append(kaloria)
    db+=1

    if db >5:
        kerdes = input("Szeretne további kalóriákat hozzáadni? (i/n):")
        if kerdes == "n":
            break

print(f"Tábor neve: {taborneve}")
print(f"Átlagosan elégetett kalória naponta: {round(sum(kaloriak)/len(kaloriak))} kcal.")