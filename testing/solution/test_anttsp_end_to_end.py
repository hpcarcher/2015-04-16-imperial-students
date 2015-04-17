import os
import os.path
import pickle


def file_exists(filename):
    if (os.path.isfile(filename)):
        print "OK ", filename, " exists"
    else:
        print "FAIL ", filename, " does not exist"

def confirm_path_form(filename):
    result = pickle.load(open(filename, "r"))
    best_path_nodes = result[0]
    best_path_names = result[1]
    if len(best_path_nodes) != len(best_path_names):
        print "FAIL ", filename, " nodes and names are different lengths"
        return
    if len(best_path_nodes) != len(set(best_path_nodes)):
        print "FAIL ", filename, " contains repeats" 
        return
    print "OK " , filename, " contains valid output" 






for f in os.listdir("./output"):
    if f.endswith(".pickle"):
        os.remove("./output/"+f)

os.system("python anttsp.py 7 data/scottish_city_distances.pickle output/scottish_path.pickle")

print "test scottish cities 7 node path"
file_exists("output/scottish_path.pickle")


print "test scottish cities 7 node path output is correct form"
confirm_path_form("output/scottish_path.pickle")



