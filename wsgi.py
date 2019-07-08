#
# Conteudo do arquivo `wsgi.py`
#
import sys

sys.path.insert(0, "/home/seu-usuario/projetos/flask-test")

from myapp import app as application
