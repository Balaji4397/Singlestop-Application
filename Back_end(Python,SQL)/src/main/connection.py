import mysql.connector
from log_file import log
import dev_config
# import os,sys
# sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)),'main'))

class connect_DB(log):
    def __init__(self):
        super().__init__()
        self.conn=self.connect()

    def connect(self):
        try:
            obj=dev_config.Dev("dev")
            host, user, pwd, db = obj.connect_db()
            mydb = mysql.connector.connect(host=host, user=user, password=pwd, database=db)
            return mydb
        except Exception as e:
            self.log.info('Either host,user,password or database given is incorrect')
            return 1

# obj=connect_DB()
# obj.connect()