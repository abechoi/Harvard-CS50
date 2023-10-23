import sys
from PIL import Image

images = []

# iterate image paths from command line, excluding the script name
for arg in sys.argv[1:]:
    # open each image
    image = Image.open(arg)
    # append each image to the list
    images.append(image)

# save the first image as a gif, appending the second image
#  "costumes.gif" - name of the gif
#  save_all=True - save all frames
#  append_images=[images[1]] - append the second image
#  duration=200 - duration of each frame in milliseconds
#  loop=0 - loop forever
images[0].save(
    "costumes.gif", save_all=True, append_images=[images[1]], duration=200, loop=0
)