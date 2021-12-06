import json
img = json.load(open("image_info_test-dev2017.json"))
print("Amount of images:",len(img["images"]))
print("Amount of categorie:",len(img["categories"]))
for i in (img["images"]):
    for j in i.keys():
        if i[j] == "000000000001.jpg":
            print("URL:",i['coco_url'])
            print("Height:",i['height'])
            print("Width:",i['width'])
            print("Id:",i['id'])
