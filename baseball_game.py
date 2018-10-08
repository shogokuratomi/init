import random

class Pitcher:
    def __init__(self, controll, speed, flactu):
        self._controll = controll
        self._speed = speed
        self._flactu = flactu

    def throw(self):
        return self._controll + random.randint(-1*self._flactu, self._flactu)

    def pitch_power(self):
        return self._speed + random.randint(-1*self._flactu, self._flactu)
 
class Batter:
    def __init__(self, meet, power, flactu):
        self._meet = meet
        self._power = power
        self._flactu = flactu

    def swing(self):
        return self._meet + random.randint(-1*self._flactu, self._flactu)

    def batt_power(self):
        return self._power * 10 + random.randint(-1*self._flactu, self._flactu) * 100

class Game:
    def __init__(self, pitcher, batter):
        print('ゲーム開始')
        print('Enterを押すごとに１球投げます')
        input()
        self._out = 0
        q = 'None'
        innings = 1
        while (q != 'q') & ( innings < 19 ):
            print(self.get_innings(innings))
            self._out = 0
            self.start()
            self.battle_main(pitcher, batter)
            q = str(input('{}が終了。ゲーム終了するにはq+Enter:'.format(self.get_innings(innings))))
            print('==============================================================================')
            innings += 1
        print('ゲーム終了')
    
    def start(self):
        self._ball = 0
        self._strike = 0

    def get_innings(self, innings):
        if (innings % 2) != 0:
            return '{}回{}'.format((innings+1)//2, '表')
        else:
            return '{}回{}'.format((innings+1)//2, '裏')
        
    def battle_main(self, pitcher, batter):
        while self.change_judgement():
            n = 1        
            while self.out_judgement():
                count = self.count()
                print(count)
                print('          {}球目投げた!'.format(n))
                if self.hantei(pitcher, batter)=='Hit!':
                    self.start()
                    break
                n+=1
            print('     *********************************************')
            self.start()
    
    def count(self):
        ballcount   = 'ball  : {}'.format(str('*')*self._ball)
        strikecount = 'strike: {}'.format(str('*')*self._strike)
        outcount    = 'out   : {}'.format(str('*')*self._out)
        count = '\n'.join([ballcount, strikecount, outcount])
        return count

    def change_judgement(self):
        if self._out >= 3:
            print('          CHANGE!')
            return False
        else:
            return True
                            
    def out_judgement(self):
        if (self._strike >= 3):
            print('          Batter Out!')
            self._out += 1
            return False
        elif (self._ball >= 4):
            print('          Four Ball!')
            return False
        return True
    
    def hantei(self, pitcher, batter):
        if pitcher.throw() <= batter.swing():
            if pitcher.pitch_power() <= batter.batt_power():
                print('          @@@@@ HOME RUN !!! @@@@@')
            else:
                print('          Hit!')
            return 'Hit!'            
        elif pitcher.throw() > 5:
            print('          Strike!')
            self._strike += 1
        else:
            print('          Ball!')
            self._ball += 1

if __name__ == "__main__":
    pitcher_otani = Pitcher(controll=10, speed=160, flactu=5)
    batter_otani = Batter(meet=2, power=8, flactu=5)
    Game(pitcher_otani, batter_otani)
