import sys
import os
import json
from pprint import pprint


def run_analysis():
    "'the main function to read the json file from input directory and start parsing'"
    #take the sys arguments as the input and output file path and names
    input_dir=sys.argv[1]
    #output_top_10_occupations_file=sys.argv[2]
    #output_top_10_states_file=sys.argv[3]

    #find the file in input directory and pass to the input_file
    file_list=os.listdir(input_dir)
    input_file=input_dir+file_list[0]

    #create the variables of map data structures holding the key of occupations and working_states
    # and values of counts respectfully
    Certified_Total=0.0
    occupations={}
    working_states={}

    # read the jsonfile one by one and parsing each json format of data into
    # objects,
    with open(input_file) as jsonfile:
    	records=json.load(jsonfile)



    pprint(records["orders"][0]["line_items"])




# run the analysis function if the file been triggered directly
if __name__ == '__main__':
    run_analysis()
