#!/usr/bin/env python3

import cgi,cgitb,createObject
cgitb.enable()

print("Content-Type: text/html")
print()
print("""
    <TITLE>Add Item</TITLE>
    <H1>Add Item</H1>
""")


formData = cgi.FieldStorage()

if "itemName" not in formData or "itemDesc" not in formData or "itemDonorName" not in formData or "itemPrice" not in formData:
	print("<h3>Error</h3>")
	print("Please fill out all the fields!")

	
desc = formData['itemDesc'].value
donor = formData['itemDonorName'].value
imgurl = formData['itemImgURL'].value
name = formData['itemName'].value
startPrice = formData['itemPrice'].value

print("<p>name:", name, "</p>")
print("<p>desc:", desc, "</p>")
print("<p>donor:", donor, "</p>")
print("<p>startPrice:", startPrice, "</p>")
print("<p>imgurl:", imgurl, "</p>")


createObject(name,desc,donor,startPrice,imgurl)