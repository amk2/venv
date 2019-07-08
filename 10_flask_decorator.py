@app.route('/admin')
def admin_index():
    # Verifica se session['logado'] já foi setado
    if ('logado' not in session):
        return redirect('index')

    # Caso usuário esteja logado, renderiza a página /admin/index.html
    return render_template('/admin/index.html')            

# Decorator
def requer_autenticacao(f):
    @wraps(f)
    def funcao_decorada(*args, **kwargs):
        # Verifica session['logado']
        if ('logado' not in session):
            # Retorna para a URL de login caso o usuário não esteja logado
            return redirect(url_for('index'))

        return f(*args, **kwargs)
    return funcao_decorada

# Olha quem tá aqui... Outro decorator :D
@app.route('/admin/dashboard')
@requer_autenticacao
def admin_dashboard():
    # Renderiza o template dashboard.html
    return render_template('admin/dashboard.html')


"""
E o decorator @wraps(f) na linha 3? O que faz?

Quando utilizamos um decorator, estamos substituindo uma função X() por outra função Y() que engloba a função X().

E o que isso traz de problema?

Isso quer dizer que a nova função irá perder seus metadados (__name__, __docstring__, etc…). Esse não é um efeito que queremos que aconteça.

Por exemplo, caso você tente mostrar na tela qual o nome da função após ela ter sido decorada, X.__name__ não irá apresentar seu nome original e sim o nome da função utilizada dentro do decorator.

Para evitar esse efeito colateral, utilizamos a função functools.wraps.

O que ela faz é copiar os metadados da função antes de ser decorada para sua versão decorada. Feito isso, utilizar um decorator não tira a identidade da sua função. Ela fica intacta!


Ref.: https://pythonacademy.com.br/blog/domine-decorators-em-python
"""
