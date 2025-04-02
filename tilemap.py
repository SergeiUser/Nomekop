from pygame import image as pygameImage
from pygame import surface as pygameSurface
from pygame import transform
from random import choices, seed
Grasses = [
        pygameImage.load("Nomekop/Assets/Tiles/Grass0 - 0.png"),
        pygameImage.load("Nomekop/Assets/Tiles/Grass0 - 1.png"),
        pygameImage.load("Nomekop/Assets/Tiles/Grass0 - 2.png"),
        pygameImage.load("Nomekop/Assets/Tiles/Grass0 - 3.png"),
        pygameImage.load("Nomekop/Assets/Tiles/Grass0 - 4.png"),
]
RoadsH = [
        pygameImage.load("Nomekop/Assets/Tiles/Road3 - 0.png"),
        pygameImage.load("Nomekop/Assets/Tiles/Road3 - 1.png"),
]
RoadsV = [
        pygameImage.load("Nomekop/Assets/Tiles/Road1 - 0.png"),
        pygameImage.load("Nomekop/Assets/Tiles/Road1 - 1.png"),
]
RoadsTurns = [
        pygameImage.load("Nomekop/Assets/Tiles/Road2 - 0.png"),
        pygameImage.load("Nomekop/Assets/Tiles/Road2 - 1.png"),
        pygameImage.load("Nomekop/Assets/Tiles/Road2 - 2.png"),
        pygameImage.load("Nomekop/Assets/Tiles/Road2 - 3.png"),
]
N = 0
G = 1
W = 2
RH = 3
RV = 4
RC = 5
RT = 6

textures = {
        N  : pygameImage.load("Nomekop/Assets/Tiles/Road0.png"),
        G  : (Grasses, [5,1,3,3,3]),
        W  : ([pygameImage.load("Nomekop/Assets/Tiles/Water1.png")], [1]),
        RH : (RoadsH, [1,1]),
        RV : (RoadsV, [1,1]),
        RC : ([pygameImage.load("Nomekop/Assets/Tiles/Road4.png")], [1]),
        RT : RoadsTurns
}
tilemap = [
    [G,     G, G, G, G,    G, G, G, G, G,     G, G, G, RV,    G, G,     G,N,N,N],#0
    [(RT,2),G, G, G,(RT,1),RH,RH,RH,RH,(RT,2),G, G, G, RV,    G, G,     G,N,N,N],#1
    [RV,    G, G, G, RV,   G, G, G, G, RV,    G, G, G, RV,    G, G,     G,N,N,N],#2
    [RV,    G, G, G, RV,   G, G, G, G, RV,    G, G, G, RV,    G, G,     G,N,N,N],#3
    [RV,    G, G, G, RV,   G, G, G, G, RV,    G, G, G, RV,    G, G,     G,N,N,N],#4
    [(RT,0),RH,RH,RH,RC,   RH,RH,RH,RH,(RT,3),G, G, G, RV,    G, G,     G,N,N,N],#5
    [G,     G, G, G, RV,   G, G, G, G, G,     G, G, G, RV,    G, G,     G,N,N,N],#6
    [G,     G, G, G,(RT,0),RH,RH,RH,RH,RH,    RH,RH,RH,RC,    RH,(RT,2),G,N,N,N],#7
    [G,     G, G, G, G,    G, G, G, G, G,     G, G, G, RV,    G,  RV,   G,N,N,N],#8
    [G,     G, G, G, G,    G, G, G, G, G,     G, G, G,(RT,0), RH,(RT,3),G,N,N,N],#9
]



tilesize = 64
mapwidth = 4
mapheight = 4


def drawBackground(display, cellSizes, gameSeed):
        for row in range(len(tilemap)):
                for column in range(len(tilemap[row])):
                        if str(type(tilemap[row][column])) == "<class 'tuple'>":
                                textureTuple = tilemap[row][column]
                                texture = textures[textureTuple[0]][textureTuple[1]]
                        else:
                                texture = textures[tilemap[row][column]]
                        if str(type(texture)) == "<class 'tuple'>":
                                image = texture[0][0]#choices(texture[0], texture[1])[0]
                        else:
                                image = texture

                        destination = (column*cellSizes[0], row*cellSizes[0])

                        image = transform.scale(image, (cellSizes[0],cellSizes[1]))
                        display.blit(image, destination)
