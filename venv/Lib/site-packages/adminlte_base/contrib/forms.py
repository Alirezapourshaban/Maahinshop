from wtforms import Form
from wtforms.fields import (
    StringField, PasswordField, BooleanField, HiddenField, FloatField,
    FieldList, FormField, TextAreaField, RadioField
)
import wtforms.validators as vd


__all__ = (
    'LoginForm', 'ResetPasswordForm',
)


class LoginForm(Form):
    """Login form."""
    email = StringField('E-Mail', validators=[
        vd.InputRequired(),
        vd.Email()
    ], render_kw={'data-icon': 'fas fa-envelope'})
    password = PasswordField('Password', validators=[
        vd.InputRequired()
    ], render_kw={'data-icon': 'fas fa-lock'})
    remember_me = BooleanField('Remember Me', validators=[
        vd.Optional()
    ])


class ResetPasswordForm(Form):
    """Password reset form."""
    email = StringField('E-Mail', validators=[
        vd.InputRequired(),
        vd.Email()
    ], render_kw={'data-icon': 'fas fa-envelope'})
