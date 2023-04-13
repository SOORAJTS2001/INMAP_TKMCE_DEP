import os
import datetime,time
images_path = 'inmapapp/static/inmapapp/temp_images/'
while True:
    for image_name in os.listdir(images_path):
        current_time = datetime.datetime.now().strftime("%H-%M")
        image_time = image_name.split('.')[0]
        print(current_time, image_time)
        if current_time >= image_time:
            image_path = os.path.join(images_path, image_name)
            print("deleted: " + image_time+".jpg")
            print("waiting for 5 minutes")
            os.remove(image_path)
            time.sleep(300)
