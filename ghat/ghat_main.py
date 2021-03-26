import os
import sys
import getopt
import subprocess
import time, datetime


def get_date_string(date_str):     
    fmt = '%Y-%m-%d'
    time_tuple = time.strptime(date_str, fmt)
    year, month, day = time_tuple[:3]
    a_date = datetime.date(year, month, day)
    rtn = a_date.strftime("%a %b %d %X %Y %z +0000")
    return rtn


def get_commit_command(date_str):
    curdate = get_date_string(date_str)
    command = "set GIT_AUTHOR_DATE='" + curdate + "'&& set GIT_COMMITTER_DATE='" + curdate + "'&& git commit -m 'update'"
    return command


def init_repository(date_str, url):
    command_list = ["echo init > README.md",
                    "git init",
                    "git add README.md",
                    "git remote add origin " + url,
                    get_commit_command(date_str),
                    "git push -u origin master"
                   ]
    command = "&& ".join(command_list)

    subprocess.call(command, shell=True)
    

def commit_as_date(date_str, times):
    for i in range(times):
        command_list = ["echo " + get_date_string(date_str) + ": " + str("update") +" >> work.txt"]
        command_list += ["git add work.txt"]
        command_list += [get_commit_command(date_str)]
        command = "&& ".join(command_list)

        subprocess.call(command, shell=True)
        print(date_str)
    #subprocess.call("git push", shell=True)


def push():
    subprocess.call("git push", shell=True)


def usage():
    print("USAGE 1: ghat")
    print("USAGE 2: ghat datefile")
    print("USAGE 3: ghat -i url datefile")


def main_process():
    is_init = False
    url = None
    file_path = None

    try:
        opts, args = getopt.getopt(sys.argv[1:], "i")
    except:
        usage()
        sys.exit()

    if len(args) == 2:
        for opt_name, opt_value in opts:
            if opt_name == "-i":
                is_init = True

        if opts:
            url = args[0]
            file_path = args[1]
        else:
            file_path = args[0]
    elif len(args) == 0:
        is_init = True if input("Initial your repository?(y/n)").upper() == "Y" else False
        if is_init:
            url = input("Input your repository url:")
        print("If you don't have a date file please make one online:")
        print("https://nymphxyz.github.io/ghat/ghat.html")
        print("Or open it locally:")
        print("{}".format(os.path.join(sys.path[0], "ghat.html")))
        file_path = input("Once you have the date file. Input its path:")
    else:
        usage()
        sys.exit()

    print("is_init: ", is_init)
    print("repository: ", url)
    print("date file: ", file_path)

    date_file = open(file_path, "r")

    flag = 0
    for line in date_file.readlines():
        line_str = line.replace("\n","")
        date_str = line_str.split(":")[0]
        num = int(line_str.split(":")[1])
        command_list = []
        for i in range(num):
            if flag == 0 and is_init:
                init_repository(date_str, url)
                flag += 1 
                continue;
            command_list += ["echo " + get_date_string(date_str) + ": " + str("update") +" >> work.txt"]
            command_list += ["git add work.txt"]
            command_list += [get_commit_command(date_str)]
            command = "&& ".join(command_list)  
            flag += 1 
        if command_list:
            print(line_str)
            subprocess.call(command, shell=True)
    print("pushing...")
    push()

if __name__ == "__main__":
    main_process()
