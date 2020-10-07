import os,sys
import traceback
from execution import execution
# from log_file import log
import time

class table_creation(execution):
    def __init__(self):
        # log.__init__(self)
        super().__init__()
        # super().loggers()
        self.path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'files', 'ddl')
        try:
            temp = sys.argv[1]
            file_path = os.path.join(self.path, temp + '.sql')
            self.create_table(temp, file_path)
        except:
            self.tables()



    def create_table(self,table,file_path):
        """TABLE CREATION"""
        try:
            time1=time.time()
            sqlfile = open(file_path,'r')
            sqlfile = sqlfile.read()
            command = sqlfile.split(';')[0]
            self.executes(command)
            time2=round(time.time()-time1,2)
            time2=(str(time2))
            self.log.info(command+" "+table+".sql"+" "+time2+"s "+table+" Table CREATED")
            return 0
        except Exception as e:
            self.log.debug(repr(traceback.format_exception(*sys.exc_info())))
            return 1

    def tables(self):
        """GETTING THE LIST OF TABLES"""
        try:
            del sys.path[:]
            sys.path.append(os.listdir(self.path))
            for i in sys.path:
                for j in i:
                    table = "".join(j)
                    name = table.split("_", 1)[0]
                    if name != "ref":
                        t_name = table.split(".")[0]
                        file_path = os.path.join(self.path,t_name + '.sql')
                        self.create_table(t_name, file_path)
                    # else:
                        # table_1 = table.split("_", 1)[1]
                        # t_name = table_1.split(".")[0]
                        # file_path = os.path.join(self.path,t_name + '.sql')
                        # self.create_table(t_name, file_path)
                        # r_name = table.split(".")[0]
                        # file_path = os.path.join(self.path,r_name + '.sql')
                        # self.create_table(r_name, file_path)
            return 0
        except Exception as e:
            self.log.debug("No table has been fetched")
            return 1

table_creation()
