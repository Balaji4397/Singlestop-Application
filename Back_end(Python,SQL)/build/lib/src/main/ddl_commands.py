import sys
from execution import execution
import traceback
import time
from log_file import log

class ddl(log,execution):
    def __init__(self):
        log.__init__(self)
        execution.__init__(self)
        self.time1 = time.time()
        print("select the ddl command (drop,rename,new_column,drop_column,truncate_table):")
        user_input=input()
        print("Enter table name:")
        temp1=input()
        if user_input=="drop":
            if self.checkTableExists(temp1) == True:
                self.drop_table(temp1)

        elif user_input == "rename":
            if self.checkTableExists(temp1) == True:
                self.rename_table(temp1)

        elif user_input == "new_column":
            if self.checkTableExists(temp1) == True:
                self.add_new_column(temp1)

        elif user_input == "drop_column":
            if self.checkTableExists(temp1) == True:
                self.drop_existing_column(temp1)

        elif user_input == "truncate_table":
            if self.checkTableExists(temp1) == True:
                self.truncate_table(temp1)


    def checkTableExists(self, tablename):
        try:
            cursor = self.mycursor
            cursor.execute("SELECT COUNT(*)FROM information_schema.tables WHERE table_name = '{0}'".format(tablename.replace('\'', '\'\'')))
            if cursor.fetchone()[0] == 1:
                self.logger.info(tablename+" table present in DB")
                return True
            else:
                self.logger.info(tablename + " table not present in DB")
                sys.exit(1)

        except Exception as e:
            self.logger.debug(repr(traceback.format_exception(*sys.exc_info())))
            return 1

    def drop_table(self,table_name):
        try:
            command="Drop table {t_name}".format(t_name=table_name)
            self.executes(command)
            time2 = round(time.time() - self.time1, 2)
            time2 = (str(time2))
            self.logger.info(command +" "+ time2 + "s " + table_name + " Table DROPED")
            return 0
        except Exception as e:
            self.logger.debug(repr(traceback.format_exception(*sys.exc_info())))
            return 1

    def truncate_table(self,table_name):
        try:
            command="truncate {t_name}".format(t_name=table_name)
            self.executes(command)
            time2 = round(time.time() - self.time1, 2)
            time2 = (str(time2))
            self.logger.info(command +" "+ time2 + "s " + table_name + " Table truncated")
            return 0
        except Exception as e:
            self.logger.debug(repr(traceback.format_exception(*sys.exc_info())))
            return 1

    def rename_table(self,table_name):
        try:
            print("Enter new name for the table")
            new_name=input()
            command="alter table {t_name} rename to {new_t_name}".format(t_name=table_name,new_t_name=new_name)
            self.executes(command)
            time2 = round(time.time() - self.time1, 2)
            time2 = (str(time2))
            self.logger.info(command +" "+ time2 + "s " + table_name + " Table, name has been changed to "+new_name)
            return 0
        except Exception as e:
            self.logger.debug(repr(traceback.format_exception(*sys.exc_info())))
            return 1

    def add_new_column(self,table_name):
        try:
            print("Enter column name to be added:")
            column_name=input()
            print("Enter data type for new column:")
            data_type=input()
            command="alter table {t_name} add {c_name} {d_type}".format(t_name=table_name,c_name=column_name,d_type=data_type)
            self.executes(command)
            time2 = round(time.time() - self.time1, 2)
            time2 = (str(time2))
            self.logger.info(command +" "+ time2 + "s " + column_name + " has been added to "+table_name)
            return 0
        except Exception as e:
            self.logger.debug(repr(traceback.format_exception(*sys.exc_info())))
            return 1

    def drop_existing_column(self,table_name):
        try:
            print("Enter column name to drop from table:")
            column_name=input()
            command="alter table {t_name} drop {c_name} ".format(t_name=table_name,c_name=column_name)
            self.executes(command)
            time2 = round(time.time() - self.time1, 2)
            time2 = (str(time2))
            self.logger.info(command +" "+ time2 + "s " + column_name + " has been droped from "+table_name)
            return 0
        except Exception as e:
            self.logger.debug(repr(traceback.format_exception(*sys.exc_info())))
            return 1


obj1=ddl()

