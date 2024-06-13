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

