from .api_credito import cr_bp
from .api_parametro import par_bp
from .api_lcc import lcc_bp
from .api_cliente import cliente_bp
from .api_ahorro import ahorro_bp
from .api_csocial import csocial_bp
from .api_lcr import lcr_bp
from .api_deposito import deposito_bp

#CURL login
#curl -X POST http://192.168.120.8:8001/v1/cliente/auth/login -H "Content-type: application/json" -d '{"rut": 6600427, "clave": 1234}'

def register_blueprints(app):
    app.register_blueprint(cr_bp)
    app.register_blueprint(par_bp)
    app.register_blueprint(lcc_bp)
    app.register_blueprint(cliente_bp)
    app.register_blueprint(ahorro_bp)
    app.register_blueprint(csocial_bp)
    app.register_blueprint(lcr_bp)
    app.register_blueprint(deposito_bp)

