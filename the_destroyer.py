import os
import datetime
import time
import pytz
from important_pts_tkmce.important_pts import web_img_path,api_img_path


# Set the time zone to Asia/Kolkata
tz = pytz.timezone('Asia/Kolkata')
print(os.getcwd())
# Loop indefinitely
while True:
    for image_name in os.listdir(web_img_path):
        print(image_name)
        current_time = datetime.datetime.now(tz).strftime("%H-%M-%S-%f")
        image_time = image_name.split('.')[0]
        print("server time is: ", current_time)
        if current_time >= image_time:
            image_path = os.path.join(web_img_path, image_name)
            print("deleted: " + image_time + ".jpg")
            os.remove(image_path)
    for image_name in os.listdir(api_img_path):
        print(image_name)
        current_time = datetime.datetime.now(tz).strftime("%H-%M-%S-%f")
        image_time = image_name.split('.')[0]
        print("server time is: ", current_time)
        if current_time >= image_time:
            image_path = os.path.join(api_img_path, image_name)
            print("deleted: " + image_time + ".jpg")
            os.remove(image_path)
    time.sleep(60)
