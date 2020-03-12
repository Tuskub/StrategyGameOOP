import re
from flask import render_template, flash, redirect
from app import app
from app.forms import ActionForm
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
    Archer(2, 1, 2),
    Catapult(1, 3, 1),
    Horseman(3, 2, 1),
    Swordsman(3, 3, 1)
]

map = Map(ground_list, unit_list)
gc = GameControl(map)


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = ActionForm()
    if form.validate_on_submit():
        nums = re.findall(r'\d{1,2}', form.unit.data)
        selected_x = int(nums[0])
        selected_y = int(nums[1])

        nums = re.findall(r'\d{1,2}', form.target.data)
        target_x = int(nums[0])
        target_y = int(nums[1])

        switch = {
            'move': move,
            'attack': attack
        }
        func = switch.get(form.action.data)
        func(selected_x, selected_y, target_x, target_y)
        return redirect('/')
    return render_template('index.html', title='Home', map=map, form=form)


def move(selected_x, selected_y, target_x, target_y):
    unit = map.get_unit_by_point(selected_x, selected_y)
    if unit is None:
        flash('В ячейке нет юнита')
        return
    gc.move_unit(unit, target_x, target_y)
    return


def attack(selected_x, selected_y, target_x, target_y):
    unit = map.get_unit_by_point(selected_x, selected_y)
    target = map.get_unit_by_point(target_x, target_y)
    if unit is None or target is None:
        flash('В ячейке нет юнита')
        return
    gc.attack_unit(unit, target)
    return
