import configparser
import os.path
class Dev:
    def __init__(self,env):
        self.dev=env
        self.envprop_access()

    def envprop_access(self):
        try:
            #print(os.getcwd())
            self.db_config = configparser.ConfigParser()
            config_path=os.path.join(os.path.dirname(os.path.dirname(__file__)),'config','dev.properties')
            self.db_config.read(config_path)
        except FileNotFoundError as e:
            return e
        except Exception as e:
            return e

    def connect_db(self):
        try:
            #print(os.getcwd())
            host = self.db_config.get(self.dev, 'host')
            user = self.db_config.get(self.dev, 'user')
            password = self.db_config.get(self.dev, 'password')
            db = self.db_config.get(self.dev, 'database')
            return host, user, password, db
        except ConnectionError as e:
            return e
        except Exception as e:
            return e

    def get_project(self):
        project = self.db_config.get(self.dev, 'project')
        return project



obj=Dev("dev")

