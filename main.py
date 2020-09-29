import folium
import webbrowser
from PIL import Image, ExifTags

def getExif(image):
    extraction = {}
    img = Image.open(image)
    info = img._getexif()
    for tag, value in info.items():
        decoded = ExifTags.TAGS.get(tag, tag)
        if tag in ExifTags.TAGS:
            extraction[decoded] = value
    return extraction

nomImage = str(input("Le nom de votre image : "))
GPS = getExif(nomImage)["GPSInfo"]

def cord(x):
    return x[2][0][0]/x[2][0][1] + x[2][1][0]/x[2][1][1]/60 + x[2][2][0]/x[2][2][1]/3600, x[4][0][0]/x[4][0][1] + x[4][1][0]/x[4][1][1]/60 + x[4][2][0]/x[4][2][1]/3600

x = cord(GPS)[0]
y = cord(GPS)[1]

if GPS[3] == 'W':
    y = float(-y)
else:
    y = y

if GPS[1] == 'S':
    x = float(-x)
else:
    x = x
    
carte= folium.Map(location=[x, y], zoom_start=15)

folium.Marker(location=[x, y], popup = 'C’est ici !',  icon=folium.Icon(color='red')).add_to(carte)

carte.save('carte.html')
webbrowser.open('carte.html',new = 2)
