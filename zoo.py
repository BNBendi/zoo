def addAnimal( myName):
    animal=dict()
    found = False
    for a in zoo:
        if myName  in  a.keys():
            a[myName] += 1
            found=True
            #break
    if not found:
        animal[myName] = 1 
        zoo.append(animal)
    



zoo = [{"kecske": 1}, {"ló": 1}]
animal=dict()


print("EZ egy állatkert.")
print("Állat hozzáadása (1)- elvétele (2) - Kilépés (0)")
select = None

while select !="0":
    select  = input("Mit szeretne tenni?")
    if select !="0":
      if select == "1":
            name = input("AZ állat neve: ")
            addAnimal(name)
                             
                
print(f"Első: {zoo} ")
        
              
