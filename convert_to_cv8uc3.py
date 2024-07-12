# Run this file in Google Colab, transfer rosbag file to pcd file


import cv2
from google.colab import files

def convert_image_to_cv8uc3(image_path, output_path):
    # Read the image
    image = cv2.imread(image_path)

    if image is None:
        print(f"Error: Cannot read image from {image_path}")
        return

    # Check the number of channels in the image
    if len(image.shape) == 2:
        # If the image is already single-channel (grayscale), convert it to 3-channel by duplicating the channel
        image_cv8uc3 = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    else:
        # Convert to 3-channel color image
        image_cv8uc3 = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Save the converted image
    cv2.imwrite(output_path, image_cv8uc3)
    print(f"Image saved to {output_path} in CV_8UC3 format")

# Step 1: Upload images
uploaded = files.upload()

# Step 2: Process each uploaded image
for image_name in uploaded.keys():
    convert_image_to_cv8uc3(image_name, 'output_' + image_name.split('.')[0] + '_cv8uc3.png')

# Step 3: Download the output images
for image_name in uploaded.keys():
    files.download('output_' + image_name.split('.')[0] + '_cv8uc3.png')

