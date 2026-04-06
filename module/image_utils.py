import cv2
import numpy as np
import json
import easyocr

def process_images(config_dict):
    config_path = config_dict['config']
    snapshot_paths = config_dict['snapshots']
    snapshot_base_dir = config_dict['snapshot_base_dir']
    
    reader = easyocr.Reader(['tr'], gpu=False, model_storage_directory=".EasyOCR/model")
    
    for snapshot_path in snapshot_paths:
        results = detect_text_regions(snapshot_path, config_path, reader)
        #print(f"Results for {snapshot_path}:")
        for (bbox, text, confidence) in results:
            print(f"Text: {text}, Confidence: {confidence}")

def detect_text_regions(image_path, region_cfg_path, reader=None):
    # Load the image
    image = cv2.imread(image_path)
    
    # Load the region configuration
    with open(region_cfg_path, 'r') as f:
        region_cfg = json.load(f)
    
    # Extract the main region coordinates
    main_region_coords = np.array(region_cfg['main_region'], dtype=np.int32)
    
    # Create a mask for the main region
    mask = np.zeros(image.shape[:2], dtype=np.uint8)
    cv2.fillPoly(mask, [main_region_coords], 255)
    
    # Apply the mask to the image
    masked_image = cv2.bitwise_and(image, image, mask=mask)
    
    # Use EasyOCR to detect text in the masked image    
    results = reader.readtext(masked_image)
    
    return results