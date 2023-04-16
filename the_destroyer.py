import os
import datetime
import time
import pytz
from important_pts_tkmce.important_pts import web_img_path,api_img_path


# Set the time zone to Asia/Kolkata
tz = pytz.timezone('Asia/Kolkata')
print(os.getcwd())

import os

# Replace 'file.txt' with the name of your file
file_name = '16-46-21-804193.jpg'

# Use the root directory as the starting point


# Walk through the directory tree starting from the root directory
for root, dirs, files in os.walk(web_img_path):
    if file_name in files:
        # If the file is found, print its full path
        file_path = os.path.join(root, file_name)
        print(f"File '{file_name}' found at '{file_path}'")
        break
else:
    # If the file is not found, print an error message
    print(f"File '{file_name}' not found in directory tree starting from '{web_img_path}'")

# Loop indefinitely
# while True:
#     for image_name in os.listdir(web_img_path):
#         print(image_name)
#         current_time = datetime.datetime.now(tz).strftime("%H-%M-%S-%f")
#         image_time = image_name.split('.')[0]
#         print("server time is: ", current_time)
#         if current_time >= image_time:
#             image_path = os.path.join(web_img_path, image_name)
#             print("deleted: " + image_time + ".jpg")
#             os.remove(image_path)
#     for image_name in os.listdir(api_img_path):
#         print(image_name)
#         current_time = datetime.datetime.now(tz).strftime("%H-%M-%S-%f")
#         image_time = image_name.split('.')[0]
#         print("server time is: ", current_time)
#         if current_time >= image_time:
#             image_path = os.path.join(api_img_path, image_name)
#             print("deleted: " + image_time + ".jpg")
#             os.remove(image_path)
#     time.sleep(60)
