#!/usr/bin/python
import os
import math
import csv

###################################################################
# Fort Split A                                                    #
###################################################################

masterfort = open("fort.25.A", "r").readlines()
forties = []
counter = -1

for line in masterfort:
    firstword = line.split()
    if firstword[0].find("MAP")!=-1:
        counter = counter + 1
        forties.append([])
    forties[counter].append(line)

i = 0
j = 0

for file in forties:
    text = ""
    for line in forties[i]:
        text = text + str(line)
        j = j + 1 
    open('fort.' + str(i+1) + '.csv', 'a').write(text)
    i = i + 1

    
###################################################################
# Fort Split B                                                    #
###################################################################

masterfort = open("fort.25.B", "r").readlines()
forties = []
counter = -1

for line in masterfort:
    firstword = line.split()
    if firstword[0].find("MAP")!=-1:
        counter = counter + 1
        forties.append([])
    forties[counter].append(line)

i = 0
j = 0

for file in forties:
    text = ""
    for line in forties[i]:
        text = text + str(line)
        j = j + 1 
    open('fort.' + str(i+1) + 'B.csv', 'a').write(text)
    i = i + 1

        
###################################################################
# Main                                                            #
###################################################################


i=0
text = []
bismuth = []
bismuth.append(6.5675) # 
bismuth.append(4.4680) # 
bismuth.append(5.3766) # 
bismuth2 = []
bismuth2.append(bismuth[0]) # 
bismuth2.append(bismuth[1]) # 
bismuth2.append(bismuth[2]) #

while os.path.exists(r'fort.' + str(i+1) + '.csv') and os.path.exists(r'fort.' + str(i+1) + 'B.csv'):
    fort = open("fort." + str(i+1) + ".csv", "r").readlines()
    fortB = open("fort." + str(i+1) + "B.csv", "r").readlines()

    content1=''
    content2=''
    content3=''
    content4=[]
    content5=[]
    content1B=''
    content2B=''
    content3B=''
    content4B=[]
    content5B=[]
    
    counter = 1
    sector = 0
    for line in fort:
        firstword = line.split()
        if firstword[0].find("MAP")!=-1:
            content1 = line
            sector = 1
        elif sector==1:
            content2 = line
            chargelines = math.ceil(float(content1.split()[1]) * float(content1.split()[2]) / 6)
            sector=2
        elif sector==2:
            content3 = line
            sector=3
        elif sector==3 and counter <= chargelines:
            content4.append(line)
            counter = counter + 1
        elif sector==3:
            sector=4
            content5.append(line)
        elif sector==4:
            content5.append(line)
    
    counter = 1
    sector = 0        
    for line in fortB:
        firstword = line.split()
        if firstword[0].find("MAP")!=-1:
            content1B = line
            sector = 1
        elif sector==1:
            content2B = line
            chargelinesB = math.ceil(float(content1B.split()[1]) * float(content1B.split()[2]) / 6)
            sector=2
        elif sector==2:
            content3B = line
            sector=3
        elif sector==3 and counter <= chargelinesB:
            content4B.append(line)
            counter = counter + 1
        elif sector==3:
            sector=4
            content5B.append(line)
        elif sector==4:
            content5B.append(line)

    #Extract grid info
    xpoints = int(content1.split()[1])
    ypoints = int(content1.split()[2])
    xstep = float(content1.split()[3])
    ystep = float(content1.split()[4])
    ax = float(content2[0:12])
    ay = float(content2[12:24])
    az = float(content2[24:36])
    bx = float(content2[36:48])
    by = float(content2[48:60])
    bz = float(content2[60:72])
    cx = float(content3[0:12])
    cy = float(content3[12:24])
    cz = float(content3[24:36])
    
    #Extract charge values
    charge=[]
    for row in content4:
        if row[0:12]!="":
            charge.append(row[0:12])
        if row[12:24]!="":
            charge.append(row[12:24])
        if row[24:36]!="":
            charge.append(row[24:36])
        if row[36:48]!="":
            charge.append(row[36:48])
        if row[48:60]!="":
            charge.append(row[48:60])
        if row[60:72]!="":
            charge.append(row[60:72])

    chargeB=[]
    for row in content4B:
        if row[0:12]!="":
            chargeB.append(row[0:12])
        if row[12:24]!="":
            chargeB.append(row[12:24])
        if row[24:36]!="":
            chargeB.append(row[24:36])
        if row[36:48]!="":
            chargeB.append(row[36:48])
        if row[48:60]!="":
            chargeB.append(row[48:60])
        if row[60:72]!="":
            chargeB.append(row[60:72])            
            
    #Print x, y, z, charge
    counter = 1
    for ypoint in range(ypoints):
        for xpoint in range(xpoints):
            equis = ax - xpoint * (ax - bx) / (xpoints-1)
            ye = ay - xpoint * (ay - by) / (xpoints-1) - ypoint * (ay - cy) / (ypoints-1)
            zeta = az - xpoint * (az - bz) / (xpoints-1)
            distancex2 = (float(bismuth[0]) - float(equis))**2
            distancey2 = (float(bismuth[1]) - float(ye))**2
            distancez2 = (float(bismuth[2]) - float(zeta))**2
            distance = (distancex2 + distancey2 + distancez2)**0.5

            distance2x2 = (float(bismuth2[0]) - float(equis))**2
            distance2y2 = (float(bismuth2[1]) - float(ye))**2
            distance2z2 = (float(bismuth2[2]) - float(zeta))**2
            distance2 = (distance2x2 + distance2y2 + distance2z2)**0.5


	    #if float(charge[counter-1]) < 0.01 and float(charge[counter-1]) > 0.001:
            if distance < 1.0 or distance2 < 1.0:
                    text.append(str(equis) + "," + str(ye) + "," + str(zeta) + "," + str(float(charge[counter-1])-float(chargeB[counter-1])) + "\n")
            counter = counter + 1
    os.remove("fort." + str(i+1) + ".csv")
    os.remove("fort." + str(i+1) + "B.csv")
    i = i + 1
    print "done " + str(i)
print "done todo"
open('data.csv', 'a').write("".join(text))

