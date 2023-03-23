def get_category_name(expense):
    return expense.category


def get_source_name(income):
    return income.source


def get_expense_category_amount(category, expenses):
    amount = 0
    current_category = expenses.filter(category=category)
    for expense in current_category:
        amount += expense.amount
    return amount


def get_income_source_amount(source, incomes):
    amount = 0
    current_source = incomes.filter(source=source)
    for income in current_source:
        amount += income.amount
    return amount


def expense_summary(expenses):
    expense_data = {}
    category_list = list(set(map(get_category_name, expenses)))
    for expense in expenses:
        for category in category_list:
            expense_data[category.name] = get_expense_category_amount(category, expenses)
    return expense_data


def income_summary(incomes):
    income_data = {}
    source_list = list(set(map(get_source_name, incomes)))
    for income in incomes:
        for source in source_list:
            income_data[source.name] = get_income_source_amount(source, incomes)
    return income_data