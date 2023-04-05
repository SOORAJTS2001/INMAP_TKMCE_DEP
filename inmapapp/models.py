from django.db import models

# Create your models here.
# it is in the format of key value
ROOM_CHOICES = (
    ('open_auditorium','open_auditorium'),
('college_gym','college_gym'),
('squash_corner','squash_corner'),
('apj_park','apj_park'),
('main_gate','main_gate'),
('main_entrance','main_entrance'),
('central_portico','central_portico'),
('machines_lab','machines_lab'),
('ladies_toilet','ladies_toilet'),
('arch_block','arch_block'),
('auditorium','auditorium'),
('basketball_court','basketball_court'),
('parking_gate','parking_gate'),
('library','library'),
('mech_workshop','mech_workshop'),
('campus_doctor','campus_doctor'),
('cooperative_store','cooperative_store'),
('canteen','canteen'),
('college_ground','college_ground'),
('electrical_lab','electrical_lab'),
('mech_block','mech_block'),
('chem_block','chem_block'),
('coffee_corner','coffee_corner'),
('kilivathil','kilivathil'),
('annex_hostel','annex_hostel'),
)

class MyModel(models.Model):
  From = models.CharField(max_length=600, choices=ROOM_CHOICES, default='Hall')
  To = models.CharField(max_length=600, choices=ROOM_CHOICES, default='Hall')