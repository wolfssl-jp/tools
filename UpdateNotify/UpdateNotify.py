# pip install PyGithub if not already installed PyGithub.
from github import Github
# !pip install slack_sdk
from slack_sdk import WebClient
import datetime
import sys
import os
import smtplib
from email.mime.multipart import  MIMEMultipart
from email.mime.text import MIMEText

import wolfssl_last_commit
import documentation_last_commit

#================== Configrations ==========================#
ACCESS_TOKEN="<Github のアクセストークン> "

mailing_list = [
    # "kojo@wolfssl.com",
    "shingo@wolfssl.com"
    # "hide@wolfssl.com",
    # "tak@wolfssl.com"
]

MAIL_ADDRESS = "送信元Gメールアドレス"
MAIL_PASSWORD = "アプリケーショントークンのパスワード" # ログインパスワードではない

TEST=False

if TEST==True:
    SLACK_APP_TOKEN = ''
    CHANNEL_ID = 'C04GL09TA7L' # channel ID of general in My Private workSpace

else:
    SLACK_APP_TOKEN = ''
    CHANNEL_ID = 'C029YM5K1J7' # channel ID of japan in wolfSSL workSpace 
#===========================================================#


def writeLog(file, str):
    with open(file, mode="a") as f:
        print(str, file=f)


def watchDoc_md():
    g = Github(ACCESS_TOKEN)
    repo = g.get_repo("wolfssl/documentation")

    # Check whether the LAST_COMMIT_SHA is None or not.
    try:
        Last_commit_sha = documentation_last_commit.LAST_COMMIT_SHA

    except AttributeError:
    # Initialize If the LAST_COMMIT_SHA is not found
        # Get the latest commit
        Last_commit = repo.get_commit("master")
        print(Last_commit.commit.committer.date)

        # Set the Hash of latest Commit to LAST_COMMIT_SHA in documentation_last_commit.py
        with open('documentation_last_commit.py', mode = "w") as f:
            f.write(f'LAST_COMMIT_SHA = \"{Last_commit.commit.sha}\"')
        print(f"Initialized {Last_commit.commit.sha[:7]}..")
        writeLog('documentation.log', f"[~] {datetime.datetime.today().strftime('%Y/%m/%d %H:%M')} : Initialized {Last_commit.commit.sha[:7]}..")

        sys.exit(1)


    # Get the object of Last commit
    Last_commit = repo.get_commit(Last_commit_sha)

    Last_updated_datetime = Last_commit.commit.committer.date

    # Get the newly updated commits.
    new_commits = repo.get_commits(since=(Last_updated_datetime+datetime.timedelta(minutes=1)) )

    print("Num of New commits", new_commits.totalCount)

    # Check if the last commit is not out of date.
    if new_commits.totalCount == 0:
        print("Not Out of Date!")
        writeLog('documentation.log', f"[*] {datetime.datetime.today().strftime('%Y/%m/%d %H:%M')} : Not Out of Date {Last_commit.commit.sha[:7]}..")
        sys.exit(2)


# Check Whether the Contents is updated or not.
    Notification_list = []

    for commit in new_commits:
        # Marge された時のコミットだけを見る。 （committerのcommitと重複してるから）
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
        print("Newly Merged commit but No updated Contents")
        writeLog('documentation.log', f"[*] {datetime.datetime.today().strftime('%Y/%m/%d %H:%M')} : Contents Not Updated!  {new_commits[0].commit.sha[:7]}..")

        
 
        
    else:   # Updated Contents Exist!
        print("Updated Contents Exist!")
        print("Num of Updated Contents: ", len(Notification_list))
        
        # Do Notification
        for commit in reversed(Notification_list):
            print(commit.commit.committer.date)
            notifier = Notifier(commit, subject="Documentation Updated !")
            notifier.gen_msg()

            for to_addr in mailing_list:

                # notifier.Sendmail(to_addr)
                notifier.SendSlack()
            writeLog('documentation.log', f"[+] {datetime.datetime.today().strftime('%Y/%m/%d %H:%M')} : Notified Updated Contents {commit.commit.sha[:7]}..")



    # Set the Newest Commit to LAST_COMMIT_SHA in documentation_last_commit.py
    with open('documentation_last_commit.py', mode = "w") as f:
        f.write(f'LAST_COMMIT_SHA = \"{new_commits[0].commit.sha}\"')






