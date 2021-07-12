# Election_Analysis

## Overview of Election Audit
A Colorado Board of Elections employee has given the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total numbers of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based om popular vote.

## Resources
- Data Source_ election_results.csv
- Software: Python 3.8.8, Visual Studio Code 1.38.1

## Election Audit Results
The analysis of the election shows that:
### Candidate Results
- There were 369,711 votes cast in the election.
- The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
- The candidate results were:
    - Charles Casper Stockham received 23.0% of the vote and 85,213 votes.
    - Diana DeGette received 73.8% of the vote and 272,892 votes.
    - Raymon Anthony Doane received 3.1% of the vote and 11,606 votes.
- The winner of the election was:
      Diana DeGette, who received 73.8% of the vote and 272,892 votes.
### County Results
- The counties results were:
    - Jefferson: 10.5% (38,855)
    - Denver: 82.8% (306,055)
    - Arapahoe: 6.7% (24,801)
- They county with the lasrgest number of votes was:
      Denver with a total of 306,055 votes.

## Election Audit Summary: 
Proposal to the election comission: This script can be used for any election, regardless of how many candidates, counties or votes are registered. 
In the case that we have these 3 same variables, only a few adjustments would be needed, for example, we will probably need to change the names and paths to open our database file and to write in our txt file.
<img width="495" alt="Captura de Pantalla 2021-07-11 a la(s) 21 23 00" src="https://user-images.githubusercontent.com/85467925/125221782-a14e8880-e27d-11eb-97cb-675604b8cfb9.png">

Variables might be presented in different order in the database file, so the column number used in the first for loop might need to change, to refer to the correct object. Variable names in the code might be modified depending on what needs to be displayed. 
<img width="383" alt="Captura de Pantalla 2021-07-11 a la(s) 21 22 32" src="https://user-images.githubusercontent.com/85467925/125221890-d529ae00-e27d-11eb-99a8-646de032f918.png">

If other extra variables are included in the database, more code should be added to be able to analyse the extra variable, but previous code structure can be used as reference to do this. 
