#Written by Kevin Linger (uvaballfan)

#This code projects the bracket locations for the 1-8 seeds in the NCAA
#tournament. Distance on a sphere is used to determine locations. This
#differs from Lunardi who has SDST in San Antonio instead of Spokane...

#To add a team, follow the template starting around line 100. The definition is
#School(latitude, longitude, rank, name). 
#CURRENTLY THE RANK IS NOT USED AT ALL. I put this here in case I wanted to
#use it later. 
#THE CORRECT WAY TO RANK TEAMS IS BASED ON THE SCURVE.APPEND ORDER.
#To make Florida the overall number 1 seed, you would have to append
#Florida first, etc. I thought this would be easier because you only have
#to change the order of one team, instead of say, moving a team from 25 to 
#20 and having to lower all numbers of the teams that were above it.

#This is probably really buggy! I wrote it really quickly and it isn't 
#polished at all. Feel free to report bugs to me, or hell, even take this
#yourself and make it better. 

#enjoy!

import math

#I use this for my distance calculation
#Method obtained from: http://www.johndcook.com/python_longitude_latitude.html
def distance_on_unit_sphere(lat1, long1, lat2, long2):

    # Convert latitude and longitude to 
    # spherical coordinates in radians.
    degrees_to_radians = math.pi/180.0
        
    # phi = 90 - latitude
    phi1 = (90.0 - lat1)*degrees_to_radians
    phi2 = (90.0 - lat2)*degrees_to_radians
        
    # theta = longitude
    theta1 = long1*degrees_to_radians
    theta2 = long2*degrees_to_radians
        
    # Compute spherical distance from spherical coordinates.
        
    # For two locations in spherical coordinates 
    # (1, theta, phi) and (1, theta, phi)
    # cosine( arc length ) = 
    #    sin phi sin phi' cos(theta-theta') + cos phi cos phi'
    # distance = rho * arc length
    
    cos = (math.sin(phi1)*math.sin(phi2)*math.cos(theta1 - theta2) + 
           math.cos(phi1)*math.cos(phi2))
    arc = math.acos( cos )

    # Remember to multiply arc by the radius of the earth 
    # in your favorite set of units to get length.
    return arc


class City:
	def __init__(self, lat, lon, name):
		self.lat = lat
		self.lon = lon
		self.name = name
		self.count = 2

#These are the first round locations, coordinates obtained from Google
SanDiego = City(32.72, 117.16, "San Diego")
Raleigh = City(35.82, 78.64, "Raleigh")
Spokane = City(47.66, 117.43, "Spokane")
SanAntonio = City(29.42, 98.5, "San Antonio")
Orlando = City(28.42, 81.30, "Orlando")
Buffalo = City(42.90, 78.85, "Buffalo")
StLouis = City(38.63, 90.20, "St. Louis")
Milwaukee = City(43.05, 87.95, "Milwaukee")

cityList = [SanDiego, Raleigh, Spokane, SanAntonio, Orlando, Buffalo, StLouis, Milwaukee]		

#This defines a school. It also generates the order of cities by distance from that school
class School:
	def __init__(self, lat, lon, rank, name):
		self.lat = lat
		self.lon = lon
		self.rank = rank
		self.name = name
		self.cityRank = list()
		for city in cityList:
			self.cityRank.append(city)

		self.cityRank.sort(key=lambda x: distance_on_unit_sphere(lat, lon, x.lat, x.lon), reverse=False)
		if(distance_on_unit_sphere(lat, lon, self.cityRank[0].lat, self.cityRank[0].lon) < 0.0001):
			temp = self.cityRank[0]
			self.cityRank[0] = self.cityRank[1]
			self.cityRank[1] = self.cityRank[2]
			self.cityRank[2] = self.cityRank[3]
			self.cityRank[3] = self.cityRank[4]
			self.cityRank[4] = self.cityRank[5]
			self.cityRank[5] = self.cityRank[6]
			self.cityRank[6] = self.cityRank[7]
			self.cityRank[7] = temp


#This is where the schools are defined.
Syracuse = School(43.05, 76.14, 1, "Syracuse")			
Arizona = School(32.22, 110.93, 2, "Arizona")
Florida = School(29.65, 82.32, 3, "Florida")
WichitaSt = School(37.69, 97.34, 4, "Wichita St")
MichiganSt = School(42.73, 84.48, 5, "Michigan St")
Villanova = School(40.04, 75.35, 6, "Villanova")
SanDiegoSt = School(32.72, 117.16, 7, "San Diego St")
Kansas = School(38.97, 95.23, 8, "Kansas")
Duke = School(35.99, 78.91, 9, "Duke")
Michigan = School(42.28, 83.74, 10, "Michigan")
Creighton = School(41.26, 95.95, 11, "Creighton")
Cincinnati = School(39.10, 84.52, 12, "Cincinnati")
Kentucky = School(38.03, 84.49, 13, "Kentucky")
IowaSt = School(42.03, 93.62, 14, "Iowa St")
Iowa = School(41.65, 91.53, 15, "Iowa")
Virginia = School(38.03, 78.48, 16, "Virginia")
Wisconsin = School(43.07, 89.40, 17, "Wisconsin")
OklahomaSt = School(36.12, 97.07, 18, "Oklahoma St")
Louisville = School(38.25, 85.77, 19, "Louisville")
Texas = School(30.25, 97.75, 20, "Texas")
OhioSt = School(39.98, 82.98, 21, "Ohio St")
StLouisU = School(38.63, 90.20, 22, "St. Louis")
Oklahoma = School(35.22, 97.42, 23, "Oklahoma")
UCLA = School(35.05, 118.25, 24, "UCLA")
UConn = School(41.81, 72.25, 25, "UConn")
UMass = School(42.37, 72.52, 26, "UMass")
Pitt = School(40.44, 80.00, 27, "Pittsburgh")
Gonzaga = School(47.66, 117.43, 28, "Gonzaga")
Memphis = School(35.12, 89.98, 29, "Memphis")
UNC = School(35.93, 79.03, 30, "UNC")
VCU = School(37.54, 77.43, 31, "VCU")
NewMexico = School(35.11, 106.61, 32, "New Mexico")
GWU = School(38.90, 77.03, 33, "George Washington")
California = School(37.87, 122.27, 34, "California")
SMU = School(32.78, 96.80, 35, "SMU")

