from ffxivbot.models import *
import logging
import json
import random

def reply_message_action(receive, msg):
    action = {
            "action":"",
            "params":{},
            "echo":""
        }
    if(receive["message_type"]=="group"):
        action.update({
            "action":"send_group_msg",
            "params":{"group_id":receive["group_id"],"message":msg}
        })
    else:
        action.update({
            "action":"send_private_msg",
            "params":{"user_id":receive["user_id"],"message":msg}
        })
    return action

def group_ban_action(group_id, user_id, duration):
    action = {
            "action":"set_group_ban",
            "params":{"group_id":group_id,"user_id":user_id,"duration":duration},
            "echo":""
        }
    return action

def delete_message_action(message_id):
    action = {
            "action":"delete_msg",
            "params":{"message_id":message_id},
            "echo":""
        }
    return action