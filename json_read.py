import json
datas = """
{
  "book": [
    {
      "title": "El señor de los anillos",
      "cover": "personas",
      "year": 1990,
      "pages": 200
    },
    {
      "title": "Harry Potter",
      "cover": "personas",
      "year": 2003,
      "pages": 200,
    },
    {
      "title": "Geronimo Stilton",
      "cover": "persona animal",
      "year": 2001,
      "pages": 200,
    },
    {
      "title": "El Mago de Oz",
      "cover": "personas",
      "year": 2015,
      "pages": 150
    }
  ]
}
"""""


with open("ejemplo.json", 'w') as file:
    json.dump(datas,file)