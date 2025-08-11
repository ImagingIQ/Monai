import os
from monai.transforms import LoadImage
from monai.data.meta_tensor import MetaTensor

def load_atlas(atlas_name: str) -> MetaTensor:
    """
    Load a NIfTI atlas segmentation file and return it as a MetaTensor.
    """
    monai_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    atlas_dir = os.path.join(monai_dir, "atlas")

    possible_exts = [".nii.gz", ".nii"]
    atlas_path = None
    for ext in possible_exts:
        candidate = os.path.join(atlas_dir, atlas_name + ext)
        if os.path.exists(candidate):
            atlas_path = candidate
            break

    if atlas_path is None:
        raise FileNotFoundError(
            f"Could not find atlas '{atlas_name}' in {atlas_dir} with extensions {possible_exts}"
        )

    loader = LoadImage(image_only=True)  # returns MetaTensor by default
    img_data = loader(atlas_path)
    return img_data

# def load_atlas(atlas_name: str) -> MetaTensor:
#     """
#     Load an atlas segmentation file by name and return it as a MetaTensor.

#     Args:
#         atlas_name (str): Name of the atlas file (without extension), e.g., "Colin".

#     Returns:
#         MetaTensor: Loaded atlas as a MetaTensor.
#     """
#     # Dir path of the dir just above this current file 
#     monai_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
#     # Path of the atlas file obtained by joining monai_dir and atlas 
#     atlas_dir = os.path.join(monai_dir, "atlas")

#     # Trying out all extensions
#     possible_exts = [".nii.gz", ".nii", ".npy"]
#     atlas_path = None
#     for ext in possible_exts:
#         candidate = os.path.join(atlas_dir, atlas_name + ext)
#         if os.path.exists(candidate):
#             atlas_path = candidate
#             break

#     if atlas_path is None:
#         raise FileNotFoundError(
#             f"Could not find atlas '{atlas_name}' in {atlas_dir} with extensions {possible_exts}"
#         )

#     nifti_img = nib.load(atlas_path)  
#     np_data = nifti_img.get_fdata()
#     affine = nifti_img.affine

#     tensor_data = torch.from_numpy(np_data).float()
#     meta_tensor = MetaTensor(tensor_data, affine=affine)

#     return meta_tensor


