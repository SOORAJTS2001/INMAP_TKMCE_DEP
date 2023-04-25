import qrcode
from PIL import Image, ImageDraw, ImageFont

# Generate the QR code
# floor1checkpoint = {"kitchen-1st-floor":(138, 23), "bedroom1-1st-floor":(48, 24), "empty-1st-floor":(59, 41), "bath-1st-floor":(31, 44), "stairentry-1st-floor":(106, 45), "bath2-1st-floor":(58, 50), "room-1st-floor":(188, 50),"stairexit-1st-floor":(106, 53),"familyroom-1st-floor":(63, 67), "formaldinnning-1st-floor":(100, 68),"office-1st-floor":(139, 71), "exit-1st-floor":(79, 76)}
# floor2checkpoint = {"bedroom1-2nd-floor":(56,24), "familyroom-2nd-floor":(119, 37), "bath-2nd-floor":(32, 45), "stairentry-2nd-floor":(143, 45), "empty-2nd-floor":(73, 51),"stairexit-2nd-floor":(142, 51), "bedroom3-2nd-floor":(146, 62),"bedroom2-2nd-floor":(74, 63),"bathroom-2nd-floor":(107, 72)}
# floor_lists = list(floor1checkpoint.keys())
important_points = {"main_entrance":(77,54),"open_auditorium": (75, 35), "open_gymnasium": (72, 34), "open_tenniscourt": (69, 34), "open_volleycourt": (70, 47), "apj_park": (77, 51), "parking_front": (71, 55), "squash_court": (63, 51), "parking_back": (58, 74), "badminton_court": (62, 71), "basketball_court": (62, 77), "backgate": (53, 80), "library": (52, 70), "canteen": (
    56, 99), "stores": (51, 91), "workshop_block": (50, 91), "college_ground": (47, 99), "prayer_hall": (55, 92), "auditorium": (66, 92), "arch_block": (56, 113), "ladies_washroom": (63, 121), "gents_washroom": (66, 124), "coffee_corner": (74, 130), "mech_block": (72, 133), "chem_block": (72, 153), "annex_hostel": (73, 158), "kilivathil": (77, 152)}
main_url = 'https://inmapapp.herokuapp.com/'
test_url = 'http://127.0.0.1:8000/'
important_pts = list(important_points.keys())
for floors in important_points:
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(f'{main_url}?from_position={floors}')
    qr.make(fit=True)
    img = qr.make_image(fill_color='black', back_color='white')

    # Add text to the image
    draw = ImageDraw.Draw(img)
    text = "prodn-"+floors
    font = ImageFont.truetype('arial.ttf', 10)
    font_large = ImageFont.truetype('arial.ttf', 20)
    textwidth, textheight = draw.textsize(text, font)
    x = (img.size[0] - textwidth) / 2
    y = img.size[1] - textheight - 10
    draw.text((x, y), text, font=font)
    draw.text((x, y+10), 'TinkerHub TKMCE', font=font)

    # Save the image
    img.save(f'{floors}.png')
