
Funkcje
================================
funkcje::

    def get_values(line):
        mini = line[line.index('Minimum') + 10: line.index('Minimum') + 14]
        maksi = line[line.index('Maximum') + 10: line.index('Maximum') + 14]
        avg = line[line.index('Average') + 10: line.index('Average') + 14]
        return mini, maksi, avg

::

    def get_ip(line):
        ip = line[line.index('[')+1:line.index(']')]
        return ip

::

    def run_command():
        problem.hide()
        os.chdir('C:\WINDOWS\system32')
        domain, num_of_calls = field_domain.value, field_num.value
        stream = os.popen('ping {0} -n {1}'.format(domain, num_of_calls))
        try:
            dane = stream.readlines()
            ip = get_ip(dane[1])
            minimum, maximum, avg = get_values(dane[-1])
            set_values(ip, minimum, maximum, avg)
        except IndexError:
            problem.show()
            problem.value = 'niepoprawne dane'
            return 0

        if file_save.value == 1:
            try:
                problem.hide()
                file = open('{}\\ping_wyniki.txt'.format(file_dir.value), 'a')
                #print('{}\\wynik.txt'.format(file_dir.value))
                file.write('Data pomiaru: ' + str(datetime.date.today()) + '\n')
                file.write('Domena: ' + field_domain.value + '\n')
                file.write('IP witryny: ' + ip_adress.value + '\n')
                file.write('Wyslano sygnalow: ' + field_num.value + '\n')
                file.write('Srednie opoznienie: ' + average.value + '\n\n')
            except PermissionError:
                problem.show()
                problem.value = 'Nieprawidłowa ścieżka'

::

    def set_values(ip, min, maks, avg):
        minimum.show()
        maximum.show()
        average.show()
        ip_adress.show()
        minimum.value = min
        maximum.value = maks
        average.value = avg
        ip_adress.value = ip
