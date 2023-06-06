from sqlalchemy import create_engine, text
import os
db_connect_string = os.environ['DB_CONNECT_STRING']



engine = create_engine(db_connect_string,
connect_args={
  "ssl" : {
    "ssl_ca": "/etc/ssl/cert.pem",
  }
}
                      )

with engine.connect() as conn:
  result = conn.execute(text("select * from smartphone"))
  print(result.all())