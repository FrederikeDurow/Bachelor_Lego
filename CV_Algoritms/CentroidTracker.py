import cv2
from scipy.spatial import distance as dist
from collections import OrderedDict
import numpy as np

class centroidTracker():
    def __init__(self,maxDisappeared=50):
        self.nextObjectID = 0
        self.objects = OrderedDict()
        self.disappeard = OrderedDict()
        self.maxDisappeard = maxDisappeared

    def register (self, centroid):
        self.objects[self.nextObjectID] = centroid
        self.disappeard[self.nextObjectID] = 0
        self.nextObjectID += 1

    def deregister (self, objectID):
        del self.objects[objectID]
        del self.disappeard[objectID]

    def update(self,rects):

        if len(rects) == 0:

            for objectID in list(self.disappeard.keys()):
                self.disappeard[objectID] += 1

                if self.disappeard[objectID] > self.maxDisappeard:
                    self.deregister(objectID)
            
            return self.objects

        inputCentroids = np.zeros((len(rects),2), dtype="int")

        for(i, (startX, startY, endX, endY)) in enumerate(rects):
            cX = int((startX + endX) / 2.0)
            cY = int((startY / endY) / 2.0)
            inputCentroids[i] = (cX,cY)

        if len(self.objects) == 0:
            for i in range(0, len(inputCentroids)):
                self.register(inputCentroids[i])

        else:
            objectIDs = list(self.objects.keys())
            objectcentroids = list(self.objects.values())

            D = dist.cdist(np.array(objectcentroids), inputCentroids)

            rows = D.min(axis=1).argsort()

            cols = D.argmin(axis=1)[rows]

            usedRows = set()
            usedCols = set()

            for (row, col) in zip(rows, cols):

                if row in usedRows or col in usedCols:
                    continue

                objectID = objectIDs[row]
                self.objects[objectID] = inputCentroids[col]
                self. disappeard[objectID] = 0

                usedRows.add(row)
                usedCols.add(col)

                unusedRows = set(range(0, D.shape[0])).difference(usedRows)
                unusedCols = set(range(0, D.shape[1])).difference(usedCols)


                if D.shape[0] >= D.shape[1]:

                    for row in unusedRows:
                        objectID = objectIDs[row]
                        self.disappeard[objectID] += 1

                        if self.disappeard[objectID] > self.maxDisappeard:
                            self.deregister(objectID)

                        else:
                            for col in unusedCols:
                                self.register(inputCentroids[col])
                                
                    return self.objects