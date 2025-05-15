import imageio.v3 as iio

filenames=['1.png','2png']
images=[ ]

for f in filenames:
    
    images.append(iio.imread(f))
    
iio.imwrite('p.gif',images,duration=500,loop=0)