username = ['John', 'Rey', 'Maquirang']
password = ['1234', 'rock123', 'python123']

def authentication():
    input_user = input('Enter Username: ')
    input_pass = input('Enter Password: ')

    for i in range(len(username)):
      if input_user == username[i] and input_pass == password[i]:
        print('Welcome,' , input_user)
        break
    else:
        print('Invalid Account')

authentication()