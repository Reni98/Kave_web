mertekegyseg = input("Milyen mértékegységről szeretne átváltani? (liter/dl):")
atvaltando = int(input("Adja meg az átváltandó mennyiséget:"))

if mertekegyseg == "liter":
    eredmeny = atvaltando*10
    print(f"Az eredmény: {eredmeny} dl")

elif mertekegyseg == "dl":
    eredmeny = atvaltando/10
    print(f"Az eredmény: {round(eredmeny)} l")