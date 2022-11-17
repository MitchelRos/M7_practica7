import xml.etree.ElementTree as ET
#Crea fitxer
def writeFile():
    # Crea arxiu
    f = open("arxiu.xml", "w")
    f.write("<students></students>")
    f.close()

def creaStudent(pare, nom, cognom, email, dni, isMatriculat):
    # Crea el fill dins del pare
    fill = ET.SubElement(pare, "student")
    fill.set("matriculat", isMatriculat)
    # Crea <name>Kevin</name>
    createName = ET.SubElement(fill, "name")
    createName.text = nom
    # Crea <surname>Sama</surname>
    createSurname = ET.SubElement(fill, "surname")
    createSurname.text = cognom
    # Crea <email>kev@mail.com</email>
    createEmail = ET.SubElement(fill, "email")
    createEmail.text = email
    # Crea <dni>kev@mail.com</dni>
    createDNI = ET.SubElement(fill, "dni")
    createDNI.text = dni
    return fill


# Crea un fitxer
writeFile()

#Seleciona l'arxiu
tree = ET.parse("arxiu.xml")
root = tree.getroot()
# Crea el pare
root =ET.Element("students")
#Seleciona el pare
pare = ET.Element("students")



creaStudent(pare, nom="Kevin", cognom="Sama", email="kev@gmail.com", dni="1111x", isMatriculat="false")
creaStudent(pare, nom="Mitchel", cognom="Sama", email="kev@gmail.com", dni="2222d", isMatriculat="false")
creaStudent(pare, nom="Julio", cognom="Sama", email="kev@gmail.com", dni="333f", isMatriculat="false")
creaStudent(pare, nom="Luis", cognom="Sama", email="kev@gmail.com", dni="444f", isMatriculat="false")
creaStudent(pare, nom="Jorge", cognom="Sama", email="kev@gmail.com", dni="5555x", isMatriculat="false")

ET.indent(pare)
ET.dump(pare)
ET.indent(tree)

tree = ET.ElementTree(pare)
# Escriu al arxiu
tree.write("arxiu.xml")
