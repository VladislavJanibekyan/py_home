import json
import requests
import threading
count = 0
def link_maker(text_file):
    image_list = []
    with open(text_file, "r") as file_text:
        for line in file_text:
            splitted_line = line.split()
            for i in splitted_line:
                if i.startswith("src="):
                    for j in i[5:]:
                        if j == "'" or j == '"':
                            j_index = i[5:].index(j)
                            if i[5:(j_index+5)].endswith("jpg") or i[5:(j_index+5)].endswith("png"):
                                image_list.append(i[5:(j_index + 5)])
    return image_list
user_input = input("give me a web site: ")
creat_file = requests.get(user_input)
with open("web_site.txt", "w") as file_text:
    print(creat_file.text, file=file_text)
iamge_link = link_maker("web_site.txt")
image_dic = {"images": [{i.split("/")[-1]: i} for i in iamge_link[:10]]}
with open("link_json.json", "w") as json_file:
    json.dump(image_dic, json_file,indent= True) 
key_list = []
val_dic = {}
with open("link_json.json") as file_json:
    final = json.load(file_json)
final_values = list(final.values())
for i in final_values[0]:
    for j,b in i.items():
        key_list.append(j)
        val_dic[j] = b 
print(key_list)
print(val_dic)

def downloader(link):   
    image_bit = requests.get(val_dic[link])
    if image_bit.status_code == 200 and val_dic[link].endswith("png"):
        with open(f"{link}.png", "wb") as png:
            png.write(image_bit.content)
    else:
        if image_bit.status_code ==200 and val_dic[link].endswith("jpg"):
            with open(f"{link}.jpg", "wb") as jpg:
                jpg.write(image_bit.content)
threading_list = []

for i in range(10):
    slave = threading.Thread(target=downloader, args=(key_list[i],))
    threading_list.append(slave)
    slave.start()




