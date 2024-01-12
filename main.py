name = input('Please, enter your name: ')
surname = input('Now, write your surname: ')
age = int(input('Well, add the infromation about your age: '))


def message_format(name, surname, age):
    def wrapper(func):
        if age <= 18:
            text = f'Hi, {name}! Nice to meet you.'
        elif 18 < age < 30:
            text = f'Hello, {name}! We are really glad to hear from you.'
        else:
            text = f'Dear, {name} {
                surname}. We are happy to welcome you, thank you for still being with us!'
        func(text)
    return wrapper


@message_format(name, surname, age)
def message(text):
    print(text)
