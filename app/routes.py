from flask import render_template
from app import app
from units.range.archer import Archer
from units.range.catapult import Catapult
from units.melee.horseman import Horseman
from units.melee.swordsman import Swordsman
from grounds.playable.grass import Grass
from grounds.unplayable.water import Water
from mainclass.map import Map
from control.game_control import GameControl

ground_list = [
    Water(1, 1,),
    Water(1, 2,),
    Grass(1, 3,),
    Grass(2, 1,),
    Grass(2, 2,),
    Water(2, 3,),
    Grass(3, 1,),
    Grass(3, 2,),
    Grass(3, 3,)
]

unit_list = [
    Archer(2, 1, 1),
    Catapult(1, 3, 1),
    Horseman(3, 2, 1),
    Swordsman(3, 3, 1)
]

map = Map(ground_list, unit_list)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home', map=map)
