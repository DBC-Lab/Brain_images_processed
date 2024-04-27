import SimpleITK as sitk
import numpy as np
import os
import cv2
import subprocess
from scipy.ndimage import zoom
import nibabel as nib

def dcm2nii(dcms_path, nii_path):
    # 1. Build a DICOM series file reader and execute it (i.e., "integrate" DICOM series files)
    reader = sitk.ImageSeriesReader()
    dicom_names = reader.GetGDCMSeriesFileNames(dcms_path)
    reader.SetFileNames(dicom_names)
    image2 = reader.Execute()
    
    # 2. Convert the integrated data to an array and retrieve basic DICOM file information
    image_array = sitk.GetArrayFromImage(image2) 
    origin = image2.GetOrigin()  
    spacing = image2.GetSpacing()  
    direction = image2.GetDirection()  
    
    # 3. Convert the array to an image and save it as .nii.gz
    image3 = sitk.GetImageFromArray(image_array)
    image3.SetSpacing(spacing)
    image3.SetDirection(direction)
    image3.SetOrigin(origin)
    sitk.WriteImage(image3, nii_path)

datapath = './'

for path, dir_lst, _ in os.walk('./', topdown=True):
    if not dir_lst:  # If there are no subfolders in the current path, it is the last layer of the folder.
        temp = path.split('/I')
        id = 'I' + temp[1].strip()
        print(id)

        # Step 1: Get reference nii struct
        ref_file=[i for i in os.listdir(datapath) if id in i and '-iBEAT.nii.gz' in i ]
        ref_filename = ref_file[0]
        ref_nii = sitk.ReadImage(ref_filename)  # file_orig_nii: The original nii file with correct header.
        img_ref = sitk.GetArrayFromImage(ref_nii)

        # Step 2: Get image data matrix
        temp = ref_filename.split('-n3-resample-reorient-stripped-n3-iBEAT.nii.gz')
        filename = temp[0].strip()
        print(filename)
        nii_filename = filename + '-T1w.nii.gz'
        dcm2nii(path, nii_filename)
        struct_hdr = sitk.ReadImage(nii_filename)
        img_np = sitk.GetArrayFromImage(struct_hdr)  # img_np: Actuall image matrix.

        # Step 3: Reorient and resample
        img_np=np.transpose(img_np,(1,2,0))
        flipped_img_np = np.flip(img_np, axis=0)
        flipped_img_np = np.flip(flipped_img_np, axis=2)
        result_space = struct_hdr.GetSpacing()
        ref_space = ref_nii.GetSpacing()
        new_shape = (int(flipped_img_np.shape[0]*result_space[0]/ref_space[0]), int(flipped_img_np.shape[1]*result_space[1]/ref_space[1]), int(flipped_img_np.shape[2]*result_space[2]/ref_space[2]))
        print(new_shape)
        resampled_img_np = zoom(flipped_img_np, new_shape / np.array(flipped_img_np.shape))
        result_nii = sitk.GetImageFromArray(resampled_img_np)  # struct_nii: the nii struct.

        # Step 4: Copy the header information
        result_nii.SetOrigin(ref_nii.GetOrigin())
        result_nii.SetDirection(ref_nii.GetDirection())
        result_nii.SetSpacing(ref_nii.GetSpacing())
        pixelID = result_nii.GetPixelID()
        caster = sitk.CastImageFilter()
        caster.SetOutputPixelType(pixelID)
        result_nii = caster.Execute(result_nii)
        result_nii = sitk.Cast(result_nii, sitk.sitkUInt32)  #Uint16 is short type;

        sitk.WriteImage(result_nii, filename + '-T1w.nii.gz')

