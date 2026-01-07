def triangleInspector(sideA, sideB, sideC,):

    # Tälläin vois tarkastaa onko annetut arvot integerei, mutta kun se on jo UI puolella "estetty" tuohon ei ikinä päästäisi.
    # Mutta jos nyt jotenkin saadaan syötettyä stringi sanitoinin läpi niin jätetää tähän, niin saadaan test case tehtyä.
    if not (isinstance(sideA, int) and isinstance(sideB, int) and isinstance(sideC, int)):
        return "All of the inputs must be integers."

    if(sideA <= 0 or sideB <= 0 or sideC <= 0):
        return "While it's possible to draw negative triangles on the x and y axis, here it is not."
    
    if (sideA + sideB <= sideC or sideA + sideC <= sideB or sideB + sideC <= sideA):
        return "The triangle is not valid"
    
    if (sideA == sideB == sideC):
        return "Triangle is equilateral"
    elif (sideA == sideB or sideB == sideC or sideA == sideC):
        return "The triangle is isosceles"
    else:
        return "The triangle is scalene"  

# JANNE VILJANEN TKM24