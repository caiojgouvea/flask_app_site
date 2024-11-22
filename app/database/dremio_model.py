import jaydebeapi
import os
from dotenv import load_dotenv

class DremioDB():
    def __init__(self):
        load_dotenv()

        self.driv = os.getenv("DREMIO_DRIV")
        self.path = os.getenv("DREMIO_PATH")
        self.host = os.getenv("DREMIO_HOST")
        self.port = os.getenv("DREMIO_PORT")
        self.user = os.getenv("DREMIO_USER")
        self.password = os.getenv("DREMIO_PASS")
        self.jdbc_url = f"jdbc:dremio:direct={self.host}:{self.port};"

    def getConn(self):
        conn = jaydebeapi.connect(
            self.driv,
            self.jdbc_url,
            [self.user, self.password],
            self.path
        )
        return conn