import requests
class Image_Downloader():
    def __init__(self,image_list=[]):
        self.image_list = image_list
    def text_reader(self, text_file):
        with open(text_file, "r") as file_text:
            for line in file_text:
                splitted_line = line.split()
                for i in splitted_line:
                    if i.startswith("src="):
                        for j in i[5:]:
                            if j == "'" or j == '"':
                                j_index = i[5:].index(j)
                                if i[5:(j_index+5)].endswith("jpg") or i[5:(j_index+5)].endswith("png"):
                                    self.image_list.append(i[5:(j_index + 5)])
        return print(self.image_list)
class Image_Jpg(Image_Downloader):
    def download(self):
        count = 0
        for i in self.image_list:
            try:
                ordiary_resp_jpg = requests.get(i)
                with open(f"{count}.png", "wb") as jpg_image:
                    jpg_image.write(ordiary_resp_jpg.content)
            except: 
                link = f"https:{i}"
                try:
                    response_jpeg = requests.get(link)
                except:
                    response_jpeg = requests.get(web_site_link+i[1:])
                    with open(f"{count}.jpg", "wb") as jpeg_image:
                        jpeg_image.write(response_jpeg.content)
            count +=1
class Image_Png(Image_Jpg):
    def download(self):
        count_ = 100
        for i in self.image_list:
            try:
                ordiary_resp_png = requests.get(i)
                with open(f"{count_}.png", "wb") as png_image:
                    png_image.write(ordiary_resp_png.content)
            except:
                link = f"https:{i}"
                try:
                    response_png = requests.get(link)
                except:
                    response_png = requests.get(web_site_link+i[:])
                    with open(f"{count_}.png", "wb") as png_image:
                        png_image.write(response_png.content)
            count_ += 1
        super().download()








image = Image_Png()
web_site_link= input("give me a link: ")
response = requests.get(web_site_link)

with open("web_site.txt", "w") as input_file:
    print(response.text, file=input_file)

image.text_reader("web_site.txt")
image.download()




