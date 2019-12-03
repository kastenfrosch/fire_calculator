import datetime


def calculate_remaining(gui):

    # TODO: make inputs robust for invalid inputs like characters, etc
    # TODO: adjusting for inflation, and taxes!

    # first calculate remaining fields and/or update others accordingly
    income = int(gui.input_netto_inc.text())
    spendings = int(gui.input_yrly_spending.text())

    # calculate savings/year
    savings = income - spendings
    gui.input_yrly_savings.setText(str(savings))

    # calculate savings rate
    savings_rate = float(savings / income)
    gui.input_saving_rate.setText("{:.2%}".format(savings_rate))

    # if not value was found, assume the following:
    if gui.input_cur_net_worth.text() is "":
        cur_net_worth = 0
        gui.input_cur_net_worth.setText("{}".format(cur_net_worth))
    else:
        cur_net_worth = float(gui.input_cur_net_worth.text())

    if gui.input_interest_rate.text() is "":
        interest_rate = 0.05
        gui.input_interest_rate.setText("{:.2}".format(interest_rate*100))
    else:
        if float(gui.input_interest_rate.text()) > 1:
            interest_rate = float(gui.input_interest_rate.text()) / 100
        else:
            interest_rate = float(gui.input_interest_rate.text())

    if gui.input_swr.text() is "":
        swr = 0.04
        gui.input_swr.setText("{:.2}".format(swr*100))
    else:
        if float(gui.input_swr.text()) > 1:
            swr = float(gui.input_swr.text()) / 100
        else:
            swr = float(gui.input_swr.text())

    print("income: {}".format(income))
    print("spendings: {}".format(spendings))
    print("savings: {}".format(savings))
    print("savings rate: {:.2%}".format(savings_rate))
    print("current net worth: {}".format(cur_net_worth))
    print("interest rate: {:.2%}".format(interest_rate))
    print("swr: {:.2%}".format(swr))

    return calculate_fire(savings=savings,
                          spendings=spendings,
                          cur_net_worth=cur_net_worth,
                          interest_rate=interest_rate,
                          swr=swr)


def calculate_fire(savings, spendings, cur_net_worth, interest_rate, swr):

    net_worth_over_time = []
    now = datetime.datetime.now()
    cur_year = int(now.year)
    year = 0
    net_interests = 0
    savings_without_interests = 0

    while (cur_net_worth*swr) < spendings:
        # calculate...
        if year is not 0:
            # adding savings of previous to current net worth
            cur_net_worth += savings
            savings_without_interests += savings

        # interests per year
        interests = cur_net_worth*interest_rate
        net_interests += interests
        # adding interests to current net worth
        cur_net_worth += interests

        # saving everything into list
        date = datetime.date(cur_year, 1, 1)
        net_worth_over_time.append((date,
                                    round(cur_net_worth, 2),
                                    round(savings_without_interests, 2),
                                    round(net_interests, 2)))

        year += 1
        cur_year += 1

    print("\nnet worth after {} years: {}.".format(year, round(cur_net_worth, 2)))
    print("savings alone: {}, interests generated: {}".format(round(savings_without_interests, 2),
                                                              round(net_interests, 2)))
    print("\ncongratulations, you have reached financial independence!")

    return net_worth_over_time


def years_to_fire_based_on_savings_rate(savings_rate):

    sr_to_years = []

    return sr_to_years








