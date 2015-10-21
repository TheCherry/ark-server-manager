import main
import utils


## http://arkdedicated.com/version

def try_update(dir):
    print("UPDATE")
    return update_routine("./steamcmd.sh " +
                          "+@ShutdownOnFailedCommand 1 " +
                          "+login " +
                          "anonymous " +
                          "+force_install_dir %s " % dir +
                          "+app_update %s " % main.config.server_appid +
                          "+quit").contains("Success! App '%s' fully installed." %s main.config.server_appid)


def backup(dir, id, vname):
    return ""


def backup_saves(dir, name):
    return ""

def 

def mod_need_update(modid):
    #POST https://api.steampowered.com/ISteamRemoteStorage/GetPublishedFileDetails/v1/, itemcount=1&publishedfileids[0]=%s" % modid
    # json
    # time_updated
    mod

def try_update_mods():
    # get list
    for mod in mods:
        update_routine("appupdate")
        #+workshop_download_item %s", main.config.mod_appid
        utils.z_unpack(main.p_mod_download + "content/mods/%s/Linux/*.z", )
        utils.create_modfile(main.p_mod_downloads + "content/mods/%s/")
        # save modid updatet at
    return ""


def update_routine(steamcmd):
    return utils.call_steam_update(steamcmd, main.p_steam)
