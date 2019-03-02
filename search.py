from lxml import etree
import sys

str_lower = sys.argv[2]
# str_lower = 'ligo waves'

xml = etree.parse('index.xml')
# print(xml)
root=xml.getroot()


str_lower=str_lower.lower()
key_word_list = str_lower.split(' ')
# print(type(key_word_list))

list=[]
for i in key_word_list:
    l = root.xpath("/index/entry[keyword='"+i+"']/ids/id")
#     print len(l)
    for n in range(len(l)):
#         print(l[n].text)
        if int(l[n].text) not in list:
            list.append(int(l[n].text))
print(list)