import os
import datetime
import time
import pytz
from important_pts_tkmce.important_pts import web_img_path,api_img_path,main_url,test_url
import requests
from termcolor import colored
# Set the time zone to Asia/Kolkata
tz = pytz.timezone('Asia/Kolkata')
print(os.getcwd())

import os

# # Replace 'file.txt' with the name of your file
# file_name = '16-46-21-804193.jpg'

# # Use the root directory as the starting point


# # Walk through the directory tree starting from the root directory
# while True:
#     for root, dirs, files in os.walk(web_img_path):
#         print(root,dirs,files)
#     time.sleep(60)


# Loop indefinitely
while True:
    print(colored("worker :sending the message to delete the unused images", 'blue', attrs=['bold']))
    response = requests.post(f'{main_url}inmap-admin/delete-images/',{'secret_key':'sooraj123*'})
    print("worker :sended the command and returned with a status code",response.json)
    print(colored("worker :going to sleep for 3 minutes", 'blue', attrs=['bold']))
    time.sleep(180)


