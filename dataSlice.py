filepath = "/home/user/Documents/Project3/CSE512-Project-Phase3/src/resources/yellow_tripdata_2017-01.csv"

sliceSize = 1000;
totalCount = 7;
i = 0;
curCount = 0;

file = open(filepath, "r")
file.readline()
file.readline()

for curCount in range(0, totalCount):
    outputPath = str.format("/home/user/Documents/Project3/CSE512-Project-Phase3/src/resources/yellow_tripdata_{0}.csv", curCount)
    filewrite = open(outputPath, "w")
    for i in range (0, sliceSize):
        line = file.readline()
        filewrite.write(line )
    filewrite.close()
file.close()