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
bismuth.append(4.52614) # 
bismuth.append(7.23481) # 
bismuth.append(-0.9) # 
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
            
            walk = 0
            isInLine = False
            while walk < 1:
                linex = float(bismuth[0]) - walk * (float(bismuth[0]) - 4.52614)
                liney = float(bismuth[1]) - walk * (float(bismuth[1]) - 7.23481)
                linez = float(bismuth[2]) - walk * (float(bismuth[2]) - 0.9)
                distance3x2 = (float(equis) - float(linex))**2
                distance3y2 = (float(ye) - float(liney))**2
                distance3z2 = (float(zeta) - float(linez))**2
                distance3 = (distance3x2 + distance3y2 + distance3z2)**0.5
                #print str(equis) + ", " + str(ye) + ", " + str(zeta)
                #print str(linex) + ", " + str(liney) + ", " + str(linez) + "\n"
                if distance3 < 0.1:
                    isInLine = True
                    break
                walk = walk + 0.02

	    #if float(charge[counter-1]) < 0.01 and float(charge[counter-1]) > 0.001:
            if isInLine:
                    text.append(str(distance) + "," + str(float(charge[counter-1])-float(chargeB[counter-1])) + "\n")
                    #text.append(str(equis) + "," + str(ye) + "," + str(zeta) + "," + str(float(charge[counter-1])-float(chargeB[counter-1])) + "\n")
            counter = counter + 1
    os.remove("fort." + str(i+1) + ".csv")
    os.remove("fort." + str(i+1) + "B.csv")
    i = i + 1
    print "done " + str(i)
print "done todo"
open('data.csv', 'a').write("".join(text))

