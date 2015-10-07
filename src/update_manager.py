import main
import utils


def try_update(dir):
    return update_routine("./steamcmd.sh " +
                          "+login " +
                          "anonymous " +
                          "+force_install_dir %s " % dir +
                          "+app_update 376030 " +
                          "+quit")


def backup(dir, id, vname):
    return ""


def backup_saves(dir, name):
    return ""


def try_update_mods():
    # get list
    for mod in mods:
        update_routine("appupdate")

        utils.z_unpack(main.p_mod_download + "content/mods/%s/Linux/*.z", )
        utils.create_modfile(main.p_mod_downloads + "content/mods/%s/")
    return ""


def update_routine(steamcmd):
    updated = False
    with utils.call2(steamcmd, main.p_steam) as proc:
        for line in proc.getBlock():
            if line.contains("Update state (0x61) downloading"):
                updated = True
                break
        proc.wait()
    return updated
