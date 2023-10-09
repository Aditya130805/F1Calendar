from geopy.distance import geodesic
import folium

orderedCalendar = ["sakhir", "jeddah", "melbourne", "shanghai", "baku", "miami", "imola", "monaco", "barcelona", "montreal",
                   "spielberg", "united-kingdom", "budapest", "belgium", "zandvoort", "monza", "singapore", "japan", "qatar",
                   "austin", "mexico-city", "sau-paulo", "las-vegas", "abu-dhabi"]

coordinatesDict = {"sakhirLat": 26.0368, "sakhirLon": 50.5107,
                    "jeddahLat": 21.6370, "jeddahLon": 39.1030,
                   "melbourneLat": -37.8501, "melbourneLon": 144.9690,
                   "shanghaiLat": 31.3395, "shanghaiLon": 121.2216,
                   "bakuLat": 40.3729, "bakuLon": 49.8532,
                   "miamiLat": 25.9569, "miamiLon": -80.2314,
                   "imolaLat": 44.3443, "imolaLon": 11.7195,
                   "monacoLat": 43.7342, "monacoLon": 7.4190,
                   "barcelonaLat": 41.5685, "barcelonaLon": 2.2573,
                   "montrealLat": 45.5040, "montrealLon": -73.5270,
                   "spielbergLat": 47.2185, "spielbergLon": 14.7588,
                   "united-kingdomLat": 52.0733, "united-kingdomLon": -1.0147,
                   "budapestLat": 47.5817, "budapestLon": 19.2506,
                   "belgiumLat": 50.4369, "belgiumLon": 5.9720,
                   "zandvoortLat": 52.3866, "zandvoortLon": 4.5379,
                   "monzaLat": 45.583332, "monzaLon": 9.266667,
                   "singaporeLat": 1.2882, "singaporeLon": 103.8585,
                   "japanLat": 34.8456, "japanLon": 136.5390,
                   "qatarLat": 25.4863, "qatarLon": 51.4529,
                   "austinLat": 30.1346, "austinLon": -97.6359,
                   "mexico-cityLat": 19.4025, "mexico-cityLon": -99.0866,
                   "sau-pauloLat": -23.7022, "sau-pauloLon": -46.6932,
                   "las-vegasLat": 36.1147, "las-vegasLon": -115.201462,
                   "abu-dhabiLat": 24.4670, "abu-dhabiLon": 54.6018}

allCoordinates = []
for i in range(0, len(orderedCalendar)):
    placeCoordinates = (coordinatesDict[str(orderedCalendar[i]+"Lat")], coordinatesDict[str(orderedCalendar[i]+"Lon")])
    allCoordinates.append(placeCoordinates)


# Calculating the total distance travelled in the planned calendar
totalDistance = 0
for i in range(0, len(allCoordinates)-1):
    totalDistance += geodesic(allCoordinates[i], allCoordinates[i+1]).km

print(f"\nTotal distance to travel currently: {totalDistance}")


# Calculating the total distance travelled in the ideal calendar

idealMap = [allCoordinates[0]]
for i in range(0, len(allCoordinates)-1):
    minDist = 999999
    minDistIndex = 99
    for j in range(0, len(allCoordinates)):
        distance = geodesic(idealMap[i], allCoordinates[j]).km
        if minDist > distance > 1:
            isRepeated = False
            for coordinates in idealMap:
                if coordinates == allCoordinates[j]:
                    isRepeated = True
            if not isRepeated:
                minDist = geodesic(idealMap[i], allCoordinates[j]).km
                minDistIndex = j

    idealMap.append(allCoordinates[minDistIndex])

# print(idealMap)


totalIdealDistance = 0
for i in range(0, len(idealMap)-1):
    totalIdealDistance += geodesic(idealMap[i], idealMap[i+1]).km

print(f"Total distance to travel ideally: {totalIdealDistance}")
print(f"Extra travelled distance: {totalDistance - totalIdealDistance}")
print(f"% Distance extra travelled: {((totalDistance - totalIdealDistance) / totalDistance) * 100}")


# Finding the names of the races from the coordinates
idealRaceCalendar = []
for venue in idealMap:
    for i in range(0, len(allCoordinates)):
        if venue == allCoordinates[i]:
            idealRaceCalendar.append(orderedCalendar[i].capitalize())

print(idealRaceCalendar, "Yay!")

# Outputting the ideal calendar
print("\nIdeal Race Calendar: ")
for i in range(0, len(idealRaceCalendar)):
    print(f"\t{i+1}. {idealRaceCalendar[i]}")

print(f"\n {idealMap}")


# Plotting the calendar on the map
latitudeList = []
longitudeList = []

for location in idealMap:
    for i in range(0, 2):
        if i == 0:
            latitudeList.append(location[i])
        else:
            longitudeList.append(location[i])

plotMap = folium.Map(location=[48.130518, 11.5364172], zoom_start=1)
idealLocationsCoordinates = []

print(idealMap)

for location in idealMap:
    marker = folium.Marker(
        location=[location[0], location[1]]
    )
    marker.add_to(plotMap)


def plottingTheMap(path):
    html_page = f'{path}'
    plotMap.save(html_page)


folium.PolyLine(idealMap, color="green", weight=5, opacity=1).add_to(plotMap)
folium.PolyLine(allCoordinates, color="red", weight=1, opacity=1).add_to(plotMap)
plottingTheMap("/Users/adi/Desktop/abcd.html")
