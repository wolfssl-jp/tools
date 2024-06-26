# pip install PyGithub if not already installed PyGithub.
from github import Github
# !pip install slack_sdk
from slack_sdk import WebClient
import datetime
import smtplib
import sys
from email.mime.multipart import  MIMEMultipart
from email.mime.text import MIMEText


#================== Configrations ==========================#
# Set the look back interval as a timedelta object
INTERVAL = datetime.timedelta(days=1)

# You must give Github and Slack APP token via command line argument.
ACCESS_TOKEN=""
SLACK_APP_TOKEN=""

TEST=False

if TEST==True:
    CHANNEL_ID = 'C04GL09TA7L' # channel ID of general at My Private workSpace
else:
    CHANNEL_ID = 'C029YM5K1J7' # channel ID of japan at wolfSSL workSpace 


# These components are not needed if you do not send an email.
mailing_list = [
    # "kojo@wolfssl.com",
    # "shingo@wolfssl.com",
    # "hide@wolfssl.com",
    # "tak@wolfssl.com"
]
MAIL_ADDRESS = ""
MAIL_PASSWORD = "<Google App Token>"
#===========================================================#



def writeLog(file, str):
    with open(file, mode="a") as f:
        print(str, file=f)

# return 0  : no update
#        2  : update
#        -1 : something wrong
def watchDoc_md():
    try:
        g = Github(ACCESS_TOKEN)
        repo = g.get_repo("wolfssl/documentation")
    except: 
        print("Github Token has no credential!")
        notifier = Notifier(subject="Github Token lost credential !", msg="")
        notifier.SendSlack()
        sys.exit(-1)


    # Get the today's UTC time
    today_UTC = datetime.datetime.now(datetime.timezone.utc)

    # Get the newly updated commits.
    new_commits = repo.get_commits(since=(today_UTC - INTERVAL))

    print("Num of New commits", new_commits.totalCount)

    # Check if the new commits exist or not
    if new_commits.totalCount == 0:
        print(f"New commit None")
        writeLog('documentation.log', f"[*] {datetime.datetime.today().strftime('%Y/%m/%d %H:%M')} : New commit None")
        return 0

# Check Whether the Contents is updated or not.
    Notification_list = []

    for commit in new_commits:
        # Marge された時のコミットだけを見る。 
        if "Merge pull request" in commit.commit.message:

            Notify=False
            for file in commit.files:
                # print(file.filename)
                if "src-ja" not in file.filename \
                            and "header-ja" not in file.filename \
                            and ".md" in file.filename:
                    Notify=True

            if Notify==True:
                Notification_list.append(commit)
                # print(file.filename, commit.commit.author.name, commit.commit.committer.date, commit.commit.html_url)



    # If there is no Updated Contents
    if len(Notification_list) == 0:
        print("Newly Merged but No updated Contents")
        writeLog('documentation.log', f"[*] {datetime.datetime.today().strftime('%Y/%m/%d %H:%M')} : Contents Not Updated!  {new_commits[0].commit.sha[:7]}..")
        return 0



    else:   # Updated Contents Exist!
        print("Updated Contents Exist!")
        print("Num of Updated Contents: ", len(Notification_list))

        # Do Notification
        for commit in reversed(Notification_list):
            print(commit.commit.committer.date)
            notifier = Notifier(commit, subject="Documentation Updated !")
            notifier.gen_msg()

            # for to_addr in mailing_list:
                # notifier.Sendmail(to_addr)
            notifier.SendSlack()
            writeLog('documentation.log', f"[+] {datetime.datetime.today().strftime('%Y/%m/%d %H:%M')} : Notified Updated Contents {commit.commit.sha[:7]}..")
        return 2




