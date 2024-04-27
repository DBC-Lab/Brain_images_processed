import SimpleITK as sitk
import numpy as np
import os
import cv2
import subprocess

def convert_mgz_to_nii(mgz_file, nii_file):
    try:
        subprocess.run(['mri_convert', '--out_orientation', 'RAI', mgz_file, nii_file])
        print("Conversion successful!")
    except FileNotFoundError:
        print("Error: 'mri_convert' command not found. Make sure FreeSurfer is installed and in your PATH.")

datapath = './'

for root, dirs, files in os.walk(datapath):
    for file in files:
        if file.endswith('orig.mgz'):
            dataT1filename = os.path.join(root, file)
            print(dataT1filename)
            temp = dataT1filename.split('_Freesurfer53_')
            id1 = temp[0].strip()
            id1 = id1[2:]
            id2 = temp[1].strip()
            id2 = id2[0:5]
             
            nii_file = id1 + '_MR_' + id2 + '_T1w_from_FreeSurfer.nii.gz'
            convert_mgz_to_nii(dataT1filename, nii_file)

            # Step 1: Get image data matrix
            struct_hdr = sitk.ReadImage(nii_file)
            img_np = sitk.GetArrayFromImage(struct_hdr)  # img_np: Actuall image matrix.

            # Step 2: Reorient data
            final_result = np.zeros([256,256,256])
            flipped_img_np1 = np.flip(img_np, axis=0)
            flipped_img_np2 = np.flip(flipped_img_np1, axis=1)
            flipped_img_np = np.flip(flipped_img_np2, axis=2)
            final_result[1:-1,:,:] = flipped_img_np[0:-2,:,:]

            # Step 3: Get reference nii struct
            ref_nii = sitk.ReadImage(id1 + '_MR_' + id2 + '-iBEAT.nii.gz')  # file_orig_nii: The original nii file with correct header.

            # Step 4: Create the result nii
            result_nii = sitk.GetImageFromArray(final_result)  # struct_nii: the nii struct.

            # Step 5: Copy the header information
            result_nii.SetOrigin(ref_nii.GetOrigin())
            result_nii.SetDirection(ref_nii.GetDirection())
            result_nii.SetSpacing(ref_nii.GetSpacing())
            pixelID = result_nii.GetPixelID()
            caster = sitk.CastImageFilter()
            caster.SetOutputPixelType(pixelID)
            result_nii = caster.Execute(result_nii)
            result_nii = sitk.Cast(result_nii, sitk.sitkUInt16)  # Uint16 is short type;

            sitk.WriteImage(result_nii, nii_file)

