import main
import utils


def try_update(dir):
    return update_routine("./steamcmd.sh " +
                          "+login " +
                          "anonymous " +
                          "+force_install_dir %s " +
                          "+app_update 376030 " +
                          "+quit" % dir)


def backup(dir, id, vname):
    return ""


def backup_saves(dir, name):
    return ""


def try_update_mods():
    return ""


def update_routine(steamcmd):
    updated = False
    with utils.call(steamcmd, main.p_steam) as proc:
        for line in proc.getBlock():
            if line.contains("Update state (0x61) downloading"):
                updated = True
                break
        proc.wait()
    return updated
