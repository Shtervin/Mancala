class GameState:
    def __init__(self, a=6, b=4):
       
        self.init_num_pits = a
        self.init_stone = b
        self.pits_num = self.init_num_pits
        self.store_score = [0, 0]
        self.pits_player1 = {k: self.init_stone for k in range(1, self.pits_num + 1)}
        self.pits_player2 = {k: self.init_stone for k in range(1, self.pits_num + 1)}

    def board(self):
        
        board_set = "\t    "
        for i in range(self.pits_num, 0, -1):
            board_set += "   " + str(i) + "   "
        board_set += "\n"
        
        # board_set = "\t\t\t\t6\t\t5\t 4\t 3\t 2\t 1\n"
        board_set += "\t   -------------------------------------------\n"
        board_set += "   " + str(self.store_score[1]).zfill(2) + "      |  "
        for i in range(len(self.pits_player2) - 1, -1, -1):
            board_set += str(self.pits_player2[i + 1]).zfill(2) + "  |  "
        board_set += "(PLAYER 2)\n"
        board_set += "--------------------------------------------------------------------\n"
        board_set += "(PLAYER 1) |  "
        for i in range(0, len(self.pits_player1)):
            board_set += str(self.pits_player1[i + 1]).zfill(2) + "  |  "
        board_set += "   " + str(self.store_score[0]).zfill(2)
        board_set += "\n"
        board_set += "\t   -------------------------------------------\n"
        board_set += "\t    "
        for i in range(self.pits_num):
            board_set += "   " + str(i + 1) + "   "
        return board_set

    def reset(self, a=6, b=4):
        self.init_num_pits = a
        self.init_stone = b
        self.pits_num = self.init_num_pits
        self.store_score = [0, 0]
        self.pits_player1 = {k: self.init_stone for k in range(1, self.pits_num + 1)}
        self.pits_player2 = {k: self.init_stone for k in range(1, self.pits_num + 1)}

    def possible_actions(self, player):
       
        if player.player_num == 1:
            pits = self.pits_player1
        else:
            pits = self.pits_player2
        actions = {}
        for (npits, stones) in pits.items():
           
            if stones != 0:
                actions[npits] = stones
        return actions

    def make_move(self, player, npits):
           
            if player.player_num == 1:
                pits = self.pits_player1
                opp_pits = self.pits_player2
            else:
                pits = self.pits_player2
                opp_pits = self.pits_player1
            stones = pits[npits]
            score = self.store_score
           
            pits[npits] = 0
           
            npits += 1
            temp = pits
            turn = 1
           
            while stones > 0:
                turn = 1
                while npits <= len(pits) and stones > 0:
                    pits[npits] += 1
                    npits += 1
                    stones -= 1
                if stones == 0:  
                    if pits[npits - 1] == 1:
                        if opp_pits[7 - (npits - 1)] != 0:
                            score[player.player_num - 1] += 1 + opp_pits[7 - (npits - 1)]
                            pits[npits - 1] = 0
                            opp_pits[7 - (npits - 1)] = 0
                    break
                
                if pits == temp:
                   
                    score[player.player_num - 1] += 1
                    stones -= 1
                    turn = 0
                   
                other_temp = pits
                pits = opp_pits
                opp_pits = other_temp
                npits = 1
            return self.pits_player1, self.pits_player2, self.store_score, turn

    def terminal(self):
        
        over1 = False
        over2 = False
        if all(value == 0 for value in self.pits_player1.values()):
            self.store_score[1] += sum(self.pits_player2.values())
            self.pits_player2 = self.pits_player1
            over1 = True
        if all(value == 0 for value in self.pits_player2.values()):
            self.store_score[0] += sum(self.pits_player1.values())
            self.pits_player1 = self.pits_player2
            over2 = True
        if over1 or over2:
            return True
        else:
            return False

    def result(self, player_num):
        
        opp_num = 3 - player_num
        if self.terminal():
            return self.store_score[player_num - 1] > self.store_score[opp_num - 1]
        else:
            return False

    def evaluate(self, player):
       
        if player.player_num == 1:
            return self.store_score[0] - self.store_score[1]
        elif player.player_num == 2:
            return self.store_score[1] - self.store_score[0]