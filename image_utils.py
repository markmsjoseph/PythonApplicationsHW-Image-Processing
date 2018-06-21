from PIL import Image
# Only the grayscale and Kalidascope work

img = Image.open('quokka.jpg')

def flipAcrossXaxis(orig_img):
    width, height = orig_img.size;
    img = Image.new('RGB', (width, height))
    pixels = img.load()
    orig_pixels = orig_img.load()

    for x in range(width):
        for y in range(height):
            # we want to flip upside down so x values will be the same
            # but y values will start from the bottom come up
            newY = height - y -1
            pixels[x, y] = orig_pixels[x,newY]

    return img

def flipAcrossYaxis(orig_img):
    width, height = orig_img.size;
    img = Image.new('RGB', (width, height))
    pixels = img.load()
    orig_pixels = orig_img.load()
    # we flip across the x axis so y values will remain the same
    for x in range(width):
        for y in range(height):
            newX = width - x -1
            pixels[x, y] = orig_pixels[newX, y]
    return img

# make image grey
def grayDay(img):
    width,height = img.size
    pixels = img.load()
    for i in range(width):
        for j in range(height):
            add = sum(pixels[i,j])
            avg = add // 3
            pixels[i,j] = (avg,avg,avg)
    img.show()

# kscope
def kscope(origImg):
    width,height = origImg.size
    orig_pixels = origImg.load()
    lowerLeft = origImg.load()

    #perform various flips before we resize the image and place in correct quadrant
    upperLeftImageHorizontally = flipAcrossXaxis(origImg)
    upperLeftImagePixels = upperLeftImageHorizontally.load()

    im2H = flipAcrossXaxis(origImg)
    im2HY = flipAcrossYaxis(im2H)
    upperRightImagePixels = im2HY.load()

    im4V = flipAcrossYaxis(origImg)
    lowerRightImagePixels = im4V.load()


    # lower left quadrant
    for x in range(0,width//2):
        ycnt = 0
        for y in range(height//2, height):
            orig_pixels[x, y] = lowerLeft[x*2,ycnt * 2]
            ycnt = ycnt + 1


    # upper left quadrant
    for x in range(width//2):
        for y in range(height//2):
            orig_pixels[x, y] = upperLeftImagePixels[x*2,y*2]


    # upper right quadrant
    xcnt = 0
    for x in range(width//2,width):
        for y in range(height//2):
                orig_pixels[x, y] = upperRightImagePixels[xcnt*2,y*2]
        xcnt = xcnt + 1


    # lower right quadrant
    xcnt = 0
    for x in range(width//2, width):
        ycnt = 0
        for y in range(height//2, height):
            orig_pixels[x, y] = lowerRightImagePixels[xcnt*2,ycnt * 2]
            ycnt = ycnt + 1
        xcnt = xcnt + 1


    origImg.show()


def enlarge(origImage):
    height,width = origImage.size
    origPixels = origImage.load()
    newiImg = Image.new('RGB', (height*2, width*2))
    newPixels = newiImg.load()

    for row in range(height):
        for col in range(width):
            #fill the columns by 4 blocks each
            #need to multiply by 2 so on second iteration we do not write over the previous block
            newPixels[2*row,2*col] = origPixels[row,col]
            newPixels[2*row,2*col+1] = origPixels[row,col]
            newPixels[2*row+1,2*col] = origPixels[row,col]
            newPixels[2*row+1,2*col+1] = origPixels[row,col]

    newiImg.show()

#rotate the original image without creating a new one
def rotateLeft(origImg):

    width,height = origImg.size
    orig_pixels = origImg.load()





# def pixelate(origImg):
#     width,height = origImg.size
#     orig_pixels = origImg.load()
#
#     newiImg = Image.new('RGB', (height, width))
#     newPixels = newiImg.load()
#
#     xcnt = 0
#     for x in range(height,0,-1):
#         ycnt = 0
#         for y in range(0,width):
#             newPixels[xcnt, ycnt] = orig_pixels[x,y]
#             ycnt = ycnt + 1
#         xcnt = xcnt + 1
#
#
#
#     newiImg.show()
#
# pixelate(img)

# arr = [[ 1,2,3,4,5,6,7,8,9],
#         [1,2,3,4,5,6,7,8,9],
#         [1,2,3,4,5,6,7,8,9]]
#
# newarr =[[1,2,3,4,5,6,7,8,9],
#          [1,2,3,4,5,6,7,8,9],
#          [1,2,3,4,5,6,7,8,9]]
# k = 0
# z = 0
# for j in range(0,len(arr),3):
#      if(j%3 == 0):
#          while z < j+3:
#             newarr[j][z] = arr[j][z]
#             for i in range(0,len(arr),3):
#                 if(i%3 == 0):
#                     while k < i+3:
#                         newarr[j][k] = arr[j][i]
#                         k = k + 1
#             z = z + 1
#
#
# print(newarr)
#


