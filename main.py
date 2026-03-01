import json
import argparse


def add_expense(budget, expenses):
    description_waste = input("Введите описании траты: ")
    waste_money = float(input("Ведите кол-во потраченный денег: "))
    if budget >= waste_money:
        print(f"Добавлена трата: {description_waste}, потрачено денег: {waste_money}")
        expenses.append({"description":description_waste,"amount": waste_money})
        return budget-waste_money
    else:
        print("Не можем добавить трату, кол-ва ващих денег не хватает, сначало укажите ваш точный бюджет.")


def show_budget_details(first_budget, expenses, budget, new_budget):
    print(f"Изначально было денег: {first_budget}.")
    for expense in expenses:
        print(f'Траты: {expense["description"]}: {expense["amount"]}')
    print(f'Добавлено к бюджету: {new_budget}')
    print(f"Текущий баланс: {budget}")
    get_total_expenses(expenses)


def get_total_expenses(expenses):
    sum_wast = 0
    for expense in expenses:
        sum_wast += expense["amount"]
    print(f'сумма всех затрат: {sum_wast}')


def save_budget_details(initial_budget, first_budget, expenses, filepath):
    data = {'first_budget': first_budget, 'initial_budget': initial_budget, 'expenses': expenses}
    with open(filepath, 'w', encoding='UTF8') as file:
        json.dump(data, file, ensure_ascii=False)


def load_budget_data(filepath):
    try:
        with open(filepath, 'r', encoding='UTF8') as file:
            data = json.load(file)
        return data['initial_budget'], data['expenses'], data['first_budget']
    except(FileNotFoundError, json.JSONDecodeError):
        return 0,[], 0


def update_budget(budget):
    add_money = float(input("Сколько денег вы получили: "))
    return add_money, budget+add_money
    

def main():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--filepath', type=str, help='')
    args = parser.parse_args()
    new_budget = 0
    initial_budget, expenses, first_budget = load_budget_data(args.filepath)
    if initial_budget == 0:
        initial_budget = float(input("Добро пожаловать, здесь вы сможете отслеживать свои фиинансы.\nПожалуйств введите имеющееся у вас кол-во денег: "))
        first_budget = initial_budget
    if not expenses:
        expenses = []
    budget = initial_budget
    while True:
        selection = input("""Что вы хотите сделать?
            1. Добавить траты
            2. Покахать кол-во оставшихся денег
            3. Обновить бюджет
            4. Выйти
            Ваш выбор 1/2/3/4: """)
        if selection == "1":
            budget = add_expense(budget, expenses)
        elif selection == "2":
            show_budget_details(first_budget, expenses, budget, new_budget)
        elif selection == "3":
            new_budget, budget = update_budget(budget)
        elif selection == "4":
            save_budget_details(initial_budget, first_budget, expenses, args.filepath)
            break
        else:
            print("Нет такого варианта ответа.\nПопробуйте снова.")
if __name__ == "__main__":
    main()
