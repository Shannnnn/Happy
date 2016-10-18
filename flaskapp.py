@route('/hello')
def hello():
    return 'Hello Flask!'
	
greet = Flask(__name__)
    
@greet.route('/')
@greet.route('/hello/<name>')
def greet(name='Stranger'):
    return template('Hello {{name}}.', name=name)