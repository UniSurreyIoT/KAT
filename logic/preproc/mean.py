__author__ = 'frieder'
import numpy as np
import math
import bottleneck as bn
class mean():
    def process(self, window, output_length):
        data = np.array_split(window, output_length)
        result = []
        for section in data:
           result.append(section.mean())
        result = np.array(result)
        #print "paa output shape", result.shape
        return result

    def getConfigurationParams(self):
        return {"Output_length":"100"}
