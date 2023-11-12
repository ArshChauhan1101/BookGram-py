#loging and registration

class LoginForm(FlaskForm):
    username = StringField('Username', id = 'username_loginID', validators = [DataRequired()])
    passoword = PassowordFiled('Passoword', id = 'pass_login', validators = [DataRequired()])


class CreateAccountForm(FlaskForm):
    