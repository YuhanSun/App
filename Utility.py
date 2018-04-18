def read_lines(filename, line_count):
    '''
    Read the first several lines
    :param filename:
    :param line_count:
    :return:
    '''
    file = open(filename, "r")
    i = 0
    for line in file:
        print line
        i+=1
        if i == line_count:
            break
    file.close()

def get_line_count(filename):
    file = open(filename, "r")
    i = 0
    for line in file:
        i += 1
    file.close()
    return i


# read_lines("D:\Project_Data\wikidata-20180308-truthy-BETA.nt\wikidata-20180308-truthy-BETA.nt", 20)
filename = "D:\Google_Drive\Courses\\512_TA_2018_Spring\CSE512_Vocareum\Project3\yellow_tripdata_2009-01_point.csv"
# filename = "D:\Ubuntu_shared\GeoReachHop\data\Patents_100_random_20\\128_128_80_80_4_2.txt"
# read_lines(filename, 20)
print get_line_count(filename)