from flask import request,make_response,redirect,render_template,session,url_for,flash
import unittest
from app import create_app
from app.forms import LoginForm

app= create_app()
todos=['1','2','3']


@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)

@app.errorhandler(404)
def not_found(error):
    
    return render_template('404.html', error=error)

@app.route('/')     
def index():
    user_ip=request.remote_addr
    response=make_response(redirect('/welcome'))
    session['user_ip'] = user_ip
    return response
    

@app.route('/welcome', methods=['GET', 'POST'])
def hello():
    user_ip=session.get('user_ip')
    login_form=LoginForm()
    user_name=session.get('user_name')
    contexto={
        'user_ip':user_ip,
        'todos':todos,
        'login_form':login_form,
        'user_name':user_name
    }
    if login_form.validate_on_submit():
        user_name= login_form.user_name.data
        session['user_name']=user_name
        flash('usuario creado')
        return redirect(url_for('index'))

    return render_template('ip_html.html',**contexto)
    # return f'Hellow world, platzS tu ip es {format(user_ip)}'