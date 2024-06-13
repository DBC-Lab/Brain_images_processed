# Brain image results for ADNI (Alzheimer's Disease Neuroimaging Initiative) dataset processed by iBEAT V2.0.

The results inlcude (1) cerebrum tissue segmentation (CSF, GM and WM), and (2) parcellation results. 

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

   <img src="https://github.com/DBC-Lab/Brain_images_processed/blob/main/ADNI_Alzheimer's_Disease_Neuroimaging_Initiative/ADNI.png" width="50%">


# Brain image results for OASIS (Open Access Series of Imaging Studies) dataset processed by iBEAT V2.0.

The results inlcude (1) cerebrum tissue segmentation (CSF, GM and WM), and (2) parcellation results. 

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

   <img src="https://github.com/DBC-Lab/Brain_images_processed/blob/main/OASIS_Open_Access_Series_of_Imaging_Studies/OASIS.png" width="50%">

