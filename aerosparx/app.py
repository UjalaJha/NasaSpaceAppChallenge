from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import os # to use operating system dependent functionality
import matplotlib.pyplot as plt # to generate the visualizations
import math
from flask import request
import requests
import json
from glob import glob

import matplotlib.pyplot as plt
from matplotlib import patches as mpatches
from matplotlib.colors import ListedColormap
from matplotlib import colors
import matplotlib as mpl
import seaborn as sns

import rasterio as rio
from rasterio.plot import plotting_extent, show
from rasterio.plot import reshape_as_raster, reshape_as_image

import geopandas as gpd
from shapely.geometry import mapping, box

import earthpy as et
import earthpy.spatial as es
import earthpy.plot as ep

import flask
from flask_ngrok import run_with_ngrok
from flask import Flask
from flask_restful import Resource, Api
import json

from matplotlib.colors import colorConverter



sns.set_style('white')
sns.set(font_scale=1.5)

app = Flask(__name__)
#app.config['UPLOAD_FOLDER']='C://Users//juyee//Envs//sih2020//Audio//resume'

@app.route('/plots/before_flood', methods=['GET'])
def plot_before_flood(pre_bytes_obj):
    return send_file(pre_bytes_obj,
                     attachment_filename='plot.png',
                     mimetype='image/png')

@app.route('/plots/after_flood', methods=['GET'])
def plot_after_flood(post_bytes_obj):
    return send_file(post_bytes_obj,
                     attachment_filename='plot.png',
                     mimetype='image/png')


def plot_colormap(dnbr_sentinel_class,location):
    dnbr_cat_names = ["Enhanced Regrowth",
                        "Unburned",
                        "Low Severity",
                        "Moderate Severity",
                        "High Severity"]

    nbr_colors = ["g", "yellowgreen", "peachpuff", "coral", "maroon"]

    nbr_cmap = ListedColormap(nbr_colors)

    # Plot the data with a custom legend
    fig, ax = plt.subplots(figsize=(10, 10))
    im = ax.imshow(dnbr_sentinel_class.reshape(dnbr_sentinel_class.shape[:2]), cmap=nbr_cmap)

    ax.set_title("Sentinel dNBR",
                fontsize=16)

    cbar = ep.colorbar(im)

    cbar.set_ticks(np.unique(dnbr_sentinel_class))
    cbar.set_ticklabels(dnbr_cat_names)

    # Turn off ticks
    ax.set_axis_off()
    path = 'static/img/fireresult/fire_plot_' + location + '.png'
    plt.savefig(path)
    #return plt.show()


def plot_algae_bloom(cha_sentinel_class,location):
    cha_cat_names = ["Pure",
                  "Light Concentration",
                  "Low Concentration",
                  "Moderate Concentration",
                  "High Concentration"]

    nbr_colors = ["g", "yellowgreen", "peachpuff", "coral", "maroon"]

    nbr_cmap = ListedColormap(nbr_colors)

    # Plot the data with a custom legend
    fig, ax = plt.subplots(figsize=(30, 20))
    im = ax.imshow(cha_sentinel_class.reshape(cha_sentinel_class.shape[1:3]), cmap=nbr_cmap)

    ax.set_title("chlorophyll a",
                fontsize=16)

    cbar = ep.colorbar(im)

    cbar.set_ticks(np.unique(cha_sentinel_class))
    cbar.set_ticklabels(cha_cat_names)

    # Turn off ticks
    ax.set_axis_off()
    #plt.show()
    path = 'static/img/algaeresult/algae_plot_' + location + '.png'
    plt.savefig(path)

@app.route('/')
def home():
    return render_template('index.html')



@app.route('/disaster/phenomenon=<string:phenomenon>',methods=['GET'])
def disaster_selection(phenomenon):
    if(phenomenon=="flood"):
        return render_template('flood.html')
    
    elif(phenomenon=="fire"):
        return render_template('fire.html')

    elif(phenomenon=="algae"):
        return render_template('algae.html')
    



@app.route('/disaster/phenomenon=<string:phenomenon>&location=<string:location>',methods=['GET'])
def get_result(phenomenon,location):
    if(phenomenon=="fire"):
        if(location=="australia"):
            r = requests.get('http://be0458a9c0db.ngrok.io/classify/australia_2019')
            print(r)
            if r.status_code == 200:
                data = r.json()
                final_data = json.loads(data)
                dnbr_sentinel_class = np.asarray(final_data[0])
                affected_areas = final_data[1]
                plot_colormap(dnbr_sentinel_class,location)
                return render_template('fire_result.html',affected_areas=affected_areas,location=location)
            else:
                print("Bad request")
                return render_template('500.html')
        elif(location=="empedrado"):
            r = requests.get('http://be0458a9c0db.ngrok.io/classify/empedrado_2016_2017')
            print(r)
            if r.status_code == 200:
                data = r.json()
                final_data = json.loads(data)
                dnbr_sentinel_class = np.asarray(final_data[0])
                affected_areas = final_data[1]
                plot_colormap(dnbr_sentinel_class,location)
                return render_template('fire_result.html',affected_areas=affected_areas,location=location)
            else:
                print("Bad request")
                return render_template('500.html')

    elif(phenomenon=='flood'):
        if(location=="kerala"):
            #r = requests.get('http://01dbfe5c87a8.ngrok.io/classify/kerala_2018')
            #print(r)
            # print(type(r.text))
            #if r.status_code == 200:
                # data = r.json()
                # #data = r.content.partition('(')[-1].rpartition(')')[0]
                # final_data = json.loads(data)
                # pre_bytes_obj = final_data[0]
                # post_bytes_obj = final_data[1]

                # plot_before_flood(pre_bytes_obj)
                # plot_after_flood(post_bytes_obj)
                # ndwi = final_data[0]
                # ndwi_af = final_data[1]
                # resulted_mask = final_data[2]
                # plot_after_flood(ndwi,ndwi_af,resulted_mask)
                # plot_before_flood(ndwi,ndwi_af,resulted_mask)
            return render_template('flood_result.html',location=location)
            # else:
            #     print("Bad request")
            #     return render_template('500.html')
        
        elif(location=="bihar"):
            
            return render_template('flood_result.html',location=location)
        
            


    elif(phenomenon=="algae"):
        if(location=="harsha"):
            r = requests.get('http://14a33bd9d7b5.ngrok.io/classify/harsha_lake')
            print(r)
            if r.status_code == 200:
                data = r.json()
                cha_sentinel_class = json.loads(data)
                cha_sentinel_class = np.array(cha_sentinel_class)
                plot_algae_bloom(cha_sentinel_class,location)
                return render_template('algae_result.html',location=location)
        
            else:
                print("Bad request")
                return render_template('500.html')
        elif(location=="powai"):
            r = requests.get('http://c6ffbe4b6888.ngrok.io/classify/powai_lake')
            print(r)
            if r.status_code == 200:
                data = r.json()
                cha_sentinel_class = json.loads(data)
                cha_sentinel_class = np.array(cha_sentinel_class)
                plot_algae_bloom(cha_sentinel_class,location)
                return render_template('algae_result.html',location=location)
        
            else:
                print("Bad request")
                return render_template('500.html')

# @app.route('/voice_predict',methods=['POST'])
# def voice_ocean():
  
#   return render_template('upload.html',  prediction_text='Your Personality: {}'.format(value))
	

if __name__ == "__main__":
    app.run(debug=True)