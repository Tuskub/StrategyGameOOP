import re
from flask import render_template, flash, redirect
from app import app
from app.forms import ActionForm
from constants.gamemap import generate_map
from mainclass.map import Map
from control.game_control import GameControl

ground_list, unit_list = generate_map()
map = Map(ground_list, unit_list)
gc = GameControl(map)


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = ActionForm()
    winner = ''
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
        fp_all_alive, fp_all_dead, sp_all_alive, sp_all_dead = map.end_game()
        
        if (fp_all_dead or sp_all_dead) and (fp_all_alive or sp_all_alive):
            winner = 'Test'
            return render_template('base.html', map=map, form=form, winner=winner)
        
        if sp_all_dead:
            winner = 'Победил первый игрок!'
            return render_template('base.html', map=map, form=form, winner=winner)

        if fp_all_dead:
            winner = 'Победил второй игрок!'
            return render_template('base.html', map=map, form=form, winner=winner)

        return redirect('/')
    return render_template('base.html', map=map, form=form, winner=winner)


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
