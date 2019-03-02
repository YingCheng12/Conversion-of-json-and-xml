
# coding: utf-8

# In[72]:


import json
import sys

file1 = sys.argv[1]
file2 = sys.argv[2]

with open(file1) as f:
    data = json.load(f)

#print(data)
key=data['prizes']
# print(m)
xml=[]
start="<prizes>\n"
# print(start)
xml.append(start)
# print("，".join(xml))


for i in key:
#     print(i)
#     print(temp)
    xml.append("\t<"+i["category"]+">")
#     print("".join(xml))
    temp_year=i["year"]
#     print(temp_year)
    for j in i["laureates"]:
#         print(j)
#         print(temp_id)
#         print(temp_)
        xml.append("\n\t\t<laurate id=\""+j["id"]+"\" year=\""+temp_year+"\">")
        xml.append("\n\t\t\t<firstname>"+j["firstname"]+"</firstname>")
        xml.append("\n\t\t\t<surname>"+j["surname"]+"</surname>")
        if j.has_key("motivation"):
            xml.append("\n\t\t\t<motivation>\n\t\t\t"+j["motivation"].replace("&","&amp;")+"\n\t\t\t</motivation>")
            xml.append("\n\t\t\t<share>"+j["share"]+"</share>")
        xml.append("\n\t\t</laurate>")
    xml.append("\n\t</"+i["category"]+">\n")
xml.append("</prizes>")

# print("".join(xml))
# xml_file="prize.xml"
f = open(file2,'w')
f.write("".join(xml).encode('utf-8'))
f.close()

