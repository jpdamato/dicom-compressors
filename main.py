import ipywidgets as widgets
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RangeSlider


import imageio


#Reading a DICOM Image
im = imageio.v2.imread('D:/Resources/DICOM/lung/000009.dcm')

#DICOM Metadata
print(im.meta)

#Stacking 99 slices
vol = imageio.volread('D:/Resources/DICOM/lung/', 'DICOM')

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

np.save('D:/Resources/DICOM/lung.raw', vol)

img = vol[axial_slice,:,:]


fig, axs = plt.subplots(1, 2, figsize=(10, 5))
fig.subplots_adjust(bottom=0.25)

im = axs[0].imshow(img)
axs[1].hist(img.flatten(), bins='auto')
axs[1].set_title('Histogram of pixel intensities')

# Create the RangeSlider
slider_ax = fig.add_axes([0.20, 0.1, 0.60, 0.03])
slider = RangeSlider(slider_ax, "Threshold", img.min(), img.max())

axamp = fig.add_axes([0.1, 0.25, 0.0225, 0.63])
slider2 = Slider(axamp, "Plane", 0, n0, orientation="vertical")

# Create the Vertical lines on the histogram
lower_limit_line = axs[1].axvline(slider.val[0], color='k')
upper_limit_line = axs[1].axvline(slider.val[1], color='k')


    
def update(val):
    # The val passed to a callback by the RangeSlider will
    # be a tuple of (min, max)
    axial_slice = int(slider2.val)

    img = vol[axial_slice,:,:]
    im = axs[0].imshow(img)
    axs[1].hist(img.flatten(), bins='auto')
    
    # Update the image's colormap
    im.norm.vmin = val[0]
    im.norm.vmax = val[1]

    # Update the position of the vertical lines
    lower_limit_line.set_xdata([val[0], val[0]])
    upper_limit_line.set_xdata([val[1], val[1]])

    # Redraw the figure to ensure it updates
    fig.canvas.draw_idle()


slider.on_changed(update)

slider2.on_changed(update)

plt.show()