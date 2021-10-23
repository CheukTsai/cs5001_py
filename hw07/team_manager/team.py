from player import Player
import re

""" Created by Zhuocai (Tsai) Li
https://github.ccs.neu.edu/CS-5001-SEA-Spring2021/student-ZhuocaiLi """


class Team:
    """A class representing a dodgeball team"""
    # All methods in Python include arguments representing the object
    # itself. In the method definition, this is represented by the
    # `self` parameter.

    def __init__(self):
        self.name = "Anonymous Team"
        self.players_list = []

    # Another example of self. The method call only passes one argument,
    # the 'name; value. But the method definition must always include the
    # self parameter.

    def set_team_name(self, name):
        # TODO: set the team name
        # Tsai: if using \W, there will still be "_" included,
        # delete it
        for char in name:
            if((re.match(r"\W", char) or char == "_") and char != " "):
                print("Team name should not include special symbols")
                return
        self.name = name
        pass

    # Note again that `self` is the first parameter.
    def add_player(self, player_name, player_number, player_position):
        # TODO: call the Player class constructor with the appropriate
        # values to create a new player object, then add that
        # player object to the team's players list.
        player = Player(player_name, player_number, player_position)
        self.players_list.append(player)
        pass

    def cut_player(self, player_name):
        # TODO: Remove the player with the name player_name
        # from the players list.
        for player in self.players_list:
            if player_name == player.name:
                self.players_list.remove(player)
                return  # stop immediately when the player is found
        pass

    def is_position_filled(self, position):
        # check if a position is input
        for player in self.players_list:
            if(position == player.position):
                print("the", position, "position is filled")
                return
        print("No, the", position, "position is not filled")

        # TODO: Write the method that checks whether
        # there is currently at least one player on the team
        # occupying the requested position

    # TODO: Write any necessary methods to support the methods
    # above, and write the method that will display (print to screen)
    # the full team roster in the following format:

    #    The lineup for Seattle Scorpions is:
    #    15       Garcia          catcher
    #    55       Wiggins         corner
    #    99       McCann          sniper

    def show_roster(self):
        # Class player has been override with __str__
        # Print player directly
        for player in self.players_list:
            print(player)
        pass
