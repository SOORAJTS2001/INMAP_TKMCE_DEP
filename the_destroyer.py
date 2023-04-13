import os
import datetime
import time
import pytz

images_path = os.path.abspath('staticfiles/inmapapp/temp_images')

# Set the time zone to Asia/Kolkata
tz = pytz.timezone('Asia/Kolkata')

# Loop indefinitely
while True:
    for image_name in os.listdir(images_path):
        print(image_name)
        current_time = datetime.datetime.now(tz).strftime("%H-%M")
        image_time = image_name.split('.')[0]
        print("server time is: ", current_time)
        if current_time >= image_time:
            image_path = os.path.join(images_path, image_name)
            print("deleted: " + image_time + ".jpg")
            os.remove(image_path)
    time.sleep(60)
