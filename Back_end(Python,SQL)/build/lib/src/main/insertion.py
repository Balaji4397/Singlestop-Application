import sys
import traceback
import os.path
# sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)),'main'))
from execution import execution
from log_file import log


class table_insertion(execution):
    """"INSERTION OF VALUES INTO THE TABLES CREATED"""
    def __init__(self):
        """CLASS INITALIZATION"""
        super().__init__()
        self.path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'files', 'records')
        try:
            temp = sys.argv[1]
            temp_1=temp+".csv"
            if os.path.exists(os.path.join(self.path, temp_1)):
                self.record_access(temp_1,temp)
            else:
                temp_1=temp+".txt"
                if os.path.exists(os.path.join(self.path, temp_1)):
                    self.record_access(temp_1, temp)
        except:
            self.tables()


    def record_access(self,table_1,table_2):
        """ACCESSING CSV RECORDS TO INSERT VALUES INTO THE TABLES"""
        try:
            del sys.path[:]
            sys.path.append(os.path.join(self.path, table_1))
            for filepath in sys.path:
                self.record_insertion(table_2,filepath)
            return 0
        except Exception as e:
            self.log.debug(repr(traceback.format_exception(*sys.exc_info())))
            return 1

    def record_insertion(self,table_name,file_path):
        """RECORD INSERTION INTO THE TABLES CREATED"""
        try:
            with open(file_path, 'r') as read_file:
                data = read_file.readlines()
                for row in data:
                    query = "INSERT INTO " + table_name + " VALUES " + "(" + row + ")"
                    self.executes(query)
                self.log.info(table_name + " Records Inserted")
                return 0
        except Exception as error:
            self.log.debug(repr(traceback.format_exception(*sys.exc_info())))
            return 1

    def tables(self):
        """GETTING THE LIST OF TABLES"""
        try:
            del sys.path[:]
            sys.path.append(os.listdir(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'files', 'records')))
            for i in sys.path:
                for j in i:
                    table_1 = "".join(j)
                    table_2 = table_1.split("_", 1)[1]
                    table_2 = table_2.split(".", -1)[0]
                    self.record_access(table_1,table_2)
            return 0
        except Exception as e:
            return 1


table_insertion()

