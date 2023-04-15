from .mazetest import Maze
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ImageSerializer
from .models import ImageModel
from important_pts_tkmce.important_pts import important_points,avg_shift_px
import os
from inmap_cred.models import ApiAccounts
from django.utils import timezone
import cProfile
import io
import pstats
map_path = os.path.abspath('inmapapi/static/inmapapi/text_maps/map.txt')

@api_view([ 'POST'])
def index_api(request):
    # pr = cProfile.Profile()
    # pr.enable()
    From = request.GET.get('from', '')
    To = request.GET.get('to', '')
    api_cred = request.GET.get('api_cred', '')
    api_secret = request.GET.get('api_secret', '')
    if From and To and api_secret and api_cred:
        # Check if the API credentials are valid
        try:
            api_account = ApiAccounts.objects.get(api_cred=api_cred, api_secret=api_secret) 
            From_x, From_y = important_points[From]
            To_x, To_y = important_points[To]
        except ApiAccounts.DoesNotExist:
            return Response({'error': 'Invalid API credentials'})
        except KeyError:
            return Response({'error': 'Invalid "from" or "to" parameters'})
        today = timezone.now().date()
        last_usage_date = api_account.last_used_time.date()
        api_account.total_usage += 1
        if today == last_usage_date:
            api_account.usage_per_day += 1
        else:
            api_account.usage_per_day = 0
        api_account.save()
        print("saved the request in the database")
        m = Maze(map_path,From_y, From_x, To_y, To_x, "tkm_map.jpg")
        m.solve()
        distance, filename_timestamp = m.output_image()

        # Generate the image URL with base URL of your Django app
        base_url = request.build_absolute_uri('/')
        image_url = f"{base_url}static/inmapapi/temp_images/{filename_timestamp}"
        print("generated image of url: ",image_url)
        # Calculate the distance
        distance = round(distance * avg_shift_px)
        # Save the model instance to the database
        image_model = ImageModel(from_field=From, to_field=To, image_url=image_url, distance=distance)
        image_model.save()
        # Serialize the model instance and return the response
        serializer = ImageSerializer(image_model)
        # pr.disable()
        # s = io.StringIO()
        # sortby = 'cumulative'
        # ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        # ps.print_stats()
        # print(s.getvalue())
        return Response(serializer.data)
        
    elif not From or not To and api_secret and api_cred:
        return Response({'error': 'Please provide the "from" and "to" parameters'})
    elif not api_secret or not api_cred:
        return Response({'error': 'Please provide the "api_cred" and "api_secret" parameters'})
    else:
        return Response({'error': 'Please provide the "from", "to", "api_cred" and "api_secret" parameters'})

