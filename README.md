![License](https://img.shields.io/github/license/UjalaJha/NasaSpaceAppChallenge) ![Version](https://img.shields.io/badge/Version-1.0.0-Blue) 
![Satellite](https://img.shields.io/badge/Satellite-Sentinel--2-yellow) ![Python](https://img.shields.io/badge/Python-3.x-success) ![Flask](https://img.shields.io/badge/App-Flask-yellow) ![Eartpy](https://img.shields.io/badge/Analytics-EarthPy-red)

# Automated Detection of Hazards
Natural phenomena like flood, fire, and algae blooms are threats to the ecosystems and hamper the chain of the life cycle, making its timely detection and categorization an important factor for mitigation and recovery. Our aim with this effort is to detect and characterize the mentioned hazards, by which researchers and decision-makers can better understand their impacts and scope. We have carried out case studies associated with these phenomena and used satellite imagery and machine learning approaches to classify threshold values that define the boundary between flooded and non-flooded, severity fire, algae bloom classes quickly and accurately. This well-formed approach can reduce the time spent and help to provide accurate maps quickly what is crucial when disaster happens.

*All the bands Mentioned below is of SENTINEL 2 Satellite Imagery Bands Launched by Europe Space Agency.*

# Flood
- Initially, we have used the Green Band (B3), Near Infrared (NIR) Band (B8) of the data, before and after flood satellite images gathered using Sentinel-2 to calculate the **Normalized Difference Water Index (NDWI)** which differentiates the water body and dry land from satellite images.
- Then we have generated ground truth for the satellite images using the NDWI of pre-flood and post-flood.
- Using the ground truth generated from the NDWI, we have developed the machine learning model to classify the flood area and non-flood area.
- Fine-tuning of the developed machine learning model is done using the grid search method.
![Image of Flood Detection](https://github.com/UjalaJha/NasaSpaceAppChallenge/blob/master/Images/flood.PNG)


# Fire
- We have used the Near Infrared (NIR) Band (B8A) and the Shortwave Infrared (SWIR) Band (B12) from Sentinel-2 satellite imagery, both pre-fire and post-fire for calculating the **Difference Normalized Burn Ratio (DNBR)**.
- The basis of this approach is the fact that natural vegetation affected by fires reflect characteristically in the above mentioned bands of the spectrum.
- The DNBR is then used to categorize the focus area into various severity levels.
- The categorized data is then used to train and develop a machine learning model, which classifies the test area into the aforementioned levels.
- Fine-tuning is done using the grid search method to optimize the performance of the model.
![Image of Fire Detection](https://github.com/UjalaJha/NasaSpaceAppChallenge/blob/master/Images/fire.PNG)


# Harmful Algae Bloom
- Initially we have used the sentinel 2 satellite imagery and segregated the bands and read its values for calculating to NDWI using green band (b3) and NIR band (Band 8). We have classified the water bodies from the image.
- Post classifying the water bodies, we have used following algorithm 
  - **Al10SABI** - Measures chlorophyll - Blue Band(B2), Green Band(B3), Red Band(B4) and NIR Band(B8 or B8A)
  - **TurbBow06RedOverGreen** - Measures Turbidity - Red Band(B3) and Green Band(B3)
  - **Be16FLHGreenRedNIR**  - Measures BlueGreenAlgae/PycoCynin- Red Band(B4), Green Band(B3) and NIR Band(B8)
- Equal Weightage to all these 3 algorithms is given to compute the water quality index which is then normalized between 0 to 1 using min max scaling where 0 represents pure water and 1 represents highest concentration of Harmful Algae Bloom.
![Image of HAB Detection](https://github.com/UjalaJha/NasaSpaceAppChallenge/blob/master/Images/algae.PNG)


# Tools and Technologies Used :

We have used a gradient boosting framework that uses tree-based algorithms to solve the problem ie., detection of flooded areas. We used python as the coding language, QGIS, ArcGis, EarthPy, LightGBM, Flask, RasterIO, GDAL software’s are used to develop a Machine learning model that detects the flooded area and non-flooded area.

# PPT Deck Link : 
https://docs.google.com/presentation/d/13n61bEEQtS3t37t1cA-qKOqJivS8KNCkB4DhWwKqqhQ/edit?usp=sharing

# Video Link :
https://drive.google.com/file/d/1nYckXCvIn8bqF3lXh31hffVREZElPr2z/view?usp=sharing

# Contribution :
We encourage any improvements or suggestion over our project. For Communications please contact at jhaujala3@gmail.com or https://www.linkedin.com/in/ujalajha/
