import nibabel as nib
import os
from medpy.io import load, save
import numpy as np

data_path='./mask/'
save_path='./mask/convert/test/'

test = [32,34,38,41,47,87,89,91,105,106,114,115,119]

for idx in test:
    seg, seg_header  = load(str(data_path) + 'segmentation-' + str(idx) + '.nii')
    print('Loading Segmentation-' + str(idx))
    index = np.where(seg==1)
    mini = np.min(index, axis =-1)
    maxi = np.max(index, axis =-1)
    #seg[seg==1]=0
    #save(seg, save_path + 'segmentation-' + str(idx) + '.nii')
    print(mini)
    print(maxi)

#for idx in range(100,200)
