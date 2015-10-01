import main
import utils

def try_update(dir):
    utils.call("./steamcmd.sh +login anonymous +force_install_dir %s +app_update 376030 +quit" % dir, main.p_steam)
def backup(dir, id, vname):
    name = "ark_server_%s" % id
def backup_saves(dir, name):
    return ""

def try_update_mods():
    return ""
