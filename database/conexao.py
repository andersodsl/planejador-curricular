
from contextlib import contextmanager
from surrealdb import Surreal


@contextmanager
def conectar():

    url = "ws://127.0.0.1:8001/rpc"

    credenciais = {
        "username": "root",
        "password": "root"
    }

    with Surreal(url) as db:

        db.signin(credenciais)

        db.use(
            "planejador_curricular",
            "planejador_curricular"
        )

        yield db
