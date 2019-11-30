def calculate_remaining(gui):

    # first calculate remaining fields and/or update others accordingly
    income = int(gui.input_netto_inc.text())
    spendings = int(gui.input_yrly_spending.text())

    # calculate savings/year
    savings = income - spendings
    gui.input_yrly_savings.setText(str(savings))

    # calculate savings rate
    savings_rate = savings / income
    gui.input_saving_rate.setText("{:.2%}".format(savings_rate))

    # if not value was found, assume the following:
    if gui.input_cur_net_worth.text() is "":
        cur_net_worth = 0
        gui.input_cur_net_worth.setText("{}".format(cur_net_worth))
    else:
        cur_net_worth = float(gui.input_cur_net_worth.text())

    if gui.input_interest_rate.text() is "":
        interest_rate = 0.05
        gui.input_interest_rate.setText("{:.2%}".format(interest_rate))
    else:
        interest_rate = float(gui.input_interest_rate.text())

    if gui.input_swr.text() is "":
        swr = 0.04
        gui.input_swr.setText("{:.2%}".format(swr))
    else:
        swr = float(gui.input_swr.text())

    print("income: {}".format(income))
    print("savings: {}".format(savings))
    print("savings rate: {:.2%}".format(savings_rate))
    print("current net worth: {}".format(cur_net_worth))
    print("interest rate: {:.2%}".format(interest_rate))
    print("swr: {:.2%}".format(swr))




