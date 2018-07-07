# Modules
import os
import csv
import collections

# file location
poll_csvpath = os.path.join("Resources", "election_data.csv")

# open and read file
with open(poll_csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # skip the first row/ header
    header=next(csvreader)

    #create empty list
    voter_list=[]
    county_list=[]
    candidate_list=[]
    count_voter=0
    
    for row in csvreader:
        voter=row[0]
        county=row[1]
        candidate=row[2]

        # calculate total vote
        count_voter+=1

        # add values/strings to empty list
        voter_list.append(voter)
        county_list.append(county)
        candidate_list.append(candidate)
    
     # this func sort out the name of candidate and how many time it occurs in the list.
    counter = collections.Counter(candidate_list)
    #print(counter)
    # The output --> Counter({'Khan': 2218231, 'Correy': 704200, 'Li': 492940, "O'Tooley": 105630})
    # using print above and know that there are 4 candidate names in the list.  So using
    # simple count to count each candidate has how many votes

    i=0
    Khan_vote_count=0
    correy_vote_count=0
    Li_vote_count=0
    Tooley_vote_count=0
    name1="Khan"
    name2="Correy"
    name3="Li"
    name4="O'Tooley"
    while i < len(candidate_list):
        if candidate_list[i] == name1:
            Khan_vote_count += 1
        if candidate_list[i] == name2:
            correy_vote_count += 1
        if candidate_list[i] == name3:
            Li_vote_count += 1
        if candidate_list[i] == name4:
            Tooley_vote_count += 1
        i += 1

    # Calculate % votes each candidate won
    Khan_percent=(Khan_vote_count/count_voter)*100
    round_khan=round(Khan_percent,3)
    Correy_percent=(correy_vote_count/count_voter)*100
    round_correy=round(Correy_percent,3)
    Li_percent=(Li_vote_count/count_voter)*100
    round_Li=round(Li_percent,3)
    Tooley_percent=(Tooley_vote_count/count_voter)*100
    round_tooley=round(Tooley_percent,3)

    # Find the winner of the election
    if (round_khan > round_correy) and (round_khan > round_Li) and (round_khan>round_tooley):
        winner=name1
    if (round_correy>round_khan) and (round_correy>round_Li) and (round_correy > round_tooley):
        winner=name2
    if (round_Li>round_khan) and (round_Li > round_correy) and (round_Li > round_tooley):
        winner= name3
    if (round_tooley > round_khan) and (round_tooley > round_correy) and (round_tooley > round_Li):
        winner = name4
    
    # OUTPUT PRINTS
    print("Election Results")
    print("---------------------------")
    print("Total Votes: ", count_voter)
    print("----------------------------")
    print(name1, ":", round_khan,"% (", Khan_vote_count, ")")
    print(name2,":",round_correy,"% (", correy_vote_count,")")
    print(name3,":", round_Li,"% (", Li_vote_count,")")
    print(name4,":", round_tooley,"% (", Tooley_vote_count,")")
    print("Winner: ", winner)

    # EXPORT TO TXT FILE
    import sys
    text_file=open("Election data analysis.txt","w")
    text_file.write("Election Results %s \n")
    text_file.write("------------------------ \n")
    text_file.write("Total Votes: %s \n" % count_voter)
    text_file.write(name1 )
    text_file.write(": %s" %round_khan)
    text_file.write(" percent, %s \n" %Khan_vote_count)
    text_file.write(name2)
    text_file.write(": %s" %round_correy)
    text_file.write(" percent, %s \n" % correy_vote_count)
    text_file.write(name3)
    text_file.write(": %s" %round_Li)
    text_file.write(" percent, %s \n" %Li_vote_count)
    text_file.write(name4)
    text_file.write(": %s" %round_tooley)
    text_file.write(" percent, %s \n" %Tooley_vote_count)
    text_file.write("Winner: %s \n" %winner)
    text_file.close()

