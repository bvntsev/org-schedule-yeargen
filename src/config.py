import os
import sys
import json

LINUX_DEFAULT_PATH = "/home/" + os.getlogin() + "/.config/osy/"
WIN_DEFAULT_PATH = "C:\\Program Files (x86)\\osy\\"
DEFAULT_FOLDER_PATH = LINUX_DEFAULT_PATH if sys.platform == "linux"\
                                                        else WIN_DEFAULT_PATH
DEFAULT_CONFIG_PATH = DEFAULT_FOLDER_PATH + "osy.cfg"

DEFAULT_ORG_BODY =\
            "#+TITLE: \n#+DATE: \n#+CATEGORY: \n* Schedule [0/0]\n** ... \n"
DEFAULT_ORG_BODY += '''
* Deadline [0/0]
** ...\n
* Tasks [0/0]
** ...\n
* Events [0/0]
** ...\n
* Notes
** ...
'''


def update_default_config(new_path):
    if os.path.exists(DEFAULT_CONFIG_PATH):
        file = open(DEFAULT_CONFIG_PATH, "w+")
        config = json.loads(file.read())
        config["path_to_config"] = new_path
        file.write(json.dumps(str(config)))
        return file
    else:
        create_config(DEFAULT_CONFIG_PATH)
        return update_default_config(new_path)


def create_defalt_json(user_path) -> dict:
    config = dict({"path_to_config": user_path, "org_body": DEFAULT_ORG_BODY})
    return config


def set_default_config(user_path):

    if (os.path.exists(DEFAULT_CONFIG_PATH) is False):
        file = create_config(user_path)
    else:
        file = open(user_path, "w+")
    file.write((str(json.dumps(create_defalt_json(user_path)))))
    return file


def read_config(user_path: str):
    if (os.path.exists(DEFAULT_CONFIG_PATH) is False):
        return create_config(user_path)
    config = json.load(open(user_path, "w+"))
    return config


def create_config(user_path):
    # print(user_path)
    # print(user_path[:user_path.rfind('/')])
    # exit()
    if (os.path.exists(DEFAULT_CONFIG_PATH) is False):
        try:
            os.makedirs(user_path[:user_path.rfind('/')])
        except FileExistsError:
            pass
        except OSError as error:
            print("Cannot create directory for config")
            print(error)
            return None
    if user_path[:user_path.rfind('/')+1] != DEFAULT_FOLDER_PATH:
        update_default_config(user_path)
    file = open(user_path, "w+")
    file.close()
    file = set_default_config(user_path)
    return file
