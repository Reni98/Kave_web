class Zoldsegek:
    def __init__(self):
        self.lista = []

    def beolvas(self):
        with open("zoldsegek.txt", "r", encoding="utf-8") as fajl:
            adatok = fajl.readlines()

            for adat in adatok:
                adat = adat.strip().split(";")

                zoldseg_nev = adat[0]
                tonna = int(adat[1])
                ar = int(adat[2])
                ev = int(adat[3])

                self.lista.append([zoldseg_nev, tonna, ar,ev])
            for item in self.lista:
                print(f"{item[0]} - {item[1]} tonna - {item[2]} Ft/kg - {item[3]}")

    def utan_2015(self):
        print("2015 utáni zöldségek:")
        for utan in self.lista:
            if utan[3] > 2015:
                print(f"{utan[0]} - {utan[1]} tonna - {utan[2]} Ft/kg - {utan[3]}")
    
    def legolcsobb(self):
        print("A legolcsóbb zöldség:")
        legolcsobb_ar = float("inf")
        legolcsobb_zoldseg=""
        for olcsobb in self.lista:
            if olcsobb[2]< legolcsobb_ar:
                legolcsobb_ar = olcsobb[2]
                legolcsobb_zoldseg = olcsobb[0]

        print(f"{legolcsobb_zoldseg} - {legolcsobb_ar} Ft/kg")

    def paprikaval_kezdodik(self):
        db = 0
        for kezd in self.lista:
            if kezd[0].startswith("Paprika"):
                db +=1
        print(f"'Paprika'-val kezdődő zöldségek száma:{db}")

        with open("paprika_zoldsegek.txt", "w", encoding="utf-8") as file:
            for kezd in self.lista:
                if kezd[0].startswith("Paprika"):

                    file.write(f"\n{kezd[0]} - {kezd[1]} tonna - {kezd[2]} Ft/kg - {kezd[3]}")
            print("A paprika_zoldsegek.txt fájlba kiírásra kerültek az adatok.")



zold = Zoldsegek()
zold.beolvas()
zold.utan_2015()
zold.legolcsobb()
zold.paprikaval_kezdodik()