# import sys,os.path
# sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)),'main'))
from connection import connect_DB

class execution(connect_DB):
    def __init__(self):
        """Establish database connection"""
        super().__init__()
        self.mycursor = self.conn.cursor()


    def executes(self, query):
        """SQL COMMAND EXECUTION"""
        try:
            if (query.split(" ")[0]=="CREATE" or query.split(" ")[0]=="INSERT" or query.split(" ")[0]=="DROP" or query.split(" ")[0]=="DELETE" or query.split(" ")[0]=="UPDATE" or query.split(" ")[0]=="ALTER"):
                self.mycursor.execute(query)
                self.conn.commit()
                return self.mycursor
            else:
                self.mycursor.execute(query)
                self.mycursor.fetchone()
                return self.mycursor
        except Exception as e:
            return 0



