import requests
from time import sleep


class Email:
    @staticmethod
    def get_email(count=1):
        """
        :param count: How many email addresses you need
        :return: Array with email addresses
        """
        return requests.get(f'https://www.1secmail.com/api/v1/?action=genRandomMailbox&count={count}').json()

    @staticmethod
    def check_mailbox(email: str):
        """
        :param email: Email address
        :return: Dict:
        id	Message id
        from	Sender email address
        subject	Subject
        date	Receive date
        """
        email_data = email.split('@')
        return requests.get(f'https://www.1secmail.com/api/v1/?action=getMessages&login={email_data[0]}&domain={email_data[1]}').json()

    @staticmethod
    def fetching_message(email: str, message_id: int):
        """
        :param email: Email address
        :param message_id: message_id. Takes from func check_mailbox
        :return: Dict:
            id	Message id
            from	Sender email address
            subject	Subject
            date	Receive date
            attachments	Attachments list
            body	Message body (html if exists, text otherwise)
            textBody	Message body (text)
            htmlBody	Message body (html)
        """
        email_data = email.split('@')
        return requests.get(f'https://www.1secmail.com/api/v1/?action=readMessage&login={email_data[0]}&domain={email_data[1]}&id={message_id}').json()


    @staticmethod
    def attachment_download(email: str, message_id: int, file: str):
        """
        :param email: Email address
        :param message_id: message_id. Takes from func check_mailbox
        :param file: filename of attachment
        :return: file
        """
        email_data = email.split('@')
        return requests.get(f'https://www.1secmail.com/api/v1/?action=download&login={email_data[0]}&domain={email_data[1]}&id={message_id}&file={file}')

    @staticmethod
    def message_handler(email: str):
        """
        :param email:  Email address
        :return: Dict:
            id	Message id
            from	Sender email address
            subject	Subject
            date	Receive date
            attachments	Attachments list
            body	Message body (html if exists, text otherwise)
            textBody	Message body (text)
            htmlBody	Message body (html)
        """
        data = len(Email.check_mailbox(email))
        while len(Email.check_mailbox(email)) == data:
            sleep(1)
        return Email.fetching_message(email, Email.check_mailbox(email)[-1]['id'])