sCurve = []

#Order of the appends defines the S-Curve
sCurve.append(Syracuse)#1
sCurve.append(Arizona)#2
sCurve.append(Florida)#3
sCurve.append(WichitaSt)#4

sCurve.append(MichiganSt)#5
sCurve.append(Villanova)#6
sCurve.append(SanDiegoSt)#7
sCurve.append(Kansas)#8

sCurve.append(Duke)#9
sCurve.append(Michigan)#10
sCurve.append(Creighton)#11
sCurve.append(IowaSt)#12

sCurve.append(Cincinnati)#13
sCurve.append(Kentucky)#14
sCurve.append(Virginia)#15
sCurve.append(Wisconsin)#16

sCurve.append(Louisville)
sCurve.append(Iowa)#17
sCurve.append(OhioSt)#18
sCurve.append(StLouisU)#19

sCurve.append(Oklahoma)#21
sCurve.append(Texas)#22
sCurve.append(UCLA)#23
sCurve.append(Pitt)#24

sCurve.append(UMass)#25
sCurve.append(UConn)#26
sCurve.append(Memphis)#27
sCurve.append(SMU)#28

sCurve.append(Gonzaga)#29
sCurve.append(OklahomaSt)#30
sCurve.append(UNC)#31
sCurve.append(GWU)#32

oneLocs = []
twoLocs = []
threeLocs = []
fourLocs = []


#If you are a top 4 seed team, take the closest city available
for i in range(0, len(sCurve)):

	if(i == 0):
		print "\n1 SEEDS:"
	elif(i == 4):
		print "\n2 SEEDS"
	elif(i == 8):
		print "\n3 SEEDS"
	elif(i == 12):
		print "\n4 SEEDS"
	elif(i == 16):
		print "\n5 SEEDS"
	elif(i == 20):
		print "\n6 SEEDS"
	elif(i == 24):
		print "\n7 SEEDS"
	elif(i == 28):
		print "\n8 SEEDS"

	print
	team = sCurve[i]
	print "Location for " + team.name + " is"
	if(i < 16):
		for city in team.cityRank:
			#print city.name
			flag = False
			for j in cityList:
				if(city.name == j.name and j.count > 0):
					#print "hi"
					j.count = j.count - 1
					print city.name
					flag = True
					if(i < 4):
						oneLocs.append(j)
					elif(i < 8):
						twoLocs.append(j)
					elif(i < 12):
						threeLocs.append(j)
					else:
						fourLocs.append(j)
					break
			if(flag):
				break
#otherwise, if you are a 5 seed, take the closest 4 seed location, etc.
	elif(i < 20):
		minLoc = 100.0
		minCity = City(0, 0, "")
		for city in fourLocs:
			dist = distance_on_unit_sphere(team.lat, team.lon, city.lat, city.lon)
			if(dist < minLoc and dist > 0.0001):
				minLoc = dist
				minCity = city
		fourLocs.remove(minCity)
		print minCity.name

	elif(i < 24):
		minLoc = 100.0
		minCity = City(0, 0, "")
		for city in threeLocs:
			dist = distance_on_unit_sphere(team.lat, team.lon, city.lat, city.lon)
			if(dist < minLoc and dist > 0.0001):
				minLoc = dist
				minCity = city
		threeLocs.remove(minCity)
		print minCity.name

	elif(i < 28):
		minLoc = 100.0
		minCity = City(0, 0, "")
		for city in twoLocs:
			dist = distance_on_unit_sphere(team.lat, team.lon, city.lat, city.lon)
			if(dist < minLoc and dist > 0.0001):
				minLoc = dist
				minCity = city
		twoLocs.remove(minCity)
		print minCity.name

	else:
		minLoc = 100.0
		minCity = City(0, 0, "")
		for city in oneLocs:
			dist = distance_on_unit_sphere(team.lat, team.lon, city.lat, city.lon)
			if(dist < minLoc and dist > 0.0001):
				minLoc = dist
				minCity = city
		oneLocs.remove(minCity)
		print minCity.name		


