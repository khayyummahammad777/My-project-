# -*- coding: utf-8 -*-
"""
Created on Tue Nov  4 19:21:43 2025

@author: hp
"""

# Traffic Accident Analysis - Single Script
import pandas as pd
import matplotlib.pyplot as plt

# 1️⃣ Load CSV
data = pd.read_csv(r"C:\Users\hp\Desktop\sagar\.vscode\vinod\traffic_accidents.csv")  # Update path

# 2️⃣ Clean column names (remove spaces)
data.columns = data.columns.str.strip()

# 3️⃣ Quick overview
print("Columns in dataset:", data.columns)
print("First 5 rows:\n", data.head())

# 4️⃣ Convert 'Occurred time' to datetime and extract hour
data['Occurred time'] = pd.to_datetime(data['Occurred time'], errors='coerce')
data['Hour'] = data['Occurred time'].dt.hour

# 5️⃣ Accidents by Hour
hour_counts = data['Hour'].value_counts().sort_index()
plt.figure(figsize=(8,5))
hour_counts.plot(kind='bar', color='skyblue')
plt.title("Accidents by Hour of Day")
plt.xlabel("Hour")
plt.ylabel("Number of Accidents")
plt.show()

# 6️⃣ Accidents by Vehicle Type
vehicle_counts = data['Vehicle type'].value_counts()
plt.figure(figsize=(8,5))
vehicle_counts.plot(kind='bar', color='orange')
plt.title("Accidents by Vehicle Type")
plt.xlabel("Vehicle Type")
plt.ylabel("Number of Accidents")
plt.show()

# 7️⃣ Accidents by Severity (Number of dead and injured)
severity_counts = data['Number of dead and injured'].value_counts().sort_index()
plt.figure(figsize=(8,5))
severity_counts.plot(kind='bar', color='red')
plt.title("Accidents by Severity")
plt.xlabel("Number of Dead/Injured")
plt.ylabel("Number of Accidents")
plt.show()

# 8️⃣ Accident Hotspots (Longitude vs Latitude)
plt.figure(figsize=(8,6))
plt.scatter(data['Longitude'], data['Latitude'], alpha=0.5, c='blue')
plt.title("Accident Hotspots")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.show()

# 9️⃣ Top 10 Accident Locations
top_locations = data['Location of occurrence'].value_counts().head(10)
print("\nTop 10 Accident Locations:\n", top_locations)
