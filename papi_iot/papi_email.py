from __future__ import print_function
import pickle
import os.path
import base64
import mimetypes
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


class PAPIEmail:

    def __init__(self):
        self.creds = None
        self.service = None


    def getCredentials(self, PATH):
        """
        
            Shows basic usage of the Gmail API.
            Lists the user's Gmail labels.

        """

        SCOPES = ['https://www.googleapis.com/auth/gmail.send']

        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                self.creds = pickle.load(token)

        # If there are no (valid) credentials available, let the user log in.
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    f"{PATH}", SCOPES)
                self.creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(self.creds, token)

        self.service = build('gmail', 'v1', credentials=self.creds)

    def create_message(self, sender, to, subject, message_text):
        """Create a message for an email.
        Args:
            sender: Email address of the sender.
            to: Email address of the receiver.
            subject: The subject of the email message.
            message_text: The text of the email message.
        Returns:
            An object containing a base64url encoded email object.
        """
        message = MIMEText(message_text)
        message['to'] = to
        message['from'] = sender
        message['subject'] = subject
        return {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}

    def create_message_with_attachment(self, sender, to, subject, message_text, file):
        """Create a message for an email.

        Args:
        sender: Email address of the sender.
        to: Email address of the receiver.
        subject: The subject of the email message.
        message_text: The text of the email message.
        file: The path to the file to be attached.

        Returns:
        An object containing a base64url encoded email object.
        """

        message = MIMEMultipart()
        message['to'] = to
        message['from'] = sender
        message['subject'] = subject

        msg = MIMEText(message_text)
        message.attach(msg)

        content_type, encoding = mimetypes.guess_type(file)

        if content_type is None or encoding is not None:
            content_type = 'application/octet-stream'
            
        main_type, sub_type = content_type.split('/',1)

        if main_type == 'text':
            fp = open(file, 'rb')
            msg = MIMEText(fp.read(), _subtype=sub_type)
            fp.close()
        elif main_type == 'image':
            fp = open(file, 'rb')
            msg = MIMEImage(fp.read(), _subtype=sub_type)
            fp.close()
        else:
            fp = open(file, 'rb')
            msg = MIMEBase(main_type, sub_type)
            msg.set_payload(fp.read())
            fp.close()

        filename = os.path.basename(file)
        msg.add_header('Content-Disposition', 'attachment', filename=filename)
        message.attach(msg)
        
        b64_bytes = base64.urlsafe_b64encode(message.as_bytes())
        b64_string = b64_bytes.decode()
        return {'raw': b64_string}

    def send_message(self, user_id, to, subject, message,file=None):
        """Send an email message.
        Args:
            service: Authorized Gmail API service instance.
            user_id: User's email address. The special value "me"
                can be used to indicate the authenticated user.
            to: Email to be sent to
            subject: Email Subject
            message: Message to be sent.
            file: File Attachment to be added
        Returns:
            Sent Message.
        """

        if file == None:
            createdMessage = self.create_message(user_id,to,subject,message)
        else:
            createdMessage = self.create_message_with_attachment(user_id, to,subject,message,file)

        message = (self.service.users().messages().send(userId=user_id, body=createdMessage)
                .execute())
        print('Message Id: %s' % message['id'])
        return message


if __name__ == '__main__':
    path_to_pickle = r"client_secret_email.json"
    subject = "Hi! from python"
    sender = "giftmugweni@gmail.com"
    to = "mgwgif001@myuct.ac.za"
    message = "This e-mail is sent from Gmail API via python! Isn't that Cool?"
    file = "./home/pi/photos/knownFaces/Stallon.jpg"
    test = PAPIEmail()

    test.getCredentials('client_secret_email.json')
    result = test.send_message(sender,to,subject,message,file)

    print(result)