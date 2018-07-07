# Modules
import os
import csv

# file location
budget_csvpath = os.path.join("Resources", "budget_data.csv")

# open and read file
with open(budget_csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # skip the first row/ header
    header=next(csvreader)
    
    #create empty list
    month_list=[]
    profit_loss_list=[]
    change_btwn_months=[]
    count_month=0
    net=0

    for row in csvreader:
        #print(row[1])
        date=row[0]
        profit_loss=row[1]

        # calculate net (total profit+loss)
        net=net+int(row[1])
        #calculate total number of months
        count_month+=1

        month_list.append(date)
        profit_loss_list.append(profit_loss)
        #print(profit_loss_list)
    i=0
    total_change=0
    while i < len(profit_loss_list)-1:
        changes= int(profit_loss_list[i+1])-int(profit_loss_list[i])
        change_btwn_months.append(changes)
        total_change += changes
        i += 1
        # Average change in Profit/Losses btwn months over entire period
        Average_change=int(total_change)/int(len(profit_loss_list)-1)
        #round number to 2 decimal point
        avg_round=round(Average_change,2)
        
    # find max/min of array (profits)
    greatest_increase=max(change_btwn_months)
    greatest_decrease=min(change_btwn_months)

    # find index value correspond to max/min of profit changes
    greatest_inc_index=change_btwn_months.index(greatest_increase)
    greatest_dec_index=change_btwn_months.index(greatest_decrease)
    #print(greatest_dec_index)

    # Find month correspond to greatest changes in profit
    greatest_inc_month=month_list[greatest_inc_index+1]
    greatest_dec_month=month_list[greatest_dec_index+1]
    #print(greatest_dec_month)

    #PRINT to terminal 
    print(f"Financial Analysis")
    print(f" ---------------------------")
    print("Total Months: ", count_month)
    print("Total: $",net )
    print("Average Change: $", round(Average_change,2))
    print("Greatest Increase in Profits: ", greatest_inc_month, "($", greatest_increase, ")")
    print("Greatest Decrease in Profits: ", greatest_dec_month, " ($", greatest_decrease, ")")

    # export to text file
    import sys
    text_file=open("Financial Analysis.txt","w")
    text_file.write("Financial Analysis %s \n")
    text_file.write("------------------------ \n")
    text_file.write("Total months: %s \n" % count_month)
    text_file.write("Total: $ %s \n" % net)
    text_file.write("Average Change: $ %s \n" %'{:.2f}'.format(Average_change))
    text_file.write("Greatest Increase in Profits: $ %s \n" %greatest_increase)
    text_file.write("Date for greatest increase in Profits: %s \n" %greatest_inc_month)
    text_file.write("Greatest Decrease in Profits: $ %s \n" %greatest_decrease)
    text_file.write("Date for greatest decrease in Profits: %s \n" %greatest_dec_month)
        
    text_file.close()
