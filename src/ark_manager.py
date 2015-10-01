#!/usr/bin/env python
# -*- coding: utf-8 -*-

def init_restart():
    msg = "Neues Update vorhanden, Server startet in %i:%i neu."
    if(config.vote):
        msg += u"\nIhr könnt den Restart um %i Minuten verzögern. Dazu gebt im Chat !noupdate ein."
        vote_bot()
    rcon.message(msg)
