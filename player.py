import math
import copy
import random
import sys


class Player:
    player_dict = {0: 'human', 1: 'random', 2: 'minimax', 3: 'alphabeta'}

    def __init__(self, player_num, player_type):
       
        self.player_num = player_num
        self.opp_num = 3 - player_num
        self.type = player_type

    def __repr__(self):
       
        return 'PLAYER {} {} is playing'.format(self.player_num, self.player_dict[self.type])

    def choose_move(self, gamestate):
       
        if self.player_dict[self.type] == 'human':
            move = self.human_decision(gamestate)
            return move
        elif self.player_dict[self.type] == 'random':
            move = self.random_decision(gamestate)
            return move
        elif self.player_dict[self.type] == 'minimax':
            move = self.minimax_decision(gamestate)
            return move
        elif self.player_dict[self.type] == 'alphabeta':
            move = self.alphabeta_decision(gamestate)
            return move
        else:
            print('invalid player')
            return -1

    def human_decision(self, gamestate):
        move = int(input('Please enter your move:\n'))
        while move not in gamestate.possible_actions(self):
            sys.stderr.write('illegal move\n')
            move = int(input('Please enter your move:\n'))
        return move

    def random_decision(self, gamestate):
        d = gamestate.possible_actions(self)
        move = random.choice(list(d.keys()))
        return move

    def minimax_decision(self, gamestate, depth=5):
        #Decides which move to make from min and maxvalue
       
        move = -1
        score = -math.inf
        for npits in gamestate.possible_actions(self):
            state_temp = copy.deepcopy(gamestate)
            
            state_temp.make_move
            opp = Player(self.opp_num, self.type)
           
            s = opp.minvalue(state_temp, depth - 1)
           
            if s > score:
                move = npits
                score = s
            if s == score:
                move = random.choice([move, npits])
                score = s
        return move

    def maxvalue(self, gamestate, depth):
        #functions as the maximizing player
       
        if gamestate.terminal() or depth == 0:
            return gamestate.evaluate(self)
        score = -math.inf
        for npits in gamestate.possible_actions(self):
            state_temp = copy.deepcopy(gamestate)
            
            state_temp.make_move
            opp = Player(self.opp_num, self.type)
            s = opp.minvalue(state_temp, depth - 1)
            if s > score:
                score = s
        return score

    def minvalue(self, gamestate, depth):
        #functions as the minimizing player
       
        if gamestate.terminal() or depth == 0:
            return gamestate.evaluate(self)
        score = math.inf
        for npits in gamestate.possible_actions(self):
            state_temp = copy.deepcopy(gamestate)
            
            state_temp.make_move
            opp = Player(self.opp_num, self.type)
            s = opp.maxvalue(state_temp, depth - 1)
            if s < score:
                score = s
        return score

    def alphabeta_decision(self, gamestate, depth=5):
        #takes in the value from the alpha and beta and decides which pruning to do
        
        move = -1
        alpha = -math.inf
        beta = math.inf
        score = -math.inf
        for npits in gamestate.possible_actions(self):
            state_temp = copy.deepcopy(gamestate)
           
            state_temp.make_move
            opp = Player(self.opp_num, self.type)
            s = opp.minab(state_temp, alpha, beta, depth - 1)
            
            if s > score:
                move = npits
                score = s
            if s == score:
                move = random.choice([move, npits])
                score = s
            alpha = max(score, alpha)
        return move

    def maxab(self, gamestate, alpha, beta, depth):
        #calculates the alpha/max value in alpha beta
       
        if gamestate.terminal() or depth == 0:
            return gamestate.evaluate(self)
        score = - math.inf
        for npits in gamestate.possible_actions(self):
            state_temp = copy.deepcopy(gamestate)
            
            state_temp.make_move
            opp = Player(self.opp_num, self.type)
           
            s = max(score, opp.minab(state_temp, alpha, beta, depth - 1))
           
            if s >= beta:
                alpha = s
                return alpha
            alpha = max(alpha, s)
        return alpha

    def minab(self, gamestate, alpha, beta, depth):
       #calculates the beta / min value in alpha beta
        if gamestate.terminal() or depth == 0:
            return gamestate.evaluate(self)
        score = math.inf
        for npits in gamestate.possible_actions(self):
            state_temp = copy.deepcopy(gamestate)
           
            state_temp.make_move
            opp = Player(self.opp_num, self.type)
            
            s = min(score, opp.maxab(state_temp, alpha, beta, depth - 1))
           
            if s <= alpha:
                beta = s
                return beta
            beta = min(beta, s)
        return beta