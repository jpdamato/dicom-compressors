import ipywidgets as widgets
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RangeSlider


import imageio
import cv2

scale_pix = 10

inputPath = 'e:/Resources/DICOM'

def convert_8bit_to_16bit(image):
    # Normalize the input image to the range [0, 1]
    normalized_image = image.astype(np.float32) 
    
    # Stretch the range to [0, 65535]
    stretched_image = (normalized_image * scale_pix - 1024).astype(np.int16)
    
    return stretched_image

#Stacking 99 slices
vol = imageio.volread(inputPath+'/lung/', 'DICOM')

# The shape of the stacked images in each plane
# (Axial, Coronal, and Sagittal, respectively)
n0, n1, n2 = vol.shape
# Print the ouput
print("Number of Slices:\n\t", "Axial=", n0, "Slices\n\t",
                               "Coronal=", n1, "Slices\n\t",
                               "Sagittal=", n2, "Slices")

                               # Define a figure with 1 row and 3 columns of plots to show
# The sampling of the stacked images in each plane
# (Axial, Coronal, and Sagittal, respectively)
d0, d1, d2 = vol.meta['sampling'] # in mm
# Print the output
print("Sampling:\n\t", "Axial=", d0, "mm\n\t",
                               "Coronal=", d1, "mm\n\t",
                               "Sagittal=", d2, "mm")

# The aspect ratio along the axial plane
axial_asp = d1/d2
# The aspect ratio along the sagittal plane
sagittal_asp = d0/d1
# The aspect ratio along the coronal plane
coronal_asp = d0 / d2


axial_slice = 1

np.save(inputPath+'lung.raw', vol)

img = vol[axial_slice,:,:]

img2 = cv2.imread(inputPath+'/lung/jpeg/' + str(axial_slice) + '.jpg', cv2.IMREAD_GRAYSCALE)

img2 = convert_8bit_to_16bit(img2)

fig, axs = plt.subplots(1, 4, figsize=(10, 5))
fig.subplots_adjust(bottom=0.25)

im = axs[0].imshow(img)
im2 = axs[1].imshow(img2) 
dif = img - img2


axs[2].hist(img.flatten(), bins='auto')
axs[2].set_title('Histogram of pixel intensities')

axs[3].hist(img2.flatten(), bins='auto')
axs[3].set_title('Histogram of pixel intensities')



axamp = fig.add_axes([0.1, 0.25, 0.0225, 0.63])
slider2 = Slider(axamp, "Plane", 0, n0, orientation="vertical")


    
def update(val):
    # The val passed to a callback by the RangeSlider will
    # be a tuple of (min, max)
    axial_slice = int(slider2.val)

    img = vol[axial_slice,:,:]
    
    img2 = cv2.imread(inputPath+'/lung' + str(axial_slice) + '.jpg', cv2.IMREAD_GRAYSCALE)
    
    img2 = convert_8bit_to_16bit(img2)


    dif = img - img2
    
    im = axs[0].imshow(img)
    im2 = axs[1].imshow(dif)

    axs[2].hist(img.flatten(), bins='auto')
    axs[3].hist(img2.flatten(), bins='auto')

    cv2.imshow("orig", img)
    cv2.imshow("other", img2)
    cv2.imshow("dif", dif)
    cv2.waitKey(1)
    
    
    # Update the image's colormap
   # im.norm.vmin = val[0]
   # im.norm.vmax = val[1]

   # im2.norm.vmin = val[0]
   # im2.norm.vmax = val[1]

    # Redraw the figure to ensure it updates
    fig.canvas.draw_idle()


slider2.on_changed(update)

plt.show()