from SecEmail import Email

def main():
    print('Добро пожаловать! Будет благодарны если вы зайдете на наш канал: https://t.me/Adolf_Githuber')
    email_address = Email.get_email(1)[0]
    print(f'Ваш временный адрес: {email_address}')
    while True:
        print('\n\nОжидаем поступления нового сообщения\n\n')
        message_data = Email.message_handler(email_address)
        print(f'От кого: {message_data["from"]}\nДата: {message_data["date"]}\nЗаголовок: {message_data["subject"]}\n___________________________\n\nСообщение: \n{message_data["textBody"]}')


if __name__ == '__main__':
    main()
