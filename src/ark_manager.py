#!/usr/bin/env python
# -*- coding: utf-8 -*-

max_delays = 3
restart_time = 15
delay_time = 10


def init_restart():
    vote_bot()

def vote_bot():
    players_voted = []
    delays = 0
    players = parse_player_list(rcon("playerList"))
    #if len(players) == 0:
    #    return True
    #starttime = time.now()
    #thread:
    #    while true:
    #        chat = rcon("getChat")
    #        for line in chat:
    #            pchat = parse_chat_line(line)
    #            if pchat["msg"] == "!noupdate" and pchat["player"] not in players_voted:
    #                players_voted.append(pchat["player"])
    #                rcon("whisper %s Dein Vote wurde angenommen." % pchat["player"])
    #        time.sleep(2)
    #thread:
    #    while true:
    #        players = parse_player_list(rcon("playerList"))
    #        prc = 100.0 / len(players) * len(players_voted)
    #        left_minutes = "00"
    #        left_seconds = "00"
    #        if(prc > 50.0):
    #            restart_time += 10
    #            delays += 1
    #            thr_vote.kill()
    #            thr_vote.wait()
    #            players_voted = []
    #            thr_vote.start()
    #            add_msg = u"Das Update wird um weitere %i Minuten verzögert.\n" % delay_time
    #            if max_delays < current_delays:
    #                add_msg += u"Ein erneuter Vote verzögert das Update um weitere %i Minuten." % delay_time
    #            else:
    #                add_msg += u"Ein weiterer Vote ist nicht mehr möglich."
    #        else:
    #            add_msg = u"Es werden über 50%% an stimmen benötigt" +
    #            u"um das Update um %i Minuten zu verzögern." % delay_time
    #        rcon(u"announce Neues Update vorhanden - Restart des Servers in %s:%s.\n" +
    #             "Ihr könnt den Restart um %i Minuten verzögern. Dazu gebt im Chat !noupdate ein.\n\n" +
    #             "%i%% der Spieler haben für eine Verzögerung des Updates gestimmt.\n" +
    #             "%s" % (left_minutes, left_seconds, delay_time, prc, add_msg))
    #        time.sleep(60)


def parse_player_list(plist):
    players = []
    for player in plist:
        players.append(player)

    return players


def parse_chat_line(cline):
    splited = cline.split()
    ret = {}
    ret["player"] = splited[0]
    ret["steam"] = splited[1]
    ret["msg"] = splited[2]
    return ret

def rcon(cmd):
    return cmd
