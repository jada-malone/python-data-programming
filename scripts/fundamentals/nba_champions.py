# PROGRAM: NBA Champions Checker
# PURPOSE: Check if a favorite NBA team has won any championships and list the years
# INPUT: Favorite NBA team
# PROCESS: Read data from file and check for the team's championships
# OUTPUT: Number of championships and years won, or a message if none
# HONOR CODE: On my honor, as an Aggie, I have neither given nor received unauthorized aid on this academic work.

def read_nba_champions(file_path):
    """
    Reads the NBA champions data file and returns a dictionary with team names as keys
    and a list of years they won as values.
    """
    nba_champions = {}
    with open(file_path, 'r') as file:
        for line in file:
            year,team = line.strip().split(',')
            if team not in nba_champions:
                nba_champions[team] = []
            nba_champions[team].append(int(year))
    return nba_champions

def main():
    # Read the NBA champions data file
    file_path = "nba-champions.txt"
    nba_champions = read_nba_champions(file_path)

    # Ask the user for their favorite NBA team
    favorite_team = input("Enter your favorite NBA team: ")

    # Check if the team has won championships
    if favorite_team in nba_champions:
        championships = len(nba_champions[favorite_team])
        years = ', '.join(map(str, nba_champions[favorite_team]))
        print(f"{favorite_team} has won {championships} NBA championship(s) in the following years: {years}.")
    else:
        print(f"{favorite_team} has not won any NBA championships.")

if __name__ == "__main__":
    main()


