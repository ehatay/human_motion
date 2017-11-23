#!/usr/bin/env python
import csv
import roslib
import rospy
import tf
import rospkg
rospack = rospkg.RosPack()
rospack.get_path('human_motion')
rospy.init_node('data_viz')
rate = rospy.Rate(100)


q = raw_input("Which trial data? [1/2/3]")
path = rospack.get_path('human_motion')
if q == "1":
	data = open(path+"/data/trial1.csv", "r")
elif q == "2":
	data = open(path+"/data/trial2.csv", "r")
elif q == "3":
	data = open(path+"/data/trial3.csv", "r")
else:
	print "Trial number not listed! Exiting.."
	exit()

csvReader = csv.reader(data)
header = csvReader.next()

TimeStamp = header.index("TimeStamp")
FrameNumber = header.index("FrameNumber")

C7X,C7Y,C7Z = header.index("C7.PosX"),header.index("C7.PosY"),header.index("C7.PosZ")
T10X,T10Y,T10Z = header.index("T10.PosX"),header.index("T10.PosY"),header.index("T10.PosZ")
NAVEX,NAVEY,NAVEZ = header.index("NAVE.PosX"),header.index("NAVE.PosY"),header.index("NAVE.PosZ")
XYPHX,XYPHY,XYPHZ = header.index("XYPH.PosX"),header.index("XYPH.PosY"),header.index("XYPH.PosZ")
STRNX,STRNY,STRNZ = header.index("STRN.PosX"),header.index("STRN.PosY"),header.index("STRN.PosZ")
BBACX,BBACY,BBACZ = header.index("BBAC.PosX"),header.index("BBAC.PosY"),header.index("BBAC.PosZ")

LSHOX,LSHOY,LSHOZ = header.index("LSHO.PosX"),header.index("LSHO.PosY"),header.index("LSHO.PosZ")
LDELTX,LDELTY,LDELTZ = header.index("LDELT.PosX"),header.index("LDELT.PosY"),header.index("LDELT.PosZ")
LLEEX,LLEEY,LLEEZ = header.index("LLEE.PosX"),header.index("LLEE.PosY"),header.index("LLEE.PosZ")
LMEEX,LMEEY,LMEEZ = header.index("LMEE.PosX"),header.index("LMEE.PosY"),header.index("LMEE.PosZ")
LFRMX,LFRMY,LFRMZ = header.index("LFRM.PosX"),header.index("LFRM.PosY"),header.index("LFRM.PosZ")
LMWX,LMWY,LMWZ = header.index("LMW.PosX"),header.index("LMW.PosY"),header.index("LMW.PosZ")
LLWX,LLWY,LLWZ = header.index("LLW.PosX"),header.index("LLW.PosY"),header.index("LLW.PosZ")
LFINX,LFINY,LFINZ = header.index("LFIN.PosX"),header.index("LFIN.PosY"),header.index("LFIN.PosZ")

RSHOX,RSHOY,RSHOZ = header.index("RSHO.PosX"),header.index("RSHO.PosY"),header.index("RSHO.PosZ")
RDELTX,RDELTY,RDELTZ = header.index("RDELT.PosX"),header.index("RDELT.PosY"),header.index("RDELT.PosZ")
RLEEX,RLEEY,RLEEZ = header.index("RLEE.PosX"),header.index("RLEE.PosY"),header.index("RLEE.PosZ")
RMEEX,RMEEY,RMEEZ = header.index("RMEE.PosX"),header.index("RMEE.PosY"),header.index("RMEE.PosZ")
RFRMX,RFRMY,RFRMZ = header.index("RFRM.PosX"),header.index("RFRM.PosY"),header.index("RFRM.PosZ")
RMWX,RMWY,RMWZ = header.index("RMW.PosX"),header.index("RMW.PosY"),header.index("RMW.PosZ")
RLWX,RLWY,RLWZ = header.index("RLW.PosX"),header.index("RLW.PosY"),header.index("RLW.PosZ")
RFINX,RFINY,RFINZ = header.index("RFIN.PosX"),header.index("RFIN.PosY"),header.index("RFIN.PosZ")

TM1X,TM1Y,TM1Z = header.index("TM1.PosX"),header.index("TM1.PosY"),header.index("TM1.PosZ")
TM2X,TM2Y,TM2Z = header.index("TM2.PosX"),header.index("TM2.PosY"),header.index("TM2.PosZ")
TM3X,TM3Y,TM3Z = header.index("TM3.PosX"),header.index("TM3.PosY"),header.index("TM3.PosZ")
TM4X,TM4Y,TM4Z = header.index("TM4.PosX"),header.index("TM4.PosY"),header.index("TM4.PosZ")

