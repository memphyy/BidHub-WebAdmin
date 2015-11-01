#!/usr/bin/env python3

import cgi,cgitb,createObject
cgitb.enable()

print("Content-Type: text/html")
print()
print("""
    <TITLE>CGI script ! Python</TITLE>
    <H1>This is my first CGI script</H1>
    Hello, world!
""")

formData = cgi.fieldStorage()

if "itemName" not in formData or "itemDesc" not in formData or "itemDonorName" not in formData or "itemPrice" not in formData:
	print("<h3>Error</h3>")
	print("Please fill out all the fields!")

print("<p>name:", formData['itemName'].value, "</p>")
print("<p>desc:", formData['itemDesc'].value, "</p>")
print("<p>donor:", formData['itemDonorName'].value, "</p>")
print("<p>startPrice:", formData['itemPrice'].value, "</p>")
print("<p>imgurl:", formData['itemImgURL'].value, "</p>")

desc = formData.getvalue('itemDesc')
donor = formData.getvalue('itemDonorName')
imgurl = formData.getvalue('itemImgURL')
name = formData.getvalue('itemName')
startPrice = formData.getvalue('itemPrice')

print("<p>", createObject(name,desc,donor,startPrice,imgurl), "</p>")