import csv
import os

def reformat_employee_file(file_name): 
    print(file_name)
    
    with open(file_name, 'r', newline='') as datafile:

        file_reader = csv.DictReader(datafile)

        #read the header row and slect needed keys
        headers = file_reader.fieldnames
        emp_id_key = headers[0]
        name_key= headers[1]
        dob_key= headers[2]
        ssn_key = headers[3]
        state_key = headers[4]

        #output headers
        out_headers = ["Emp ID","First Name","Last Name","DOB","SSN","State"]
        o_emp_id_key = out_headers[0]
        o_first_name_key = out_headers[1]
        o_last_name_key = out_headers[2]
        o_dob_key = out_headers[3]
        o_ssn_key = out_headers[4]
        o_state_key = out_headers[5]

        reformated_data = []

        # US state abbreviation dictionary (courtesy github)
        us_state_abbrev = {
            'Alabama': 'AL',
            'Alaska': 'AK',
            'Arizona': 'AZ',
            'Arkansas': 'AR',
            'California': 'CA',
            'Colorado': 'CO',
            'Connecticut': 'CT',
            'Delaware': 'DE',
            'Florida': 'FL',
            'Georgia': 'GA',
            'Hawaii': 'HI',
            'Idaho': 'ID',
            'Illinois': 'IL',
            'Indiana': 'IN',
            'Iowa': 'IA',
            'Kansas': 'KS',
            'Kentucky': 'KY',
            'Louisiana': 'LA',
            'Maine': 'ME',
            'Maryland': 'MD',
            'Massachusetts': 'MA',
            'Michigan': 'MI',
            'Minnesota': 'MN',
            'Mississippi': 'MS',
            'Missouri': 'MO',
            'Montana': 'MT',
            'Nebraska': 'NE',
            'Nevada': 'NV',
            'New Hampshire': 'NH',
            'New Jersey': 'NJ',
            'New Mexico': 'NM',
            'New York': 'NY',
            'North Carolina': 'NC',
            'North Dakota': 'ND',
            'Ohio': 'OH',
            'Oklahoma': 'OK',
            'Oregon': 'OR',
            'Pennsylvania': 'PA',
            'Rhode Island': 'RI',
            'South Carolina': 'SC',
            'South Dakota': 'SD',
            'Tennessee': 'TN',
            'Texas': 'TX',
            'Utah': 'UT',
            'Vermont': 'VT',
            'Virginia': 'VA',
            'Washington': 'WA',
            'West Virginia': 'WV',
            'Wisconsin': 'WI',
            'Wyoming': 'WY',
            }
        
        #for each row in the input file add a new dictionary to output
        for row in file_reader:
            emp_id = row[emp_id_key]
            split_name  = row[name_key].split(" ")
            split_dob = row[dob_key].split("-")
            split_ssn = row[ssn_key].split("-")
            state_ab = us_state_abbrev[row[state_key]]
            reformated_data.append(
                {
                    o_emp_id_key:emp_id,
                    o_first_name_key:split_name[0],
                    o_last_name_key:split_name[1],
                    o_dob_key:(split_dob[2]+'/'+split_dob[1]+'/'+split_dob[0]),
                    o_ssn_key:('***-**-'+split_ssn[2]),
                    o_state_key:state_ab
                }
            )   

     
    return (out_headers, reformated_data)


def write_to_file(input_file_name, results_dictionary):
    # writes to an output file named results_"input_file_name", csv separated
    output_file_path = os.path.join("results_"+input_file_name)
    with open(output_file_path,"w") as csvfile:
        field_names = ["title","value"]
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(results_dictionary)




def main():

    # list of files to process
    file_names = ["employee_data1.csv","employee_data2.csv"]

    # for each file 
    # create a new dictionary in the needed format and populate
    # write out the dictionary in csv format
    for f in file_names:
        input_file_path = os.path.join(f)
        headers,reformatted_data_dict = reformat_employee_file(input_file_path)
        #print(results)
        output_file_path = os.path.join("output",f)
        with open(output_file_path,"w") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()
            writer.writerows(reformatted_data_dict)



if __name__ == "__main__":
    main()