List = []

for row in csvReader:
	"INFO"
	time = float(row[TimeStamp])
	frame = float(row[FrameNumber])

	"UPPER BODY"
	C7 = [float(row[C7X]),float(row[C7Y]),float(row[C7Z])]
	T10 = [float(row[T10X]),float(row[T10Y]),float(row[T10Z])]
	NAVE = [float(row[NAVEX]),float(row[NAVEY]),float(row[NAVEZ])]
	XYPH = [float(row[XYPHX]),float(row[XYPHY]),float(row[XYPHZ])]
	STRN = [float(row[STRNX]),float(row[STRNY]),float(row[STRNZ])]
	BBAC = [float(row[BBACX]),float(row[BBACY]),float(row[BBACZ])]

	"LEFT ARM"
	LSHO = [float(row[LSHOX]),float(row[LSHOY]),float(row[LSHOZ])]
	LDELT = [float(row[LDELTX]),float(row[LDELTY]),float(row[LDELTZ])]
	LLEE = [float(row[LLEEX]),float(row[LLEEY]),float(row[LLEEZ])]
	LMEE = [float(row[LMEEX]),float(row[LMEEY]),float(row[LMEEZ])]
	LFRM = [float(row[LFRMX]),float(row[LFRMY]),float(row[LFRMZ])]
	LMW = [float(row[LMWX]),float(row[LMWY]),float(row[LMWZ])]
	LLW = [float(row[LLWX]),float(row[LLWY]),float(row[LLWZ])]
	LFIN = [float(row[LFINX]),float(row[LFINY]),float(row[LFINZ])]

	"RIGHT ARM"
	RSHO = [float(row[RSHOX]),float(row[RSHOY]),float(row[RSHOZ])]
	RDELT = [float(row[RDELTX]),float(row[RDELTY]),float(row[RDELTZ])]
	RLEE = [float(row[RLEEX]),float(row[RLEEY]),float(row[RLEEZ])]
	RMEE = [float(row[RMEEX]),float(row[RMEEY]),float(row[RMEEZ])]
	RFRM = [float(row[RFRMX]),float(row[RFRMY]),float(row[RFRMZ])]
	RMW = [float(row[RMWX]),float(row[RMWY]),float(row[RMWZ])]
	RLW = [float(row[RLWX]),float(row[RLWY]),float(row[RLWZ])]
	RFIN = [float(row[RFINX]),float(row[RFINY]),float(row[RFINZ])]

	"TABLE"
	TM1 = [float(row[TM1X]),float(row[TM1Y]),float(row[TM1Z])]
	TM2 = [float(row[TM2X]),float(row[TM2Y]),float(row[TM2Z])]
	TM3 = [float(row[TM3X]),float(row[TM3Y]),float(row[TM3Z])]
	TM4 = [float(row[TM4X]),float(row[TM4Y]),float(row[TM4Z])]

	List.append([time,frame,C7,T10,NAVE,XYPH,STRN,BBAC,
		LSHO,LDELT,LLEE,LMEE,LFRM,LMW,LLW,LFIN,
		RSHO,RDELT,RLEE,RMEE,RFRM,RMW,RLW,RFIN,
		TM1,TM2,TM3,TM4
		])

def broadcast(msg,name):
	br = tf.TransformBroadcaster()
	br.sendTransform((-msg[0], msg[2], msg[1]), (0,0,0,1),
					 rospy.Time.now(),
					 name, "world")

def call(item):
		broadcast(item[2],"C7")
		broadcast(item[3],"T10")
		broadcast(item[4],"NAVE")
		broadcast(item[5],"XYPH")
		broadcast(item[6],"STRN")
		broadcast(item[7],"BBAC")
		broadcast(item[8],"LSHO")
		broadcast(item[9],"LDELT")
		broadcast(item[10],"LLEE")
		broadcast(item[11],"LMEE")
		broadcast(item[12],"LFRM")
		broadcast(item[13],"LMW")
		broadcast(item[14],"LLW")
		broadcast(item[15],"LFIN")
		broadcast(item[16],"RSHO")
		broadcast(item[17],"RDELT")
		broadcast(item[18],"RLEE")
		broadcast(item[19],"RMEE")
		broadcast(item[20],"RFRM")
		broadcast(item[21],"RMW")
		broadcast(item[22],"RLW")
		broadcast(item[23],"RFIN")
		broadcast(item[24],"TM1")
		broadcast(item[25],"TM2")
		broadcast(item[26],"TM3")
		broadcast(item[27],"TM4")

def main():
	for item in List:
		call(item)
		rate.sleep()
	rospy.spin()

if __name__ == '__main__':
	main()
	data.close()