# return 0  : no update
#        2  : update
#        -1 : something wrong
def watchDoc_header():
    try:
        g = Github(ACCESS_TOKEN)
        repo = g.get_repo("wolfssl/wolfssl")
    except:  
        print("Github Token has no credential!")
        notifier = Notifier(subject="Github Token lost credential !", msg="")
        notifier.SendSlack()
        sys.exit(-1)



    # Get the today's UTC time
    today_UTC = datetime.datetime.now(datetime.timezone.utc)

    # Get the newly updated commits.
    new_commits = repo.get_commits(since=(today_UTC - INTERVAL))

    print("Num of New commits", new_commits.totalCount)

    # # Check if a new commit exist or not
    if new_commits.totalCount == 0:
        print("New commit None")
        writeLog('wolfssl_repo.log', f"[*] {datetime.datetime.today().strftime('%Y/%m/%d %H:%M')} : New commit None")
        return 0

    # Check Whether the Contents is updated or not.
    Notification_list = []

    for commit in new_commits:
        # Marge された時のコミットだけを見る。 
        if "Merge pull request" in commit.commit.message:

            Notify=False
            for file in commit.files:
                # print(file.filename)
                if "doc/dox_comments" in file.filename \
                            and "header_files-ja" not in file.filename:
                    Notify=True

            if Notify==True:
                Notification_list.append(commit)
                # print(file.filename, commit.commit.author.name, commit.commit.committer.date, commit.commit.html_url)



    # If there is no Updated Contents
    if len(Notification_list) == 0:
        print("Newly Merged but No updated Contents")
        writeLog('wolfssl_repo.log', f"[*] {datetime.datetime.today().strftime('%Y/%m/%d %H:%M')} : Contents Not Updated!  {new_commits[0].commit.sha[:7]}..")
        return 0

    else:   # Updated Contents Exist!
        print("Updated Contents Exist!")
        print("Num of Updated Contents: ", len(Notification_list))

        # Do Notification
        for commit in reversed(Notification_list):
            print(commit.commit.committer.date)
            notifier = Notifier(commit, subject="Documentation Updated !")
            notifier.gen_msg()

            # for to_addr in mailing_list:
            #     notifier.Sendmail(to_addr)  
            notifier.SendSlack()
            writeLog('wolfssl_repo.log', f"[+] {datetime.datetime.today().strftime('%Y/%m/%d %H:%M')} : Notified Updated Contents {commit.commit.sha[:7]}..")
        return 2




class Notifier():

    def __init__(self, commit=None, subject="", msg=""):
        self.commit = commit
        self.subject=subject
        self.msg = msg

        if commit is not None:
            self.updated_files = []
            for file in commit.files:
                self.updated_files.append(file.filename)


    def get_msg(self):
        return self.msg

    def gen_msg(self):
        msg = ""
        msg += f"[Date]         {self.commit.commit.committer.date}\n"
        msg += f"[Merged by]    {self.commit.commit.author.name}\n"
        msg += f"[Commit Message]\n"
        msg += f"{self.commit.commit.message}\n\n"

        msg += f"[Changed Files]\n"
        for filename in self.updated_files:
            msg += f"{filename}\n"
        msg += "\n"
        msg += f"[URL]  {self.commit.commit.html_url}\n"


        self.msg = msg


    def Sendmail(self, to_addr="shingo@wolfssl.com"):
        smtp_server = "smtp.gmail.com"
        port = 587

        server = smtplib.SMTP(smtp_server, port)
        server.starttls()

        server.login(MAIL_ADDRESS, MAIL_PASSWORD)

        message = MIMEMultipart()

        message["Subject"] = self.subject
        message["From"] = MAIL_ADDRESS
        message["To"] = to_addr

        text = MIMEText(self.get_msg())

        message.attach(text)

        server.send_message(message)

        server.quit()

    def SendLINE(self):
        pass

    def SendSlack(self):
        # Create the Slack Client
        client = WebClient(SLACK_APP_TOKEN)
        text= self.subject + "\n" + self.msg
        # Send text to the Slack Channel
        responce = client.chat_postMessage(channel=CHANNEL_ID, text=text)


def usage():
    print('')
    print('python UpdateNofiy.py <GitHub Access Token> <Slack App Token>')

if __name__ == '__main__':
    args = sys.argv

    if 2 >= len(args):
        print('')
        print('ACCESS TOKEN should be passed!')
        usage()
        sys.exit(-1)
    else:
        if 2 < len(args):
            ACCESS_TOKEN = args[1]
            SLACK_APP_TOKEN = args[2]
            
    mdval = watchDoc_md()
    print('---------------------------------------------')
    headval = watchDoc_header()
    
    print('=============================================')
    print('mdval ', mdval)
    print('headval ', headval)

    if mdval == 2 or headval == 2:
        sys.exit(2)

    else:
        if mdval == -1 or headval == -1:
            sys.exit(-1)
 
        else:
            if mdval == 0 and headval == 0:
                sys.exit(0)

