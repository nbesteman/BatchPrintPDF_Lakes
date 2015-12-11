#-------------------------------------------------------------------------------
# Name:        Directory Search for File Geodatabases
# Purpose:      Reports location of file geodatabases in J drive in GDBPath1.txt in C:\\workspace
#
# Author:      BMay
#
# Created:     28/09/2015
# Copyright:   (c) BMay 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import arcpy,os

#rootDir = "j:\\Data"
rootDir = "C:\Data\Geodatabases\EQ_Data_Merge\Source"
exten = "T"
#Not sure what exten does but script does not work if its removed

prjunits=[]
#This is a list object that is populated with prjx but not otherwise used at this time

def step(ext,dirName,names):

    for name in names:
        if name.endswith(".gdb"):
            prjx=(os.path.join("\\"+rootDir,dirName+"\\"+name))
            print prjx
            prjunits.append(prjx)
            #This block outputs a series of items to .txt
            f = open('C:\\Data\\Geodatabases\\EQ_Data_Merge\\Source\\Merge4.txt','a')
            ##f = open('j:\\Apps\\Python\\ESRI\\BatchReprojectGDB\\build\\GDBPath.txt','a')
            #a is for append mode
            f.write(prjx+'\n')
            #writes to .txt
            f.close()

os.path.walk(rootDir,step,exten)

#This block outputs a list to .txt
##g = open('c:\\Apps\\Python\\BatchReprojectGDB\\build\\GDBPath2.txt','a')
##prju = str(prjunits)
##g.write(prju)
##g.close()
##print prjunits

