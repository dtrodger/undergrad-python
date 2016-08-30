#! /usr/bin/env python

print 'Content-type: text/html\n'

import cgi

html = """
<html>
    <head><title>BMI Results</title></head>
    <body>
        <p>Your weight is {html_weight} lbs.</p>
        <p>Your height is {html_heightf} feet {html_heighti} inches.</p>
        <p>Your BMI is {result}</p>
        <p>BMI Category: {category}<p>
        <!--easter egg! -->
        <p>{arnold}</p>
    </body>
</html>
"""
error_html = """
<html>
    <head><title>ERROR</title></head>
    <body>
        <h1>ERROR</h1>
    </body>
</html>"""

form = cgi.FieldStorage()

error = 0

while True:
    try:
        weight = float(form.getfirst('weight',''))
    except:
        error = 1
        break
    try:
        heightf = float(form.getfirst('heightfeet',''))
    except:
        error = 1
        break
    try:
        heighti = float(form.getfirst('heightinch',''))
    except:
        error = 1
        break
    break

if error == 0:
    arnold_img = ''
    height_inches = (heightf*12) + heighti
    bmi = round((weight * 703) / (height_inches * height_inches),3)
    if bmi < 15:
        bmi_category = 'Very severely underweight'
    elif bmi <= 16:
        bmi_category = 'Severely underweight'
    elif bmi <= 18.5:
        bmi_category = 'Underweight'
    elif bmi <= 25:
        bmi_category = 'Normal'
        arnold_img = '<img src="http://www.askthetrainer.com/\
wp-content/uploads/2011/12/arnold-schwarzenegger-featured-image.jpg"><br>Arnold is happy.'
    elif bmi <= 30:
        bmi_category = 'Overweight'
    elif bmi <= 35:
        bmi_category = 'Obese Class I (Moderately obese)'
    elif bmi <= 40:
        bmi_category = 'Obese Class II (Severely obese)'
    else:
        bmi_category = 'Obese Class II (Very severely obese)'
        

    print html.format(html_weight = weight, html_heightf = heightf,\
                  html_heighti = heighti, result = bmi, category = bmi_category,\
                      arnold = arnold_img)
else:
    print error_html

        
