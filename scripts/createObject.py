import json,http.client

def create(name,desc,donor,startPrice,imgurl):
	connection = http.client.HTTPSConnection('api.parse.com', 443)
	connection.connect()
	connection.request('POST', '/1/classes/Item', json.dumps({
			"description": desc,
			"donorname": donor,
			"imageurl": imgurl,
			"name": name,
			"price": startPrice,
			"priceIncrement": 2.5,
			"qty": "1"
		 }), {
		   "X-Parse-Application-Id": "WhkQetI8nb0HrIykoaNc8LJ9flHIxOvgaXhFXFxm",
		   "X-Parse-REST-API-Key": "G02koccgg9q6RzqwRmpiQDx3QllASet5iW2XbLob",
		   "Content-Type": "application/json"
		 })
	#results = json.loads(connection.getresponse().read())
	#return results