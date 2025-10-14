# 🧠 Custom MONAI — ImagingIQ Edition

This repository is a **customized version of MONAI**, enhanced with post-processing functionality for medical image segmentation pipelines.

---

## 🩺 Key Additions

### 🔹 `ReplaceLowConfidenceWithAtlasd` and `ReplaceLowConfidenceWithAtlas`

These two new post-processing transforms are added under:

- `monai/transforms/post/array.py`  
- `monai/transforms/post/dictionary.py`  

#### **Purpose**
These functions refine segmentation masks produced by the pipeline by leveraging a **Colin atlas**.  
They replace low-confidence regions in the predicted mask with atlas-based anatomical information, improving overall segmentation consistency and anatomical accuracy.

#### **Use Case**
Ideal for **brain MRI segmentation** or similar volumetric tasks where anatomical priors enhance low-confidence predictions.

---

## ⚙️ MONAI Directory Overview

| Module | Description |
|:--|:--|
| **apps** | High-level medical domain-specific deep learning applications. |
| **auto3dseg** | Automated machine learning (AutoML) components for volumetric image analysis. |
| **bundle** | Tools to build portable, self-descriptive model bundles. |
| **config** | System configuration and diagnostic utilities. |
| **csrc** | C++/CUDA extensions. |
| **data** | Datasets, readers/writers, and synthetic data generation. |
| **engines** | Ignite engine-derived classes for training pipeline management. |
| **fl** | Federated learning integration components. |
| **handlers** | Event-based handlers for different training stages. |
| **inferers** | Model inference methods. |
| **losses** | Loss functions following the `torch.nn.modules.loss` pattern. |
| **metrics** | Metric computation and tracking utilities. |
| **networks** | Network definitions and PyTorch utilities. |
| **optimizers** | Optimizers following the `torch.optim` pattern. |
| **transforms** | Data preprocessing, augmentation, and postprocessing transforms. |
| **utils** | General-purpose utilities (implemented in Python/Numpy, not PyTorch). |
| **visualize** | Visualization tools for medical imaging. |
| **_extensions** | JIT-loaded C++/CUDA extensions. |

---

## 🚀 Installation (Developer Mode)

To install **this custom MONAI version** with the new atlas-based postprocessing transforms:

```bash
# Clone the ImagingIQ custom MONAI repository
git clone https://github.com/ImagingIQ/Monai.git

# Enter the repository
cd Monai

# Install in editable (developer) mode
pip install -e .

# Return to your working directory
cd ..
