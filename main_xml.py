import xml.etree.ElementTree as ET


tree = ET.parse("arxiu.xml")
root = tree.getroot()
# Crea el pare
pare = ET.Element("students")

# Crea el fill dins del pare
fill = ET.SubElement(pare, "student")
fill.set("matriculat", "true")

#Crea <name>Kevin</name>
createName = ET.SubElement(fill, "name")
createName.text = "Kevin"

#Crea <surname>Sama</surname>
createSurname = ET.SubElement(fill, "surname")
createSurname.text = "Sama"

#Crea <email>kev@mail.com</email>
createEmail = ET.SubElement(fill, "email")
createEmail.text = "kev@mail.com"

#Crea <dni>kev@mail.com</dni>
createDNI = ET.SubElement(fill, "dni")
createDNI.text = "12345678x"

ET.indent(pare)
ET.dump(pare)
ET.indent(tree)

tree = ET.ElementTree(pare)
# Escriu al arxiu
tree.write("arxiu.xml")
