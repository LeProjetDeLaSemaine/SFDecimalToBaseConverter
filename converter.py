(nombreDecimal,r,listeBase,toBase) = (input("Entrez votre décimal:") ,-1,[],input("Entrez la base:"))
#On utilise un tuple parce que c'est beau
while(nombreDecimal!=0):
    r= nombreDecimal%toBase
    nombreDecimal//=toBase
    listeBase.append(r)
listeBase.reverse()
chaine=""
if(toBase<=16):
    for bit in listeBase:
        if(bit==10):
            bit="A"
        elif(bit==11):
            bit="B"
        elif(bit==12):
            bit="C"
        elif(bit==13):
            bit="D"
        elif(bit==14):
            bit="E"
        elif(bit==15):
            bit="F"
        chaine+=str(bit)
else:
   print(listeBase)
print(chaine)

    

