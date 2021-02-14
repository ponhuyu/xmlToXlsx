import xml.etree.ElementTree as ET
import pandas as pd
from collections import OrderedDict

tree = ET.parse(source="resources/file_to_be_parsed.xml")
root = tree.getroot()

headers = root.findall('./*/transaction/table/tabledesc/*')
body = root.findall('./*/transaction/table/replace/*')

struc = OrderedDict()
# body


for head in headers:
    struc[head.attrib['name']] = [head.attrib['label']]

for el in body:
    if el.tag == 'record':
        for child in el:
            if child.tag == 'field':
                try:
                    struc[child.attrib['name']].append(child.attrib['value'])
                except:
                    struc[child.attrib['name']].append("")
            else:
                continue
    else:
        continue

# for el in body:
#    try:
#        struc[el.attrib['name']].append(el.attrib['value'])
#    except:
#        struc[el.attrib['name']].append("")

df = pd.DataFrame(struc)

# determining the name of the file
file_name = input('Vvedite absolute path dlya sohraneniya file and name of the file: ')

# saving the excel
df.to_csv(file_name)
print('DataFrame is written to Excel File successfully.')





