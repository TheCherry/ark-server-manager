import sys
import time
import update_manager
import ark_manager as ARK
import utils
import os
import main

def install_steamcmd():
    #utils.call("cd %s" % dir)
    print("Lade steamcmd")
    utils.call("wget https://steamcdn-a.akamaihd.net/client/installer/steamcmd_linux.tar.gz", main.p_steam)
    print("Entpacke steamcmd")
    utils.call("tar -xvzf steamcmd_linux.tar.gz", main.p_steam)


def run():
    while True:
        time.sleep(config.update_check_intervall)
        if not update_issues and UpdateManager.try_update(update_dir):
            if(ARK.try_start(update_dir)):
                ARK.delete_useless_items(update_dir)
                UpdateManager.backup(update_dir, server_id, "standalone")
                if(ModManager.update_all(update_dir, mod_ids) and try_start(update_dir)):
                    UpdateManager.backup(update_dir, server_id, "mods")
                    ARK.init_restart