def watchDoc_header():
    g = Github(ACCESS_TOKEN)
    repo = g.get_repo("wolfssl/wolfssl")

    # Check whether the LAST_COMMIT_SHA is None or not.
    try:
        Last_commit_sha = wolfssl_last_commit.LAST_COMMIT_SHA
    except AttributeError:
    # Initialize If the LAST_COMMIT_SHA is not found
        # Get the latest commit
        Last_commit = repo.get_commit("master")
        print(Last_commit.commit.committer.date)

        # Set the Hash of latest Commit to LAST_COMMIT_SHA in wolfssl_last_commit.py
        with open('wolfssl_last_commit.py', mode = "w") as f:
            f.write(f'LAST_COMMIT_SHA = \"{Last_commit.commit.sha}\"')
        print(f"Initialized {Last_commit.commit.sha[:7]}..")
        writeLog('wolfssl_repo.log', f"[~] {datetime.datetime.today().strftime('%Y/%m/%d %H:%M')} : Initialized {Last_commit.commit.sha[:7]}..")

        sys.exit(1)


    # Get the object of Last commit
    Last_commit = repo.get_commit(Last_commit_sha)

    Last_updated_datetime = Last_commit.commit.committer.date

    # Get the newly updated commits.
    # path を指定すると https://github.com/wolfSSL/wolfssl/commits/master/{path} のコミットだけを取得できる
    # ロードするコミット数を減らせるが、仕組みが少し変わってしまうため　Merge されたコミットだけを見るというロジックが使えない。
    new_commits = repo.get_commits(since=(Last_updated_datetime+datetime.timedelta(minutes=1)) )

    print("Num of New commits", new_commits.totalCount)

    # # Check if the last commit is not out of date.
    if new_commits.totalCount == 0:
        print("Not Out of Date!")
        writeLog('wolfssl_repo.log', f"[*] {datetime.datetime.today().strftime('%Y/%m/%d %H:%M')} : Not Out of Date {Last_commit.commit.sha[:7]}..")
        sys.exit(2)


    # Check Whether the Contents is updated or not.
    Notification_list = []

    for commit in new_commits:
        # Marge された時のコミットだけを見る。 （committerのcommitと重複してるから）
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
        print("Newly Merged commit but No updated Contents")
        writeLog('wolfssl_repo.log', f"[*] {datetime.datetime.today().strftime('%Y/%m/%d %H:%M')} : Contents Not Updated!  {new_commits[0].commit.sha[:7]}..")

        
    else:   # Updated Contents Exist!
        print("Updated Contents Exist!")
        print("Num of Updated Contents: ", len(Notification_list))
        
        # Do Notification
        for commit in reversed(Notification_list):
            print(commit.commit.committer.date)
            notifier = Notifier(commit, subject="Documentation Updated !")
            notifier.gen_msg()

            for to_addr in mailing_list:

                # notifier.Sendmail(to_addr)
                notifier.SendSlack()
            writeLog('wolfssl_repo.log', f"[+] {datetime.datetime.today().strftime('%Y/%m/%d %H:%M')} : Notified Updated Contents {commit.commit.sha[:7]}..")



    # Set the Newest Commit to LAST_COMMIT_SHA in wolfssl_last_commit.py
    with open('wolfssl_last_commit.py', mode = "w") as f:
        f.write(f'LAST_COMMIT_SHA = \"{new_commits[0].commit.sha}\"')
    


class Notifier():

    def __init__(self, commit, subject="", msg=""):
        self.commit = commit
        self.subject=subject
        self.msg = msg

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


    def Sendmail(self, to_addr=""):
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



def getMerges():
    g = Github(ACCESS_TOKEN)
    repo = g.get_repo("wolfssl/wolfssl")
    print(repo.merges_url)




    
if __name__ == '__main__':
    watchDoc_md()
    watchDoc_header()
