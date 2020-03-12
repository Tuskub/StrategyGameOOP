import re
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, ValidationError


class ActionForm(FlaskForm):
    unit = StringField('Выбор юнита', validators=[DataRequired()])
    action = SelectField('Действие', choices=[('move', 'Перейти'), ('attack', 'Атаковать')]) # noqa
    target = StringField('Выбор цели', validators=[DataRequired()])
    submit = SubmitField('Сходить')

    def validate_unit(self, unit):
        nums = re.findall(r'\d{1,2}', unit.data)
        out_of_map = False
        for num in nums:
            if int(num) < 1 or int(num) >= 19:
                out_of_map = True
        if not re.match(r'^[[(]?\d{1,2}[,\s][\s]?\d{1,2}[])]?$', unit.data) or out_of_map:
            raise ValidationError('Введены неверные координаты.')

    def validate_target(self, target):
        nums = re.findall(r'\d{1,2}', target.data)
        out_of_map = False
        for num in nums:
            if int(num) < 1 or int(num) >= 19:
                out_of_map = True
        if not re.match(r'^[[(]?\d{1,2}[,\s][\s]?\d{1,2}[])]?$', target.data) or out_of_map:
            raise ValidationError('Введены неверные координаты.')
