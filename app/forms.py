from flask_wtf import FlaskForm
from wtforms.fields import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    user_name=StringField('Nombre de usuario',validators=[DataRequired()])
    password=PasswordField('Contraseña', validators=[DataRequired()])
    submit=SubmitField('Enviar')
