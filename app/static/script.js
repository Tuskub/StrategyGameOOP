let past_unit = {
  background: null,
  coordinates: null
}
let past_target = {
  background: null,
  coordinates: null
}
var event = new MouseEvent('mouseout', {
  'view': window,
  'bubbles': true,
  'cancelable': true
});

function list_click(unit) {
  return function (e) {
    let selected = document.getElementById('unit');
    selected.value = unit.dataset.coordinates;
    for (let j = 0; j < player_two_units.children.length; j++) {
      player_two_units.children[j].dispatchEvent(event);
    };
    for (let j = 0; j < player_one_units.children.length; j++) {
      player_one_units.children[j].dispatchEvent(event);
    };
    document.querySelector(`div[data-coordinates="${unit.dataset.coordinates}"]`).style.borderColor = 'yellow';
    unit.style.backgroundImage = 'url(/static/img/textures/StoneB.png)'
  }
}

function list_mouseover(unit) {
  return function (e) {
    if (document.getElementById('unit').value == unit.dataset.coordinates) {
      return;
    }
    let selected = document.querySelector(`div[data-coordinates="${unit.dataset.coordinates}"]`);
    selected.style.backgroundImage = 'url(/static/img/textures/GrassB.png)';
    unit.style.backgroundImage = 'url(/static/img/textures/StoneA.png)';
  }
}

function list_mouseout(unit){
  return function(e) {
    if (document.getElementById('unit').value == unit.dataset.coordinates) {
      return;
    }
    let selected = document.querySelector(`div[data-coordinates="${unit.dataset.coordinates}"]`);
    selected.style.backgroundImage = 'url(/static/img/textures/GrassA.png)';
    selected.style.borderColor = 'black'
    unit.style.backgroundImage = null;
  }
}

player_one_units = document.getElementById('playerone_units');
player_two_units = document.getElementById('playertwo_units');
document.getElementById('unit').addEventListener('input', function (e) {
  if (!(/\d{1,2}\s\d{1,2}/).test(this.value) || past_target.coordinates == this.value)
    return;
  let past_cell = document.querySelector(`div[data-coordinates="${past_unit.coordinates}"]`)
  if (past_cell != null) {
    past_cell.style.backgroundImage = `${past_unit.background}`;
  }
  const grid = document.getElementById('grid')
  let unit = document.querySelector(`div[data-coordinates="${this.value}"]`)
  past_unit.background = unit.style.backgroundImage
  unit.style.backgroundImage = 'url(/static/img/textures/GrassB.png)';
  past_unit.coordinates = this.value;
});

document.getElementById('target').addEventListener('input', function (e) {
  if (!(/\d{1,2}\s\d{1,2}/).test(this.value) || past_unit.coordinates == this.value)
    return;
  let past_cell = document.querySelector(`div[data-coordinates="${past_target.coordinates}"]`)
  if (past_cell != null) {
    past_cell.style.backgroundImage = `${past_target.background}`;
  }
  const grid = document.getElementById('grid')
  let target = document.querySelector(`div[data-coordinates="${this.value}"]`)
  past_target.background = target.style.backgroundImage
  target.style.backgroundImage = 'url(/static/img/textures/GrassB.png)';
  past_target.coordinates = this.value;
});

for (let i = 0; i < player_one_units.children.length; i++) {
  let unit = player_one_units.children[i];
  unit.addEventListener('mouseover', list_mouseover(unit));
  unit.addEventListener('mouseout', list_mouseout(unit));
  unit.addEventListener('click', list_click(unit));
};

for (let i = 0; i < player_two_units.children.length; i++) {
  let unit = player_two_units.children[i];
  unit.addEventListener('mouseover', list_mouseover(unit));
  unit.addEventListener('mouseout', list_mouseout(unit));
  unit.addEventListener('click', list_click(unit));
};

document.getElementById('grid').addEventListener('click', function(e){
  let target = document.getElementById('target')
  target.value = e.target.dataset.coordinates;
});