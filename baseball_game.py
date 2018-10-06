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
            print('{}球目投げた!'.format(n))
            thrown = self.nageta(ball)
            swing = self.hutta(batt)
            if thrown > swing:
                print('Strike!')
                self._strike += 1
                n+=1
            else:
                print('Hit!')
                break
                            
    def out_judgement(self):
        if self._strike >= 3:
            return False
        return True
    
    def nageta(self, ball):
        thrown = ball[0] + random.randint(-1*ball[2],ball[2])
        return thrown

    def hutta(self, batt):
        swing = batt[0] + random.randint(-1*batt[2], batt[2])
        return swing            

if __name__ == "__main__":
    pitcher_otani = Pitcher(controll=5, speed=160, flactu=5)
    batter_otani = Batter(meet=5, power=8, flactu=5)
    Game(pitcher_otani, batter_otani)
