ModManager:
  def download(id):
  def unpack_z(src, dst):
  def create_mod_file(arg, arg):
  def get_version(id):
  def check_version(id):
  def update_all(dir, id_list):

ServerManager:
  def install(dir):
  def run():
    while True:
      time.sleep(60)
      if(not update_issues and UpdateManager.try_update(update_dir))
        if(ARK.try_start(update_dir))
          ARK.delete_useless_items(update_dir)
          UpdateManager.backup(update_dir, server_id, "standalone")
          if(ModManager.update_all(update_dir, mod_ids) and try_start(update_dir))
            UpdateManager.backup(update_dir, server_id, "mods")
            ARK.init_restart


  def is_ark_running():
  def

ARK:

    def init_restart():
        msg = "Neues Update vorhanden, Server startet in %i:%i neu."
        if(config.vote):
            msg += "\nIhr könnt den Restart um %i Minuten verzögern. Dazu gebt im Chat !noupdate ein."
            vote_bot()
        rcon.message(msg)
        

UpdateManager:
  def try_update(dir):
  def backup(dir, id, vname):
      name = "ark_server_%s" % id
  def backup_saves(dir, name)
