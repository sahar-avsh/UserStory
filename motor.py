from role import getRole
from demand import getDemand
from reason import getReason


def motor():

    flag_role = True

    while flag_role:
        try:
            role = input('What is your role? ').lower().strip()
            r = getRole(role=role)
            flag_role = False
        except ValueError as e:
            print(e)
            continue

    flag_demand = True

    while flag_demand:
        try:
            demand = input('What is your demand? ').lower().strip()
            d = getDemand(demand=demand)
            flag_demand = False
        except ValueError as e:
            print(e)
            continue

    flag_reason = True

    while flag_reason:
        try:
            reason = input('What is your reason? ').lower().strip()
            re, flag_neg = getReason(reason=reason)
            flag_reason = False
        except ValueError as e:
            print(e)
            continue

    reqs = []
    for i in d:
        if flag_neg:
            req = 'As a(n) ' + r[0] + ' I want to ' + i + ' so that I do not ' + re
        else:
            req = 'As a(n) ' + r[0] + ' I want to ' + i + ' so that I ' + re
        reqs.append(req)

    return reqs


if __name__ == '__main__':
    print(motor())
