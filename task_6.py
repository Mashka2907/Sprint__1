types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
}

tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
}

tickets_by_type = {}
all_ticket = []

def removes_duplicates(tiket):
    new_ticket = []
    for t in tiket:
        if t not in all_ticket:
            new_ticket.append(t)
            all_ticket.append(t)
    return new_ticket

def tickets_type(types, tickets):
    for i in range(1, 6):
        tickets_by_type[types[i]] = removes_duplicates(tickets[i])
    return tickets_by_type


print(tickets_type(types, tickets))