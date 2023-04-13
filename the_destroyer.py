import os
import datetime,time
directory = os.getcwd() 
images_path = os.path.abspath(f'inmapapp/static/inmapapp/temp_images/')
# print(images_path)
# Create the directory if it does not exist
while True:
    for image_name in os.listdir(images_path):
        print(image_name)
        current_time = datetime.datetime.now().strftime("%H-%M")
        image_time = image_name.split('.')[0]
        # print(current_time, image_time)
        if current_time >= image_time:
            image_path = os.path.join(images_path, image_name)
            print("deleted: " + image_time+".jpg")
            # print("waiting for 5 minutes")
            os.remove(image_path)
    time.sleep(60)
