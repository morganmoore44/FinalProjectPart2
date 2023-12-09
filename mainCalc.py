from guiCalc import *
from logicCalc import *

def main() -> None:
    '''
    Method that runs GUI
    '''
    application = QApplication([])
    window = LogicCalc()
    window.show()
    application.exec()

if __name__ == "__main__":
    main()