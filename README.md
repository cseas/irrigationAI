# Futureskills-Excelsior
Closed loop irrigation solution for farmers:

Irrigating fields plays a vital role in crop yield. However, how much and when to irrigate is still
moderated by the traditional knowledge for the farmers. Knowing how much water is actually
required for a given crop for a particular soil type depends majorly on soil’s capacity to hold
moisture. 

We've developed an IoT, AI based solution which can auto irrigate the fields for a given crop based
on the soil moisture content.

We've come up with a solution to tackle ALL the features expected in the Aeris problem statement.

This document covers the following sections:
- [Features](#features)
- [Hardware](#hardware)
- [Working](#working)
- [Power efficient system](#power-efficient-system)
- [Water efficient system](#water-efficient-system)
- [Secure system](#secure-system)
- [Effective maintenance](#effective-maintenance)

## Features
1. `Know the moisture content in the soil using sensors.`
This is achieved using soil moisture sensors that are immersed into the soil.
2. `Predict the weather condition.`
This is done using a Machine Learning model that has been trained on historical data for a region and predicts weather condition in real-time without the need for depending on the internet for information, hence the model gradually adapts better to the local weather of the particular area where it is installed.
(a) If there will be rain, the motor remains OFF.
(b) If it will not rain, the motor is switched ON for a specific amount of time.
3. `Based on the soil moisture present, determine the quantity of water to be released for irrigation.`
We've used another Machine Learning model here which takes the following possible inputs:
    - Soil Sensors
        - Soil Moisture
        - Soil Water Potential
        - Soil temperature
    - Weather Conditions
        - Rainfall
        - Wind Speed
        - Air Temperature
        - Relative Humidity
        - Global Radiation
        - Dew Point
        - Vapour Pressure Deficit
    - Crop Evapotranspiration

    The model calculates the minutes of irrigation required and turns the motor ON for the required period if there's no chance of a rain, depending on how much water the crop lacks in real-time.
4. `Stop the motor when required soil moisture content has been achieved.`
The system monitors the soil moisture content using sensors and stops the motor when the optimal amount of water has been achieved for the crop. It also takes into account the age of the crop since crops require different amounts of water during different phases in the growing period.

5. `Automatic start and stop of the motor for irrigating water in the field.`
The entire system is built to intelligently operate on its own without need for human intervention.

## Hardware
Following is a list of minimum hardware to realise a deployable working prototype of the system.
- WiFi Router
- Node MCUs
- Soil moisture sensors
- Waterproof boxes
- Alarms
- Raspberry Pi
- Connecting wires for internal components

## Working
- Soil sensors connected to Node MCUs are deployed throughout the field in a closed loop. Each node is encased in a waterproof box with an alarm system.
- The nodes are connected to a central router through WiFi, enabling the system to communicate wirelessly.
- Data from the sensors is sent to the router which is passed on to the Raspberry Pi for analysis.
- Using Machine Learning, real-time analysis of the weather and soil is done.
- Depending on the size of the field, an appropriate time is calculated and the motor is switched ON for the required amount of time.
- The motor remains OFF if the system predicts a fair chance of rain. If it doesn't rain for a considerable amount of time, the motor is switched ON to supply the water required.
- This process repeats at regular intervals till the crop is ready to be harvested.

## Power efficient system
We took several measures to increase the power efficiency of the system.
- Rather than staying ON constantly, the nodes send requests at regular intervals to conserve battery life.
- Solar panels can be incorporated at every node to further increase the autonomy of the system for longer periods without needing maintenance.

## Water efficient system
Since all the nodes communicate separately to the central device, drip/sprinkler can be switched ON only for the particular area requiring water, further conserving water and improving the accuracy of the system. This feature additonally requires a servomotor.

## Secure system
Each node can be equipped with a geo-fencing enabled alarm which goes ON in case a node leaves the vicinity of the field, alerting the owner of theft.

## Effective maintenance
- Since the nodes work on a request-response model, it can be easily identified if a node stops working or malfunctions, in which case the particular node can be repaired by a technician or simply replaced by the farmer, making the system easily maintenable.
- The health of the nodes and the system can be monitored through a user-friendly mobile or web-based interface, informing the user which particular nodes have malfunctioned in the field.