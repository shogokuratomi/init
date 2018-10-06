import random

class Pitcher:
    def __init__(self, controll, speed, flactu):
        self._tama = [controll, speed, flactu]

class Batter:
    def __init__(self, meet, power, flactu):
        self._batt = [meet, power, flactu]

class Game:
    def __init__(self, pitcher, batter):
        print('ゲーム開始')
        print('Enterを押すごとに１球投げます')
        input()
        self.start()
        self.battle_main(pitcher, batter)
        print('ゲーム終了')
    
    def start(self):
        self._ball = 0
        self._strike = 0
        self._out = 0

    def battle_main(self, pitcher, batter):
        ball = pitcher._tama
        batt = batter._batt
        n = 1
        while self.out_judgement():
            count = self.count()
            print(count)
            print('          {}球目投げた!'.format(n))
            thrown = self.nageta(ball)
            swing = self.hutta(batt)
            if self.hantei(thrown, swing)=='Hit!':
                break
            n+=1
    
    def count(self):
        ballcount = 'ball  : ' + str('*')*self._ball
        strikecount = 'strike: ' + str('*')*self._strike
        outcount = 'out   : ' + str('*')*self._out
        count = '\n'.join([ballcount, strikecount, outcount])
        return count
                            
    def out_judgement(self):
        if (self._strike >= 3):
            print('          Batter Out!')
            print('          Pitcherの勝ち!')
            return False
        elif (self._ball >= 4):
            print('          Four Ball!')
            print('          Batterの勝ち!')
            return False
        return True
    
    def nageta(self, ball):
        thrown = ball[0] + random.randint(-1*ball[2],ball[2])
        return thrown

    def hutta(self, batt):
        swing = batt[0] + random.randint(-1*batt[2], batt[2])
        return swing

    def hantei(self, thrown, swing):
        if thrown > swing:
            if thrown > 5:
                print('          Strike!')
                self._strike += 1
            else:
                print('          Ball!')
                self._ball += 1
        else:
            print('          Hit!')
            print('          Batterの勝ち!')
            return 'Hit!'

if __name__ == "__main__":
    pitcher_otani = Pitcher(controll=5, speed=160, flactu=5)
    batter_otani = Batter(meet=2, power=8, flactu=5)
    Game(pitcher_otani, batter_otani)