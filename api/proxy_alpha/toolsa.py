import json
from urllib.parse import parse_qs
from django.db.models import Max

post_endpoint_message = 'This is a POST API End Point'

# Generate Next Id for the Model
def next_id(Model):
	no = Model.objects.all().aggregate(Max('id'))

	max_id = no['id__max']

	if max_id == None:
		return 1
	else:
		return int(max_id) + 1


# Parse Data for Other Methods from Front End Pals
def parse_data(request):
	body_data = {}

	try:
		body_data = json.loads(request.body.decode('utf-8'))
	except Exception:
    	# RawPostDataException
		body_data = json.loads(json.dumps(request.data))
	
	if len(body_data) < 1:
		body_data_a = parse_qs(request.get_full_path().split('?')[1])
		body_data_dict = json.dumps(dict(body_data_a)) 
		body_data = json.loads(body_data_dict)
		
	return body_data