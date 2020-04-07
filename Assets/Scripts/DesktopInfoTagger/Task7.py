import numpy as np 
import math
import csv
import xml
import xml.dom.minidom
import xml.etree.ElementTree as ET
import string 
import pprint

#Step 1: Pull Info from XML File

def parseXML(xmlfile):
    tree = ET.parse(xmlfile)
    root = tree.getroot()

    listOfFile = []
    titleArr = []
    xArr = []
    yArr = []
    zArr = []

    for title in root.findall('./MarkerData/title'):
        titleArr.append(title.text)

    for position in root.findall('./MarkerData/position'):
      
        for child in position:
            
            if child.tag == 'x':
                x = float(child.text)

            if child.tag == 'y':
                y = float(child.text)

            if child.tag == 'z':
                z = float(child.text)

        xArr.append(x)
        yArr.append(y)
        zArr.append(z) 
   
    listOfFile.extend(titleArr)
    listOfFile.extend(xArr)
    listOfFile.extend(yArr)
    listOfFile.extend(zArr)

    length = len(titleArr)

    return listOfFile, length



    
    


#Step 2: Find point with respect to ref
def RespectToRef(List, length):
    i = 0
    n = length - 1 #2
    newxArr = []
    newyArr = []
    newzArr = []
    newList = []

    # x component
    while (i <= length-2):
        # x = oldx - refx
        # refx is last x comp
        # oldx starts at first x comp
        # newx = oldx - refx
        newx = List[length+i] - List[length+n]
        newxArr.append(newx)

        newy = List[2*length + i] - List[2*length + n]
        newyArr.append(newy)

        newz = List[3*length + i] - List[3*length + n]
        newzArr.append(newz)

        i += 1

    newList.extend(newxArr)
    newList.extend(newyArr)
    newList.extend(newzArr)

    return newList




#Step 3: Conver to Inches 
def ConvertToInches(List):
    length = len(List)
    i = 0
    # meters / 0.0254
    while (i < length):
        List[i] = List[i] / 0.0254
        i += 1
    return List


#Step 4: Make Z Coordinate Normal to Deck by switching Y/Z Values 
def NormalToDeck(List):
    length = len(List)
    #length of one component (x,y,or z)
    length2 = int (length / 3)
    i = 0
    
    while (i < length2):
        Temp = List[length2 + i]
        List[length2 + i] = List[2*length2 + i]
        List[2*length2 + i] = Temp
        i += 1

    return List


#Step 5: Transform
def Transform(List):







def main():
    print("Printing whole list")
    List, length = parseXML('measuretest2.xml')
    print(List)
    ToRef = RespectToRef(List, length)
    ToInches = ConvertToInches(ToRef)
    #print(ToInches)
    NormalZ = NormalToDeck(ToInches)
    print(NormalZ)


if __name__ == "__main__":
    main()
    



