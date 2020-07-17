from wtforms import Form, DecimalField, SelectField, validators


class validate(Form):
    age = DecimalField(
        1, [validators.NumberRange(min=1), validators.DataRequired()])
    sex = SelectField("male", [validators.DataRequired()],
                      choices=[("male", "male"), ("female", "female")])
    embarked = SelectField(
        "S", [validators.DataRequired()], choices=[("S", "S"), ("Q", "Q"), ("C", "C")])
