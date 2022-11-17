#importem el json
import json
#Creem una variable que es diu datas amb les dades següents 4 llibres
datas = {
  #Creem el primer llibre
  "book": [
    {
      "title": "El senyor de los anillos",
      "cover": "personas",
      "year": 1990,
      "pages": 200
    },
    #El segon llibre
    {
      "title": "Harry Potter",
      "cover": "personas",
      "year": 2003,
      "pages": 200,
    },
    #El tercer llibre
    {
      "title": "Geronimo Stilton",
      "cover": "persona animal",
      "year": 2001,
      "pages": 200,
    },
    #El ultim llibre
    {
      "title": "El Mago de Oz",
      "cover": "personas",
      "year": 2015,
      "pages": 150
    }
  ]
}

#Quan executem aquet fitxer, lo que permet es que crei el nom del fitxer que li hem posat
#Obrira el fitxer jsonFile.json amb permis d'escritura
with open("jsonFile.json", 'w') as file:
    json.dump(datas,file)
#Quan executem el fitxer doncs modificarem el numero d'espais per cada llibre
print(json.dumps(datas, indent=2))

