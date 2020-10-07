import logging
import os
from time import strftime
import dev_config

class log():
    def __init__(self):
        self.obj = dev_config.Dev("dev")
        self.project = self.obj.get_project()
        self.log= self.create_log()

    def create_log(self):
        file_name=os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logs',
                               strftime('{p_name}_%Y_%m_%d_%H_%M.log'.format(p_name=self.project)))
        logging.basicConfig(level=logging.INFO,
                            format="%(asctime)s [%(levelname)s] %(message)s",
                            handlers=[logging.FileHandler(file_name),
                                      logging.StreamHandler()])
        logger=logging.getLogger(__name__)
        return logger