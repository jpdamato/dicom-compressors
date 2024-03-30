import nibabel as nib
import numpy as np
import matplotlib.pyplot as plt
import os

inputPath = 'd://Resources//DICOM//Niis//'

#convert to RAW format
for i in range(1, 30):
    if i < 10 :
        srcPath =inputPath+ 'coronacases_org_00'+str(i)
    else:
        srcPath =inputPath+ 'coronacases_org_0'+str(i)
    if not os.path.exists(srcPath+'.nii'):
        print(f"Error: File '{srcPath}' does not exist.")
        
    test_load = nib.load(srcPath+'.nii').get_fdata()
    test_load = np.array(test_load, dtype=np.int16)
    
    print(test_load.shape)

    np.save(srcPath, test_load)


test = test_load[:,:,1]

plt.imshow(test)
plt.show()