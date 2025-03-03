'''
    This module is used to log the information of the program.
'''
from pathlib import Path
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Logger:
    '''
        Logger class
    '''
    path: str

    def log(self,
            message: str) -> None:
        '''
            Logs the message
        '''
        Path(self.path).touch(exist_ok = True)
        message_to_log: str = f"{datetime.now().strftime('%Y.%m.%d %H:%M:%S')}\t{message}\n"
        with open(self.path,
                  "a+",
                  encoding = "utf-8-sig") as file:
            file.write(message_to_log)
            file.close()
        print(message_to_log.strip())
