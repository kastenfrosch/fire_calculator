def calculate_remaining(gui):
    income = int(gui.input_netto_inc.text())
    spendings = int(gui.input_yrly_spending.text())
    savings = income - spendings
    gui.input_yrly_savings.setText(str(savings))

    savings_rate = savings / income
    gui.input_saving_rate.setText("{:.2%}".format(savings_rate))

