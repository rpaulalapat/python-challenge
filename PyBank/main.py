import csv
import os


def calculate_months(start_month_year, end_month_year):
    month_dict = {"Jan":1,"Feb":2,"Mar":3,"Apr":4,"May":5,"Jun":6,"Jul":7,"Aug":8,"Sep":9,"Oct":10,"Nov":11,"Dec":12}
    start_date = start_month_year.split("-")
    end_date = end_month_year.split("-")
    start_m = month_dict[start_date[0]]
    start_y = int(start_date[1])
    end_m = month_dict[end_date[0]]
    end_y = int(end_date[1])
    #total months is the number of years time twelve
    #then assuming Jan to Jan, add months in ending year and subtract months in stating year
    months = (end_y - start_y)*12 + end_m - start_m
    return months


def tallyRevenues(file_name, date_column, revenue_column): 
    print("Processing "+file_name)
    file_path = os.path.join(file_name)
    with open(file_path, 'r', newline='') as datafile:

        total_revenue = 0.0
        prev_revenue = 0.0
        revenue = 0.0
        revenue_dict = {}
        revenue_change_dict = {}
        #results = []
        first_row = True
        fileReader = csv.DictReader(datafile)

        #create a dictionary with the data key: date, value: revenue
        for row in fileReader:
            date = row[date_column]
            revenue = row[revenue_column]
            revenue_dict[date]=revenue

        # calculate total months
        dates = list(revenue_dict.keys())
        total_months = calculate_months(dates[0],dates[-1])

        #calculate total revenue
        for x in list(revenue_dict.values()):
            total_revenue += float(x)

        #create a dictionary with key date and value change_in_revenue
        for d in dates:
            if first_row:
                prev_revenue = float(revenue_dict[d])
                first_row = False
            else:
                revenue = float(revenue_dict[d])
                revenue_change_dict[d] = revenue - prev_revenue
                prev_revenue = revenue
                revenue_changes = list(revenue_change_dict.values())
                max_rev_change = max(revenue_changes)
                max_rev_change_date = list(revenue_change_dict.keys())[revenue_changes.index(max_rev_change)]
                min_rev_change = min(revenue_changes)
                min_rev_change_date = list(revenue_change_dict.keys())[revenue_changes.index(min_rev_change)]

        #populate the result list
        headers = ["title","value"]
        results = { "Total Months":total_months,
                    "Total Revenue":total_revenue,
                    "Average Revenue Change":(total_revenue / total_months),        
                    "Greatest Increase In Revenue":(str(max_rev_change)+" on "+max_rev_change_date),
                    "Greatest Decrease in Revenue":(str(min_rev_change)+" on "+min_rev_change_date)}
        

        return headers,results

def print_results(results_dictionary):
    # prints the dictionary in required format to CLI
    print("***********************")
    for title, value in results_dictionary.items():
        print(title+" : "+ str(value))
    print("***********************")

def write_to_file(input_file_name, headers, results_dictionary):
    # writes to an output file named results_"input_file_name", csv separated
    output_file_path = os.path.join("output",input_file_name)
    with open(output_file_path,"w") as csvfile:
        writer = csv.writer(csvfile)
        for key,value in results_dictionary.items():
            writer.writerow([key,value])




def main():

    # list of files to process, and column headers
    file_names = ["budget_data_1.csv","budget_data_2.csv"]
    date_column_header = "Date"
    revenue_column_header = "Revenue"
    

    # for each file get the tallied results and print
    for f in file_names:
        headers,results = tallyRevenues(f, date_column_header, revenue_column_header)
        #print_results(results)
        write_to_file(f,headers,results)



if __name__ == "__main__":
    main()