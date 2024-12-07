"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

# from crypt import methods
import site 

from app import app, Config,  mongo, Mqtt
from flask import escape, render_template, request, jsonify, send_file, redirect, make_response, send_from_directory 
from json import dumps, loads 
from werkzeug.utils import secure_filename
from datetime import datetime,timedelta, timezone
from os import getcwd
from os.path import join, exists
from time import time, ctime
from math import floor
 



#####################################
#   Routing for your application    #
#####################################

@app.route('/api/numberfrequency', methods=['GET']) 
def get_numberFrequency():   
    '''Returns list of frequency'''
    
    if request.method == "GET":
        try:
            frequency = mongo.numberFrequency()
            if frequency:
                return jsonify({"status":"found","data": frequency})
            
        except Exception as e:
            print(f"get_numberFrequency error: f{str(e)}")        
    return jsonify({"status":"failed","data":[]})
   

@app.route('/api/oncount/<ledName>', methods=['GET']) 
def get_onCount(ledName):   
    '''Returns number which represents the amount of time a specific LED was turned on'''
    if request.method == "GET":
        try:
            LED_Name = escape(ledName)
            count = mongo.onCount(LED_Name)
            if count:
                return jsonify({"status":"found","data": count})
            
        except Exception as e:
            print(f"get_onCount error: f{str(e)}")        
    return jsonify({"status":"failed","data": 0})


@app.route('/api/oncount', methods=['POST']) 
def get_onCountPost():   
    '''Returns number which represents the amount of time a specific LED was turned on'''
    if request.method == "POST":
        try:
            form =  request.form

            LED_Name = escape(form.get("LED_Name"))
            count = mongo.onCount(LED_Name)
            if count:
                return jsonify({"status":"found","data": count})
            
        except Exception as e:
            print(f"get_onCountPost error: f{str(e)}")        
    return jsonify({"status":"failed","data": 0})
   

@app.route('/api/file/get/<filename>', methods=['GET']) 
def get_images(filename):   
    '''Returns requested file from uploads folder'''
   
    if request.method == "GET":
        directory   = join( getcwd(), Config.UPLOADS_FOLDER) 
        filePath    = join( getcwd(), Config.UPLOADS_FOLDER, filename) 

        # RETURN FILE IF IT EXISTS IN FOLDER
        if exists(filePath):        
            return send_from_directory(directory, filename)
        
        # FILE DOES NOT EXIST
        return jsonify({"status":"file not found"}), 404


@app.route('/api/file/upload',methods=["POST"])  
def upload():
    '''Saves a file to the uploads folder'''
    
    if request.method == "POST": 
        file     = request.files['file']
        filename = secure_filename(file.filename)
        file.save(join(getcwd(),Config.UPLOADS_FOLDER , filename))
        return jsonify({"status":"File upload successful", "filename":f"{filename}" })

 


###############################################################
# The functions below should be applicable to all Flask apps. #
###############################################################


@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)

@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response

@app.errorhandler(405)
def page_not_found(error):
    """Custom 404 page."""    
    return jsonify({"status": 404}), 404



