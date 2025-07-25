def adults_filter(lst):
    adults = []
    for person in lst:
        if person['age'] >= 18 :
            adults.append(person)
    return adults

def active_filter(lst):
    active_users = []
    for person in lst:
        if person['is_active'] == True :
            active_users.append(person)
    return active_users 

def adults_active_filter(lst):
    adults_active_users = []
    for person in lst:
        if person['age'] >= 18 and person['is_active'] == True :
            adults_active_users.append(person)
    return adults_active_users 