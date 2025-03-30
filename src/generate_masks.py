import os
import json
import numpy as np
import cv2
from pycocotools.coco import COCO

# Define paths
annotation_path = r"D:\Brain Tumor\brain-tumor-segmentation(Using Dataset)\data\_annotations.coco.json"
mask_output_dir = r"D:\Brain Tumor\brain-tumor-segmentation(Using Dataset)\data\train\masks"
os.makedirs(mask_output_dir, exist_ok=True)

# Load COCO dataset
coco = COCO(annotation_path)
image_ids = coco.getImgIds()

# Convert annotations to masks
for image_id in image_ids:
    ann_ids = coco.getAnnIds(imgIds=image_id)
    anns = coco.loadAnns(ann_ids)
    img_info = coco.loadImgs(image_id)[0]
    mask = np.zeros((img_info["height"], img_info["width"]), dtype=np.uint8)

    for ann in anns:
        if "segmentation" in ann:
            for seg in ann["segmentation"]:
                polygon = np.array(seg, dtype=np.int32).reshape((-1, 2))
                cv2.fillPoly(mask, [polygon], color=255)

    mask_filename = os.path.join(mask_output_dir, img_info["file_name"].replace(".jpg", "_mask.png"))
    cv2.imwrite(mask_filename, mask)

print("Masks saved successfully!")
  
