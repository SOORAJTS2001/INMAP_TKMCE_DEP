# if the given points are not plotted we could use these points to plot the points
# for our example it is not used
important_points={"open_auditorium":(164,515),"college_gym":(154,491),"squash_corner":(246,436),"apj_park":(252,535),"badminton_court":(347,450),"basketball_court":(379,441),"main_entrance":(287,522),"central_portico":(427,530),"machines_lab":(575,524),"ladies_toilet":(596,443),"mens_toilet":(612,463),"arch_block":(565,423),"electrical_lab":(616,412),"mechanical_block":(667,504),"coffee_corner":(661,529),"chemical_block":(761,501),"annex_hostel":(797,516),"kilivathil":(760,534),"workshop_block":(425,348),"campus_doctor":(443,359),"college_store":(445,358),"canteen":(475,363),"college_ground":(497,330),"library":(345,367),"parking":(353,414)}
important_tuple = important_points.values()
important_list = []
for i in important_tuple:
# the points used here uses the enlarged points from the image that's why there is a reductions happening
    important_list.append((round(i[0]/7.092),round(i[1]/7.07)))
f = open("mapped_tkmce.txt", "r+")
row_no,col_no =0,0
new_map = ""
for rows in f:
  row_no+=1
  for cols in rows:
    col_no+=1
    if (col_no,row_no) in important_list:
        new_map+="*"
        print("corrections done")
    else:
        new_map+=cols
  print(col_no,row_no)
  col_no =0
  

with open('mod.txt', 'w') as f:
    f.write(new_map)



