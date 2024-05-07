# Timothy Rutkowski 04/19/2024 randomTeamsGenerator.py

# This program will take names from files separated by grade and randomly
# populate a number of teams selected by the user and display those teams. 
# The user can also choose to exclude names from being chosen for teams.

import random
import re

# Define global variables for file contents
grade4_5_names = []
grade2_3_names = []
gradeK_1_names = []

# Main function of the program
def main():
    open_and_read_files()
    excluded_names = get_excluded_names()
    num_teams = get_num_of_teams()
    teams = generate_teams(num_teams, excluded_names)
    display_teams(teams)

# Function to open, read, and store the names from the files
def open_and_read_files():
    global grade4_5_names, grade2_3_names, gradeK_1_names
    
    with open('grade4_5.txt', 'r') as grade4_5_file:
        grade4_5_names = [name.strip() for name in grade4_5_file.readlines()]
    print('\t4th and 5th Grade:')
    for name in grade4_5_names:
        print(name)
    
    with open('grade2_3.txt', 'r') as grade2_3_file:
        grade2_3_names = [name.strip() for name in grade2_3_file.readlines()]
    print('\n\t2nd and 3rd Grade:')
    for name in grade2_3_names:
        print(name)
    
    with open('gradeK_1.txt', 'r') as gradeK_1_file:
        gradeK_1_names = [name.strip() for name in gradeK_1_file.readlines()]
    print('\n\tKindergarten and 1st Grade:')
    for name in gradeK_1_names:
        print(name)
        
def normalize_name(name):
    # Remove leading and trailing whitespace, replace multiple spaces with a single space
    return re.sub(r'\s+', ' ', name.strip())

# Function to ask the user if they want any names excluded from being selected
# for teams and get those names
def get_excluded_names():
    excluded_names = []
    all_names = [normalize_name(name) for name in grade4_5_names + grade2_3_names + gradeK_1_names]
    
    while True:
        name = input('\nEnter a name you would like to exclude ' +
                     '(or press Enter to finish): ')
        if name.strip():
            # Normalize the entered name for comparison
            normalized_name = normalize_name(name)
            matches = [full_name for full_name in all_names if normalized_name.lower() in full_name.lower()]
            if matches:
                excluded_names.extend(matches)
                print(f"Excluded names matching '{name}':")
                for match in matches:
                    print(match)
            else:
                print(f"No names found matching '{name}'.")
        else:
            break  # Exit the loop if Enter is pressed
        
    return excluded_names

# Function to get the number of desired teams from the user    
def get_num_of_teams():
    num_teams = int(input('\nEnter the number of teams you want generated: '))
    return num_teams

# Function to randomly generate teams
def generate_teams(num_teams, excluded_names):
    global grade4_5_names, grade2_3_names, gradeK_1_names
    
    # Combine all names from different grades and remove unwanted characters
    all_names = [normalize_name(name) for name in grade4_5_names + 
                 grade2_3_names + gradeK_1_names]
    random.shuffle(all_names)
    
    # Filter out excluded names
    all_names = [name for name in all_names if name not in excluded_names]
    
    # Calculate the number of names per team
    num_names_per_team = len(all_names) // num_teams
    
    # Distribute names to teams
    teams = [all_names[i * num_names_per_team:(i + 1) * num_names_per_team] 
             for i in range(num_teams)]
    
    # Add any remaining names to teams
    remaining_names = all_names[num_teams * num_names_per_team:]
    for i in range(len(remaining_names)):
        teams[i % num_teams].append(remaining_names[i])
    
    return teams

# Function to display all the teams
def display_teams(teams):
    for i, team in enumerate(teams, 1):
        print(f'\n\tTeam {i}:')
        for name in team:
            print(name)
        print()  # Add an empty line after each team  

# Call the main function
if __name__ == '__main__':
    main()
