import matplotlib.pyplot as plt
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('プログラム開始')

class Ball:
    def __init__(self, x, y, dia, weight, init_vel):
        self._x = x
        self._y = y
        self._diameter = dia
        self._weight = weight
        self._velocity = init_vel
        logging.debug('Ballインスタンスを作成しました!')

    def is_on_surface(self):
        if self._y <= 0:
            return True
        return False

    def calculation(self, planet, time_delta):
        dv_dt = (( (self._weight*planet._gravity) - (planet._resist*self._diameter*self._velocity**2) ) / self._weight)
        new_x = self._x
        new_v = self._velocity - ( dv_dt * time_delta)
        new_y = self._y + new_v  * time_delta
        return new_x, new_y, new_v

    def update_position(self, new_x, new_y, new_v):
        self._x = new_x
        self._y = new_y
        self._velocity = new_v

class Planet:
    def __init__(self, name):
        gravity_list = {"Earth":9.81, "moon":1.62, "jupyter":23}
        resist_list = {"Earth":0.02, "moon":0, "jupyter":0}    
        self._name = name
        self._gravity = gravity_list[name]
        self._resist = resist_list[name]
        logging.debug('Planetインスタンスを作成しました!')

class Result:
    def __init__(self, ball):
        self.name = str(ball)  
        self.tcount = 0
        self.tresult = [self.tcount]
        self.xresult = [ball._x]
        self.yresult = [ball._y]
        self.vresult = [ball._velocity]
        logging.debug('Resultに初期値を記録しました!')
    
    def storage(self, time_delta, new_x, new_y, new_v):
        self.tcount += time_delta
        self.tresult.append(self.tcount)
        self.xresult.append(new_x)
        self.yresult.append(new_y)
        self.vresult.append(new_v)

def graph_plot(result):    
    plt.plot(result.tresult,result.yresult, label='y')
    plt.legend()

def ball_falling(ball, planet, time_delta, result):
    while True:
        x, y, v = ball.calculation(planet, time_delta)
        ball.update_position(x, y, v)
        if not ball.is_on_surface():
#            logging.debug('calculation実行しました。v={:.2f}, y={:.2f}'.format(v, y))
            result.storage(time_delta, x, y, v)
            pass
        else:
            logging.debug('地面に到達しました')
            break

if __name__ == "__main__":
    ball = Ball(x=1, y=10, dia=1, weight=1, init_vel=0.0)   #直径が小さく重量も重いball
    earth = Planet("Earth")
    result1 = Result(ball)
    ball_falling(ball, earth, 0.01, result1)
    graph_plot(result1)

    cotton = Ball(x=1, y=10, dia=100, weight=0.1, init_vel=0.0)  #直径が大きく重量が軽いcotton
    earth = Planet("Earth")
    result2 = Result(cotton)
    ball_falling(cotton, earth, 0.01, result2)
    graph_plot(result2)
    
    plt.show()