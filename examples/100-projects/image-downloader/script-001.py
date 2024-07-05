import os, re, requests

def ImageDownloader(url):

    response = requests.get(url)
    
    text = response.text

    print(text)

    p = r'<img.*?src="(.*?)"[^\>]+>'
    img_addrs = re.findall(p, text)

    for i in img_addrs:
        os.system("wget {}".format(i))

    return "DONE"

print("Hey!! Welcome to the Image downloader...")

link=input("Please enter the url from where you want to download the image..")

ImageDownloader(link)