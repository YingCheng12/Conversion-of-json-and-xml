
# coding: utf-8

# In[1]:


from lxml import etree
import sys

file1 = sys.argv[1]
file2 = sys.argv[2]



# fp = open('stopwords.txt')
# arr=[]
# for lines in fp.readlines():
#     lines=lines.replace("\n","")
#     arr.append(lines)
#     #print(lines)
# fp.close()

xml = etree.parse(file1)
# print(xml)
root=xml.getroot()
# print(root)
dic={}

for node in root.getchildren():
#     print(node.tag) 
    for sub_node in node.getchildren():
#         print(sub_node.get("id"))
        for sub_sub_node in sub_node.getchildren():
#             print(sub_sub_node)
            if sub_sub_node.tag=='motivation':
#                 print(sub_sub_node.text)
                content=sub_sub_node.text
#                 print content
                n1 = content.replace('\"','')
#                 print(n1)
                n2 = n1.replace(",","").replace("-",'').replace("'",'').replace('&','').replace(';','').replace(':','').replace('.','').replace('+','').replace('/','').replace('(','').replace(')','').replace('<','').replace('>','')
#                 print n2
                n = n2.split(' ')
#                 print n
                for j in n:
                    j=j.replace("\t","").replace("\n","")
                    key_d = j.lower()
                    key_d_value = sub_node.get("id")
                        #dic.update(d)
                    if key_d not in dic.keys():
                        d = {key_d:[key_d_value]}
                        dic.update(d)
                        #dic.setdefault("key_d",).append(key_d_value)
                    else:
                        dic[key_d].append(key_d_value)
                        dic[key_d].sort()
#print(dic)


index = etree.Element("index")  
for keys, id_list in dic.items():
#     print(keys)
    entry=etree.SubElement(index, "entry")
    keyword=etree.SubElement(entry,'keyword')
    keyword.text=keys
    ids=etree.SubElement(entry,'ids')
    
    for id_values in id_list:
#         print(id_values)
        id=etree.SubElement(ids,'id')
        id.text= id_values
m=etree.tostring(index, pretty_print=True)
# print(etree.tostring(index, pretty_print=True))

# index_xml="index.xml"
f = open(file2,'w')
f.write(m.encode('utf-8'))
f.close()

