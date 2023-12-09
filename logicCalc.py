from guiCalc import *
from PyQt6.QtWidgets import *

class LogicCalc(QMainWindow, Ui_Form):
    def __init__(self) -> None:
        '''
        Method that sets class variables
        '''
        super().__init__()
        self.name = ""
        self.income = 0.0
        self.needs = 0.0
        self.wants = 0.0
        self.savings = 0.0
        self.needs_rating = ""
        self.wants_rating = ""
        self.savings_rating = ""
        self.rating_num = 0
        self.setupUi(self)
        # calls submit function
        self.submit_button.clicked.connect(lambda: self.submit())

    def submit(self) -> None:
        '''
        Method that sets input variables to class variables, and then rates the budget based on percentage of traditional budgeting scale (50% needs, 30% wants, 20% savings)
        '''
        try:
            self.name = self.name_input.text()
            self.income = float(self.income_input.text())
            self.needs = float(self.needs_input.text())
            self.wants = float(self.wants_input.text())
            self.savings = float(self.savings_input.text())
            # rates needs first
            if self.needs/self.income == .50:
                self.needs_rating = "Great"
                self.rating_num += 2
            elif .48 <= self.needs/self.income <= .53:
                self.needs_rating = "Okay"
                self.rating_num += 1
            elif .48 > self.needs/self.income or self.needs/self.income > .53:
                self.needs_rating = "Bad"
                self.rating_num += 0
            # rates wants second
            if self.wants/self.income == .30:
                self.wants_rating = "Great"
                self.rating_num += 2
            elif .28 <= self.wants/self.income <= .33:
                self.wants_rating = "Okay"
                self.rating_num += 1
            elif .28 > self.wants/self.income or self.wants/self.income > .33:
                self.wants_rating = "Bad"
                self.rating_num += 0
            # rates savings last
            if self.savings/self.income == .20:
                self.savings_rating = "Great"
                self.rating_num += 2
            elif .18 <= self.savings/self.income <= .23:
                self.savings_rating = "Okay"
                self.rating_num += 1
            elif .18 > self.savings/self.income or self.savings/self.income > .23:
                self.savings_rating = "Bad"
                self.rating_num += 0
            self.output_label.setText(f'{self.name}\'s Budget Rating:\nYour total rating out of 6 possible points is: {self.rating_num}\nYour needs percentage rating is: {self.needs_rating}\nYour wants percentage rating is: {self.wants_rating}\nYour savings percentage rating is: {self.savings_rating}')
            self.clear()

        except ValueError:
            # prints error to output label
            self.output_label.setText('Income, needs, wants, and\nsavings must all be numeric\nvalues. (ex: 1500.00 not $1500.00)')
            self.clear()




    def clear(self) -> None:
        '''
        Method that clears input variables
        '''
        self.name_input.clear()
        self.income_input.clear()
        self.needs_input.clear()
        self.wants_input.clear()
        self.savings_input.clear()


