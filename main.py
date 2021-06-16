from motor import motor


def main():
    requirements = []
    req = motor()
    print(req)
    requirements.append(req)
    flag_stop = True
    while flag_stop:
        cont = input('Do you want to continue? [y/n] ')
        if cont == 'y':
            req = motor()
            print(req)
            requirements.append(req)
            continue
        else:
            flag_stop = False

    reqs = ' '.join([str(item) for item in requirements])
    return 'List of requirements:' + '\n' + reqs


if __name__ == '__main__':
    print(main())

