from team import Team
from bench import Bench


""" Created by Zhuocai (Tsai) Li
https://github.ccs.neu.edu/CS-5001-SEA-Spring2021/student-ZhuocaiLi """

# The restrict of positions
POSITION_LIST = ["catcher", "sniper", "corner", "thrower"]


def main():
    print("Welcome to the team manager.")
    # Here's where we create objects for the team and the bench. These
    # objects will be able to call the methods we've defined in their
    # respective classes. When the constructor functions are called here,
    # the classes' __init__() method is called with these values
    # passed to it. In both of these cases no arguments are passed, here.
    # However, the `self` argument is always implicitly passed with any
    # method call.
    the_team = Team()
    the_bench = Bench()

    while True:
        # Immediately converting the input to lower() lets the user enter
        # any kind of capitalization, so it's a little less strict.
        command = (input("What do you want to do?\n")).lower()

        if command == "done":
            print("Shutting down team manager\n")
            return  # this return statement exits main, ending the session.
        elif command == "set team name":
            do_set_team_name(the_team)
        elif command == "show roster":
            do_show_team_roster(the_team)
        elif command == "add player":
            do_add_player_to_team(the_team)
        elif command == "check position is filled":
            do_check_position_filled(the_team)
        elif command == "send player to bench":
            do_send_player_to_bench(the_team, the_bench)
        elif command == "get player from bench":
            do_get_player_from_bench(the_bench)
            # TODO: call a function that calls
            # the appropriate method on the team
            # object to cut the player (you need
            # to write the function below)
        elif command == "cut player":
            do_cut_player(the_team, the_bench)
            pass
        elif command == "show bench":
            do_display_bench(the_bench)
            # TODO: call a function to call the necessary
            # bench method to show the names of the players
            # who are currently on the bench.
            pass
        else:
            do_not_understand()


def do_set_team_name(team):
    name = input("What do you want to name the team?\n")
    team.set_team_name(name)


def do_show_team_roster(team):
    # TODO: call the method on the team object that
    # displays the roster
    print(f"The lineup for {team.name} is:")
    if(len(team.players_list) > 0):
        # Show full roster only if there is at least one player in team
        team.show_roster()
    else:
        print("The team currently has no players")
    pass


def do_check_position_filled(team):
    position = input("What position are you checking for?\n")
    team.is_position_filled(position)
    # TODO: call the method on the team object that determines
    # whether a given position has at least one player filling it,
    # then print the appropriate message:
    # "Yes, the", position, "position is filled"
    # or
    # "No, the", position, "position is not filled"
    # Tsai: the function is built in class Team
    pass


def check_name(team, player_name):
    # Tsai: If the name of the player exists in the team,
    # This program would give out information that
    # the player is already in the team,
    # and ask user to give another name
    for player in team.players_list:
        if(player_name == player.name):
            player_name = input("This player is already in the team\n" +
                                "Please enter a new player\n")
    return player_name


def check_number(team, player_number):
    # Tsai: the player number input would have several restictions:
    # 1. should be a number;
    # 2. should only be a positive integer;
    # 3. should only include no more than 2 digits,
    # since for player numbers of most sports,
    # seldom 3-or-more digits are seen;
    # 4. two differenr players should ;
    # not share the same number
    # Any restricition violated,
    # user will be asked to resubmit a new number
    while True:
        if((player_number.isdigit() is False)
           or (int(player_number) < 0)
           or (len(player_number) > 2)):
            # Restriction 1, 2, 3
            player_number = input("Please enter an 2-digit positive integer\n")
        elif (len([True for player in team.players_list
                   if player_number == player.number]) > 0):
            # Restricition 4
            player_number = input("This number is used in the team\n" +
                                  "Please enter a new number\n")
        else:
            return player_number


def check_position(team, player_position):
    # Tsai: position of this game (dodgeball),
    # can only include the 4 positions.
    # If anything else is input,
    # user will be asked to resubmit a correct position
    while(player_position not in POSITION_LIST):
        player_position = input("Please enter a correct position\n")
    return player_position


def do_add_player_to_team(team):
    # Add player function
    player_name = input("What's the player's name?\n")
    player_name = check_name(team, player_name)

    player_number = input("What's " + player_name + "'s number?\n")
    player_number = check_number(team, player_number)

    player_position = input("What's " + player_name + "'s position?\n")
    player_position = check_position(team, player_position)

    # TODO: call the method on team that creates a new player and
    # adds the player to the team.
    team.add_player(player_name, player_number, player_position)
    print("Added", player_name, "to", team.name)


def do_cut_player(team, bench):
    # Cut player from the team with 3 restrictions:
    # 1. at least 1 player should be in team;
    # 2. player to-be-cut should be in the team;
    # 3. he/she should not be on bench
    if(len(team.players_list) == 0):
        print("There is no player in team")
        return
    name = input("Who do you want to cut?\n")
    if check_bench(name, bench):
        print(f"{name} cannot be cut, since he/she is on bench.")
    elif check_player_in_team(name, team) is False:
        print(f"{name} isn't on the team.")
    else:
        team.cut_player(name)


def do_send_player_to_bench(team, bench):
    # Send player to bench with 3 restrictions:
    # 1. at least 1 player should be in team;
    # 2. he/she should not already be on bench;
    # 3. he/she should be in team;
    if(len(team.players_list) == 0):
        print("There is no player in team")
        return
    name = input("Who do you want to send to the bench?\n")
    if check_bench(name, bench):
        print(f"{name} is already on bench.")
    elif check_player_in_team(name, team) is False:
        print(f"{name} isn't on the team.")
    else:
        bench.send_to_bench(name)
        print(f"Sent {name} to bench")


def check_bench(name, bench):
    # check if a player is on bench
    # supporting do-cut-player and
    # do_send_player_to_bench function
    for bench_player in bench.bench_list:
        if name == bench_player:
            return True
    return False


def check_player_in_team(name, team):
    # check if a player is in team
    # supporting do-cut-player and
    # do_send_player_to_bench function
    for player in team.players_list:
        if name == player.name:
            return True
    return False


def do_get_player_from_bench(bench):
    # Tsai: this function constucted in class Bench,
    # different from function do_display_bench as below.
    # Giving two different ideas of constructing functions
    # Not sure which one would be better
    bench.get_from_bench()
    # TODO: get the best-rested player by name from the bench
    # (i.e. the player who has been on the bench longest). Print to
    # the screen the name of the player who was retrieved from the
    # bench. If the bench is empty, print to the screen that the
    # bench is empty.
    pass


# TODO: write a function that calls the appropriate method on the team
# object to cut the player

def do_display_bench(bench):
    # Tsai: this function is to display bench
    # give out certain information when bench is empty
    if(len(bench.bench_list) == 0):
        print("The bench is empty.")
    else:
        for player in bench.bench_list:
            print(player)
# TODO: write a function to call the necessary method to show the
# names of the players who are currently on the bench.


def do_not_understand():
    print("I didn't understand that command")


main()
