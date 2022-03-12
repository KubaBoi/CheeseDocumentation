import imageio
from PIL import Image


def create(name, size):
    imshape = imageio.imread(f"{name}")
    print(imshape.shape)

    im = Image.open(f"{name}")
    pixels = im.convert("RGB")

    newIm = Image.new(mode="RGBA", size=(imshape.shape[0]*size, imshape.shape[1]*size))

    for x in range(0, imshape.shape[0]):
        for y in range(0, imshape.shape[1]):
            for x1 in range(0, size):
                for y1 in range(0, size):
                    newIm.putpixel((x*10+x1, y*10+y1), pixels.getpixel((x, y)))

    newIm.show()
    newIm.save("documentation300x300.png")


create("src/resources/web/documentation.png", 10)