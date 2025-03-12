Before you start, you must have obtained access to the original ADNI data and have the authorized right from ADNI to use the ADNI MRI data (http://adni.loni.usc.edu), and you must fully agree to abide by the terms of Data Use Agreement from ADNI (http://adni.loni.usc.edu/wp-content/uploads/how_to_apply/ADNI_Data_Use_Agreement.pdf)

Before you start, you must have obtained access to the original OASIS3 data and have the authorized right from OASIS3 to use the OASIS3 MRI data (https://www.oasis-brains.org/#access), and you must fully abide by the terms of Data Use Agreement from OASIS (https://www.oasis-brains.org/#access).



# Brain image results for ADNI (Alzheimer's Disease Neuroimaging Initiative) dataset processed by iBEAT V2.0.

The results include tissue segmentation (CSF, GM and WM). 

__Please download the results from https://www.dropbox.com/scl/fo/2n3t7xciakfgrv48s1f51/AHIDNge5Is6RvjR7r1c3IaM?rlkey=hsxdkp2em5zo2mxql870exwph&st=m6uwbqcr&dl=0.__ 

Please note that the data in folder ***002_S_0295*** and __*-T1w.nii.gz__ can only be used as examples to match the spatial orientation and resolution of the processed results. 

## MR images from ADNI

1. Please download ADNI images from https://ida.loni.usc.edu/login.jsp. One example is in folder ***002_S_0295***. 
2. Please use __T1w_space_consistency_for_ADNI.py__ to match the spatial orientation and resolution of the processed results.

   `python3 T1w_space_consistency_for_ADNI.py`

    #### Inputs:

      a. The download images from ADNI, e.g., ***002_S_0295***.

      b. The corresponding processed results, e.g., __ADNI_002_S_0295_MR_MP-RAGE__br_raw_20061102123250714_1_S21856_I28561-n3-resample-reorient-stripped-n3-iBEAT.nii.gz__
   
    #### Outputs:

      The processed images, e.g., __ADNI_002_S_0295_MR_MP-RAGE__br_raw_20061102123250714_1_S21856_I28561-T1w.nii.gz__.
   
The processed images and brain image results are shown as the following:

 ![ADNI](https://github.com/DBC-Lab/Brain_images_processed/assets/110405481/065d5bca-22cd-4221-8388-3349068ecf12)



# Brain image results for OASIS (Open Access Series of Imaging Studies) dataset processed by iBEAT V2.0.

__Please download the results from https://www.dropbox.com/scl/fo/xrm46gl91ywbfvcvqhrnp/AH4ptI_hU5X_hLsjt50tP2k?rlkey=pygv9iskmpukj2p3immue9fwk&st=0se2g090&dl=0.__ 

Please note that the image data in folder ***OAS31170_Freesurfer53_d2410_Freesurfer***, ***OAS31172_Freesurfer53_d0407_Freesurfer*** and __*T1w_from_FreeSurfer.nii.gz__ can only be used as examples to match the spatial orientation and resolution of the processed results. 

## MR images from OASIS

1. Please download OASIS images processed by FreeSurfer from xxxx. One example is in folder ***OAS31170_Freesurfer53_d2410_Freesurfer***. 
2. Please use __T1w_space_consistency_for_OASIS3.py__ to match the spatial orientation and resolution of the processed results.

   `python3 T1w_space_consistency_for_OASIS3.py`

    #### Inputs:

      a. The download images from OASIS, e.g., ***OAS31170_Freesurfer53_d2410_Freesurfer***.

      b. The corresponding processed results, e.g., __OAS31170_MR_d2410-iBEAT.nii.gz__
   
    #### Outputs:

      The processed images, e.g., __OAS31170_MR_d2410_T1w_from_FreeSurfer.nii.gz__.
   
The processed images and brain image results are shown as the following:

![OASIS](https://github.com/DBC-Lab/Brain_images_processed/assets/110405481/83e628fd-0f63-4b73-ad33-f96c14068cc4)
