from motor import motor


def main():
    requirements = []
    req = motor()
    print(req)
    for r in req:
        requirements.append(r)
    flag_stop = True
    while flag_stop:
        cont = input('Do you want to continue? [y/n] ')
        if cont == 'y':
            req = motor()
            print(req)
            for r in req:
                requirements.append(r)
            continue
        else:
            flag_stop = False

    reqs = ''.join([str(item) + '\n' for item in requirements])

    with open('requirements.txt', 'w') as f:
        f.write('List of requirements:' + '\n' + reqs)

    return 'List of requirements:' + '\n' + reqs


if __name__ == '__main__':
    print(main())

