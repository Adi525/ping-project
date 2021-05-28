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



def set_values(ip, min, maks, avg):
    minimum.show()
    maximum.show()
    average.show()
    ip_adress.show()
    minimum.value = min
    maximum.value = maks
    average.value = avg
    ip_adress.value = ip


app = App(title='ping')

text = Text(app, text='Uzupełnij parametry poniżej:')

text_domain = Text(app, text='domena (www.adreswitryny.com/pl):')
field_domain = TextBox(app, text='www.google.com', width=50)

text_num = Text(app, text='liczba wysyłanych sygnałów (liczba całkowita):')
field_num = TextBox(app, text='5')

file_save = CheckBox(app, text='zapisz do pliku')
file_path = Text(app, text='Wpisz ścieżkę do folderu w którym zapisać wyniki (nie dysk systemowy)')
file_dir = TextBox(app, text='D:\\', width=50)
problem = Text(app, text='', enabled=False)

run = PushButton(app, text='wykonaj', command=run_command)

ip = Text(app, text='adres ip witryny:')
ip_adress = Text(app, text='', enabled=False)

min = Text(app, text='Minimalne opóźnienie:')
minimum = Text(app, text='', enabled=False)

maks = Text(app, text='Maksymalne opóźnienie:')
maximum = Text(app, text='', enabled=False)

av = Text(app, text='Średnia opóźnienia:')
average = Text(app, text='', enabled=False)

status_box = Box(app, align="bottom", border=1, width=500, height=30)
operations_status = Text(status_box, text='Wpisz dane i naciśnij przycisk "wykonaj"')
app.display()
