from PIL import Image
import numpy as np

def simulatePrint(path):
    """
    path: filepath to get to image to simulate printing
    """
    img = Image.open(path)
    img.load()
    print("here")
    
    dataR = np.asarray(img, dtype="int32")
    dataRG = np.asarray(img, dtype="int32")
    dataRGB = np.asarray(img, dtype="int32") #contains all RGB values
    print("here2")
    for c in range(len(dataR)):
        for r in range(len(dataR[c])):
            dataR[c][r] = [dataR[c][r][0],0,0] #keep R, zero out G and B
            dataRG[c][r] = [dataRG[c][r][0],dataRG[c][r][1],0] #keep R and G, zero out B
    print("here3")         
    pathSplit = path.split(".")  
    name = ".".join(pathSplit[:-1])
    ext = "."+pathSplit[-1]
                  
    imgR = Image.fromarray(np.asarray( np.clip(dataR,0,255), dtype="uint8"))
    imgR.show()
    img.save(name+"R"+ext)
    imgRG = Image.fromarray(np.asarray( np.clip(dataRG,0,255), dtype="uint8"))
    imgRG.show()
    imgRG.save(name+"RG"+ext)
    imgRGB = Image.fromarray(np.asarray( np.clip(dataRGB,0,255), dtype="uint8"))
    imgRGB.show()
    imgRGB.save(name+"RGB"+ext)
#simulatePrint(".\images\me.jpg")
#simulatePrint(".\images\me2.jpg")
simulatePrint(".\images\shoes.jpg")
