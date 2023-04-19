# test = "#############################        ###    ### **"
# cnt = 0
# for elem in test:
#     if elem!="*":cnt+=1
# print(cnt)
# import cv2 as cv,os
# base_img = cv.imread(os.path.abspath(f'inmapapp/static/inmapapp/floor2.png'))    
# base_img = cv.resize(base_img, (826, 465))
# cv.imwrite(os.path.abspath(f'inmapapp/static/inmapapp/modfloor2.png'),base_img)
# important_points = {"open_auditorium":(193,338),"college_gym":(186,323),"squash_corner":(246,288),"apj_park":(250,353),"main_gate":(265,357),"main_entrance":(273,343),"central_portico":(366,350),"machines_lab":(464,345),"ladies_toilet":(476,293),"arch_block":(456,279),"auditorium":(400,283),"basketball_court":(334,291),"parking_gate":(318,273),"library":(312,241),"mech_workshop":(365,229),"campus_doctor":(376,236),"cooperative_store":(384,235),"canteen":(398,239),"college_ground":(412,217),"electrical_lab":(489,270),"mech_block":(523,331),"chem_block":(585,331),"coffee_corner":(520,347),"kilivathil":(585,353),"annex_hostel":(609,339)}
# for keys in important_points:
#     print("("+"'"+keys+"'"+","+"'"+keys+"'"+"),")
# get the current time
# import datetime
# now = datetime.datetime.now()
# # add five minutes to the current time
# five_minutes_later = now + datetime.timedelta(minutes=5)
# # format the time as a string with only the hour and minutes
# filename_timestamp = five_minutes_later.strftime("%H-%M")
# print(filename_timestamp)
from important_pts_tkmce.important_pts import important_points
print(list(important_points.keys()))