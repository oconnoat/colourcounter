from PIL import Image, ImageDraw
from collections import Counter

rgbim = Image.open('photo.jpg').convert('RGB')
colours = Counter()

# get the colour count info
for i in xrange(rgbim.height):
    for j in xrange(rgbim.width):
        rgb = rgbim.getpixel((i,j))
        colours.update({','.join(str(i) for i in rgb):1})

# write images
outputim = Image.new('RGB',(240,300), (255,255,255))
draw = ImageDraw.Draw(outputim)

for i, (colour, count) in enumerate(colours.most_common(150)):
    rgbval = tuple(int(v) for v in colour.split(','))
    draw.rectangle([(i%10 * 20) + 22, i/10 * 20 + 2 , 40 + (i%10 * 20), 20
        +(i/10 * 20)],
            rgbval,
            (0,0,0)
            )
    outputim.save('out.jpg')
