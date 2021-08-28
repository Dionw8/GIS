# produces slope percentage file for inputted raster.
# should include 2 arguments
# 1. file path
# 2. raster
import arcpy
from arcpy import env
from arcpy.sa import *
arcpy.env.workspace = arcpy.GetParameterAsText(0)
if arcpy.CheckExtension("spatial") == "Available":
    arcpy.CheckOutExtension("spatial")
    # second argument is input shape file, must include complete path.
    inputFeatures = arcpy.GetParameterAsText(1)
    myremap = RemapRange([[1000,2000,1], [2000,3000,2], [3000,4000,3]])
    outreclass = Reclassify(inputFeatures, "VALUE", myremap)
    outreclass.save("elev_recl")
    arcpy.CheckInExtension("spatial")
else:
    print "Spatial Analyst license is not available."

def fillin(manning):
	if Feature == "1":
		return 0.030
	elif Feature == "4":
		return 0.050
	elif Feature == "2":
		return 0.035
	elif Feature == "5":
 		return 0.080

 		return 0.120
	else:
		return 


fillin(!manning!)


# Reclassify values to another value
# More calculator examples at esriurl.com/CalculatorExamples
def Reclass(texcl):
    if texcl == "Sand":
        return .42
    elif texcl == "Loamy sand":
        return .40
    elif texcl == "Sandy loam":
        return 0.41
    elif texcl == "Loam":
        return .43
    elif texcl == "Silt loam":
        return .49
    elif texcl == "Sandy clay loam":
        return .33
    elif texcl == "Clay loam":
        return .31
    elif texcl == "Silty clay loam":
        return .43
    elif texcl == "Sandy clay":
        return .32
    elif texcl == "Silty clay":
        return .42
    elif texcl == "Clay":
        return .39
    elif texcl == 0:
        return 0
    return texcl
32.8054459280668
32.8053607057825
