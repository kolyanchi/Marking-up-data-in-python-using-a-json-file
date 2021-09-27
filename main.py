from PIL import Image, ImageDraw
import json
import os

#Creating folders for images by specific classes
if not os.path.isdir("isOccluded"):
    os.mkdir("isOccluded")
if not os.path.isdir("isTruncated"):
    os.mkdir("isTruncated")
if not os.path.isdir("isDepiction"):
    os.mkdir("isDepiction")
if not os.path.isdir("isInside"):
    os.mkdir("isInside")
if not os.path.isdir("isGroupOf"):
    os.mkdir("isGroupOf")

#Flags for sorting images
isOccluded, isTruncated, isDepiction, isInside, isGroupOf = 0,0,0,0,0


with open('annotation.json') as json_file:
    data = json.load(json_file)
    for p in data:
        img = Image.open(p)
        draw = ImageDraw.Draw(img)
        for value in data[p]['objects']:

            #Setting flags
            isOccluded += value["isOccluded"]
            isTruncated += value["isTruncated"]
            isDepiction += value["isDepiction"]
            isInside += value["isInside"]
            isGroupOf += value["isGroupOf"]

            #Drawing a rectangle by coordinates
            if value["ignore"] == False:
                draw.rectangle([value["x"], value["y"], value["x"] + value["w"], value["y"] + value["h"]], outline='green', width=2)

        #Saving images by folders
        if isOccluded:
            img.save(p[7:])
            os.replace(p[7:], "isOccluded/"+p[7:])
        if isTruncated:
            img.save(p[7:])
            os.replace(p[7:], "isTruncated/" + p[7:])
        if isDepiction:
            img.save(p[7:])
            os.replace(p[7:], "isDepiction/" + p[7:])
        if isInside:
            img.save(p[7:])
            os.replace(p[7:], "isInside/" + p[7:])
        if isGroupOf:
            img.save(p[7:])
            os.replace(p[7:], "isGroupOf/" + p[7:])

        #Zeroing the flags for the following image
        isOccluded, isTruncated, isDepiction, isInside, isGroupOf = 0,0,0,0,0
