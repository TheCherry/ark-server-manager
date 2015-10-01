global p_main, p_steam, p_run, p_update
import utils

p_main = utils.getScriptPath() + "/working"
p_steam = p_main + "/steamcmd"
p_run = p_main + "/ark/run"
p_update = p_main + "/ark/update"

def main():
    if sys.argv[1] == "init":
        os.makedirs([path, p_run, p_update])
        server_manager.install_steamcmd()
    if sys.argv[1] == "start":
        updated = update_manager.try_update(p_run)
        updated_mods = update_manager.try_update_mods(p_run, config.mods)
        if(updated and updated_mods):
            update_manager.backup(p_run)
        ark.run(p_run)

if __name__ == "__main__":
    import os

    import sys
    import update_manager
    import ark_manager as ark
    import server_manager
    import config



    main()
