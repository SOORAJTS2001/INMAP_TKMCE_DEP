from django.shortcuts import render, redirect
from .mazetest import Maze
from .solutiondata import sols
import time
import os
import json

# floor1checkpoint = {"kitchen":(138, 23), "bedroom1":(48, 24), "emptyroom":(59, 41), "bath":(31, 44), "stairentry":(106, 45), "bath2":(58, 50), "room":(188, 50),"stairexit":(106, 53),"familyroom":(63, 67), "formaldining":(100, 68),"office":(139, 71), "exit":(79, 76)}
# floor2checkpoint = {"bedroom1":(56,24), "familyroom":(119, 37), "bath":(32, 45), "stairentry":(143, 45), "emptyroom":(73, 51),"stairexit":(142, 51), "bedroom3":(146, 62),"bedroom2":(74, 63),"Bathroom":(107, 72)}

# locations={'Hall':(55,86),'Bedroom 1':(26,36),'Bedroom 2':(67,35),'Bedroom 3':(78,94),'Bedroom 4':(57,171),'Sitting Area':(14,112),'Balcony':(15,140),'Master Bath':(27,151),'Master Bedroom':(26,98),'Bath':(54,27),'W.I.C':(34,133)}
# # this is for the first floor
# floor1checkpoint = {"kitchen-1st floor":(138, 23), "bedroom1-1st floor":(48, 24), "empty-1st floor":(59, 41), "bath-1st floor":(31, 44), "stairentry-1st floor":(106, 45), "bath2-1st floor":(58, 50), "room-1st floor":(188, 50),"stairexit-1st floor":(106, 53),"familyroom-1st floor":(63, 67), "formaldinnning-1st floor":(100, 68),"office-1st floor":(139, 71), "exit-1st floor":(79, 76)}
# # this is for the second floor
# floor2checkpoint = {"bedroom1-2nd floor":(56,24), "familyroom-2nd floor":(119, 37), "bath-2nd floor":(32, 45), "stairentry-2nd floor":(143, 45), "empty-2nd floor":(73, 51),"stairexit-2nd floor":(142, 51), "bedroom3-2nd floor":(146, 62),"bedroom2-2nd floor":(74, 63),"bathroom-2nd floor":(107, 72)}
# floor1 = False
# floor2 = False
# Create your views here.
# important_points={"open_auditorium":(164,515),"college_gym":(154,491),"squash_corner":(246,436),"apj_park":(252,535),"badminton_court":(347,450),"basketball_court":(379,441),"main_entrance":(287,522),"central_portico":(427,530),"machines_lab":(575,524),"ladies_toilet":(596,443),"mens_toilet":(612,463),"arch_block":(565,423),"electrical_lab":(616,412),"mechanical_block":(667,504),"coffee_corner":(661,529),"chemical_block":(761,501),"annex_hostel":(797,516),"kilivathil":(760,534),"workshop_block":(425,348),"campus_doctor":(443,359),"college_store":(445,358),"canteen":(475,363),"college_ground":(497,330),"library":(345,367),"parking":(353,414)}
important_points = {"main_entrance":(77,54),"open_auditorium": (75, 35), "open_gymnasium": (72, 34), "open_tenniscourt": (69, 34), "open_volleycourt": (70, 47), "apj_park": (77, 51), "parking_front": (71, 55), "squash_court": (63, 51), "parking_back": (58, 74), "badminton_court": (62, 71), "basketball_court": (62, 77), "backgate": (53, 80), "library": (52, 70), "canteen": (
    56, 99), "stores": (51, 91), "workshop_block": (50, 91), "college_ground": (47, 99), "prayer_hall": (55, 92), "auditorium": (66, 92), "arch_block": (56, 113), "ladies_washroom": (63, 121), "gents_washroom": (66, 124), "coffee_corner": (74, 130), "mech_block": (72, 133), "chem_block": (72, 153), "annex_hostel": (73, 159), "kilivathil": (77, 152)}
# important_points = {"open_auditorium":(193,338),"college_gym":(186,323),"squash_corner":(246,288),"apj_park":(250,353),"main_gate":(265,357),"main_entrance":(273,343),"central_portico":(366,350),"machines_lab":(464,345),"ladies_toilet":(476,293),"arch_block":(456,279),"auditorium":(400,283),"basketball_court":(334,291),"parking_gate":(318,273),"library":(312,241),"mech_workshop":(365,229),"campus_doctor":(376,236),"cooperative_store":(384,235),"canteen":(398,239),"college_ground":(412,217),"electrical_lab":(489,270),"mech_block":(523,331),"chem_block":(585,331),"coffee_corner":(520,347),"kilivathil":(585,353),"annex_hostel":(609,339)}
avg_length = 370/578
avg_breadth = 170/254
apparent_shift = ((465/100)+(826/200))/2
avg_shift_px = ((avg_length+avg_breadth)/2)*apparent_shift

def index(request):
    global solutions
    if request.method == "GET":
        return render(request, 'inmapapp/index.html', {"points": important_points, 'image': "inmapapp/tkm_map_normal.jpg", 'time': '', 'update': False})
    elif (request.method == "POST"):
        then = time.time()
        FromAuto = request.POST.get('fromLocation')
        ToAuto = request.POST.get('To')
        FromMan = request.POST.get('manualFrom')
        ToMan = request.POST.get('manualTo')
        if FromAuto and ToAuto:
            From = FromAuto
            To = ToAuto
        else:
            From = FromMan
            To = ToMan
        From_x, From_y = important_points[From]
        To_x, To_y = important_points[To]
        # From_x = round(From_x/5.10625)
        # From_y = round(From_y/4.7)
        # To_x = round(To_x/5.10625)
        # To_y = round(To_y/4.7)

        print(From_x, From_y, To_x, To_y)
        m = Maze(os.path.abspath('inmapapp/static/inmapapp/map.txt'),
                 From_y, From_x, To_y, To_x, "tkm_map.jpg")
        m.solve()
        m.output_image()
        solution_meters = round(m.output_image()*avg_shift_px)
        solution_time = round(solution_meters*1.2)
        solution_feet = round(solution_meters*1.3)
        
        # solutions = m.output_image()
        # # floor1 = True
        # # floor2 = False
        # ans=""
        # for sol in solutions[1]:
        #     ans+=f'''<span class="animationEl" style="width:10px;height:10px;position: absolute;top: {sol[0]*5.35}px;left: {sol[1]*4.78}px;"> </span>'''
        # # return render(request,'inmapapp/sample.html',{"data":ans})
        # # return render(request,'inmapapp/result.html',{'floor1':floor1,'floor2':floor2,'time':time.time()-then,"data":ans,'update':True})

        now = time.time()
        return render(request, 'inmapapp/result.html', {"image": "inmapapp/static/inmapapp/modtkm_map.jpg", "time": now-then, "update": True,"solution_meters":solution_meters,"solution_time":solution_time,"solution_feet":solution_feet,"time":round(now-then,2)})
        # print(From_x,From_y,To_x,To_y)

        # /home/sooraj/Documents/PROJECTS/INMAPWEB/inmapproject/inmapapp/static/inmapapp/map.txt
        # '/home/sooraj/Documents/PROJECTS/INMAPWEB/inmapproject/static/inmapapp/map.txt'
        # print("Maze:")
        # # m.print()
        # print("Solving...")
        # m.solve()
        # # print("States Explored:", m.num_explored)
        # # print("Solution:")
        # m.print()
        # m.output_image()


