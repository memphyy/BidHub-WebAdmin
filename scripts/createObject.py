import json,httplib,cgi

formData = cgi.fieldStorage()

if "itemName" not in formData or "itemDesc" not in formData or "itemDonorName" not in formData or "itemPrice" not in formData:
	print "<h1>Error</h1>"
	print "Please fill out all the fields!"
	return
	

print "<p>name:", formData['itemName'].value, "</p>"
print "<p>desc:", formData['itemDesc'].value, "</p>"
print "<p>donor:", formData['itemDonorName'].value, "</p>"
print "<p>startPrice:", formData['itemPrice'].value, "</p>"
print "<p>imgurl:", formData['itemImgURL'].value, "</p>"


desc = formData.getvalue('itemDesc')
donor = formData.getvalue('itemDonorName')
imgurl = formData.getvalue('itemImgURL')
name = formData.getvalue('itemName')
startPrice = formData.getvalue('itemPrice')


connection = httplib.HTTPSConnection('api.parse.com', 443)
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
results = json.loads(connection.getresponse().read())
print results