''' 
Roulette game.

Badea Adrian Catalin


A roulette wheel consists of a spinning disk with divisions around its edge that revolves around the base of a bowl. 

A ball is spun around the outside of the bowl until eventually ball and wheel come to rest with the ball in one of the divisions.

The divisions around the wheel are numbered from 1 to 36 in a seemingly random pattern and alternate red and black. 

Additionally, there is a green division numbered 0. 

On American tables only there is a second extra green division marked 00 and it is largely this that makes the American version of Roulette a worse proposition financially than the European game.

Prior to rolling the ball, people place bets on what number will come up by laying down chips on a betting mat, the precise location of the chips indicating the bet being made. 


https://www.mastersofgames.com/rules/roulette-rules.htm


'''

import random


import matplotlib.pyplot as plt
import matplotlib as mpl


class Roulette:
    
    '''
        The Roulette class will be instantiated with a number of ball spins.
        
        Types of bets:
            Red / Rouge: a red number
            Black / Noir: a black number
            Even / Pair: an even number
            Odd / Impair: an odd number
            Low bet / Manque: numbers 1 - 18 (Manque is French for "failed" and is used because the ball has failed to pass 18)
            High bet / Passe: numbers 19 - 36 (Passe is so named because it has "passed" the centrepoint)
    
        
    '''
    
    def __init__(self, nr_iter : int = 100000):
        
        self._min = 0
        self._max = 36
        
        
        self.rouge = [1, 3, 5, 7 , 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
        
        self.games = []
        self.nr_iter = nr_iter
        
        for i in range(nr_iter):
            self._spin_ball()
    
    def _spin_ball(self):
        
        number = random.randint(self._min, self._max);
        self.games.append(number)
        
    
    def impair_bet(self):
        
        impair_list = filter(lambda number : number % 2 == 1, self.games);
        return len(list(impair_list))
    
    def pair_bet(self):
        
        return len(self.games) - self.impair_bet() - self.zeros()
    
    def rouge_bet(self):
        
        rouge_list = filter(lambda number : number in self.rouge, self.games)
        return len(list(rouge_list))
    
    def noir_bet(self):
        return len(self.games) - self.rouge_bet() - self.zeros()
    
    
    def zeros(self):
        
        zero_list = filter(lambda number : number == 0, self.games)
        return len(list(zero_list))
    
    def manque_bet(self):
        
        manque_list = filter(lambda number : 1<= number and number <= 18, self.games)
        return len(list(manque_list))
        
    def passe_bet(self):
        return len(self.games) - self.manque_bet()- self.zeros()
    
    
    def printer(self, name, good_spins, procent):
        print("Number of {} spins: {}, with procentage {}".format(name, good_spins, procent))
        
    
    def statistics(self):
        
        
        print("Roullete game. Ball spun for {} iterations".format(self.nr_iter))
        
        impair = self.impair_bet()
        impair_procent = impair / self.nr_iter
        
        self.printer('odd', impair, impair_procent)
        
        pair = self.pair_bet()
        pair_procent = pair / self.nr_iter
        
        self.printer('pair', pair, pair_procent)
        
        
        rouge = self.rouge_bet()
        rouge_procent = rouge / self.nr_iter
        self.printer('red', rouge, rouge_procent)
        
        noir = self.noir_bet()
        noir_procent = noir / self.nr_iter
        self.printer('black', noir, noir_procent)
        
        manque = self.manque_bet()
        manque_procent = manque / self.nr_iter
        self.printer('low', manque, manque_procent)
        
        passe = self.passe_bet()
        passe_procent = passe / self.nr_iter
        self.printer('high', passe, passe_procent)
        
        print("Number of zero - green spins: {}".format(self.zeros()))
        print("The plot calculates return of bet based on bet type.")
        
        mpl.style.use('seaborn')
    
        plt.suptitle('European Roulette game. Return based on bet type')
        
        plt.xlabel('Type of bet')
        
        plt.ylabel('Return of bet')
        
        
        plt.scatter('non-zero spins', ((self.nr_iter - 0.5 * self.zeros()) / self.nr_iter))
        
        plt.scatter('odd', impair_procent * 2)
        plt.scatter('pair', pair_procent * 2)
        plt.scatter('rouge', rouge_procent * 2)
        plt.scatter('noir', noir_procent * 2)
        plt.scatter('manque', manque_procent * 2)
        plt.scatter('passe', passe_procent * 2)
        
        
        
        plt.legend()
        
        plt.savefig("Roulette_bet_return_type.png")
        plt.show()
    
    

if __name__ == "__main__":
    
    roulette = Roulette(100)
    roulette.statistics()
    
        
        
    
    
    
    
    
    
        