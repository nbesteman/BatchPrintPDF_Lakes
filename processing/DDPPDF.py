#-------------------------------------------------------------------------------
# Name:        Data Driven Pages PDF Printer
# Purpose:
#
# Author:      BMay
#
# Created:     23/11/2015
# Copyright:   (c) BMay 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------


#You can also use python in conjunction with data driven pages to cycle through each page,
#and perform one of the many operations supported by arcpy.mapping. For example, you can update a layer?s
#symbology, update some layout text, and export or print each map. This example demonstrates how to cycle
#through all your data driven pages and export them as PNG files:

import arcpy

#Specify the map document
#mxd = arcpy.mapping.MapDocument("C:\Data\MXD_s\Production\ACParcelPrinter.mxd")
mxd = arcpy.mapping.MapDocument("C:\Data\MXDs\AC_ParcelAtlas.mxd")
##i= 0

#Export each of the data driven pages

for pageNum in range(15620, mxd.dataDrivenPages.pageCount + 1):
    mxd.dataDrivenPages.currentPageID = pageNum
##    i=i+1
    ddp = mxd.dataDrivenPages
    ###pageID = ddp.getPageIDFromName(MAPPING_ID)
    #pageID = ddp.pageRow.MAPPING_ID
    pageID = ddp.pageRow.MAPPING_ID

    print pageID
    #print "Exporting page {0} of {1}".format(str(mxd.dataDrivenPages.currentPageID), str(mxd.dataDrivenPages.pageCount))
    ##parcelnum = mxd.dataDrivenPages.pageRow.Name
    ##print parcelnum
    arcpy.mapping.ExportToPDF(mxd, "C:\Data\MXDs\Production/\/" + pageID + ".pdf")
##    if i > 24:
##        break
del mxd


