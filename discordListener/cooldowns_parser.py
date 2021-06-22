""" Example JSON from EPIC RPG
{
   "footer":{
      "text":"Check the short version of this command with \"rpg rd\""
   },
   "author":{
      "proxy_icon_url":"https://images-ext-1.discordapp.net/external/9Ty_Ug27x4pSVVVhxDnBJTpCTrdrH5Pvg3CEFAa0q0w/%3Fsize%3D512/https/cdn.discordapp.com/avatars/191356760873893890/a_5dcf72bb085b4ab869e86089391e1a87.gif",
      "name":"Dano's cooldowns",
      "icon_url":"https://cdn.discordapp.com/avatars/191356760873893890/a_5dcf72bb085b4ab869e86089391e1a87.gif?size=512"
   },
   "fields":[
      {
         "value":":clock4: ~-~ **`Daily`** (**20h 34m 20s**)\n:clock4: ~-~ **`Weekly`** (**0d 12h 32m 41s**)\n:clock4: ~-~ **`Lootbox`** (**2h 49m 57s**)\n:clock4: ~-~ **`Vote`** (**6h 1m 6s**)",
         "name":":gift: Rewards",
         "inline":false
      },
      {
         "value":":white_check_mark: ~-~ **`Hunt`**\n:clock4: ~-~ **`Adventure`** (**0h 55m 10s**)\n:clock4: ~-~ **`Training`** (**5m 15s**)\n:white_check_mark: ~-~ **`Duel`**\n:clock4: ~-~ **`Quest | Epic quest`** (**0h 43m 3s**)",
         "name":"<:epicrpgsword:697935997555572858> Experience",
         "inline":false
      },
      {
         "value":":clock4: ~-~ **`Chop | Fish | Pickup | Mine`** (**1m 22s**)\n:clock4: ~-~ **`Farm`** (**6m 35s**)\n:clock4: ~-~ **`Horse breeding | Horse race`** (**0d 21h 38m 28s**)\n:clock4: ~-~ **`Arena`** (**0d 14h 33m 53s**)\n:clock4: ~-~ **`Dungeon | Miniboss`** (**6h 5m 25s**)",
         "name":":sparkles: Progress",
         "inline":false
      }
   ],
   "color":10115509,
   "type":"rich"
}
"""

#":clock4: ~-~ **`Chop | Fish | Pickup | Mine`** (**1m 22s**)\n:clock4: ~-~ **`Farm`** (**6m 35s**)\n:clock4: ~-~ **`Horse breeding | Horse race`** (**0d 21h 38m 28s**)\n:clock4: ~-~ **`Arena`** (**0d 14h 33m 53s**)\n:clock4: ~-~ **`Dungeon | Miniboss`** (**6h 5m 25s**)"
def get_progress_cooldowns(progress_cds):
    work_cd_secs, farm_cd_secs = 0, 0
    rewards_cds_splitted = progress_cds.split("\n")
    for cd in rewards_cds_splitted:
        try:
            time_str = cd.split("(",1)[1].replace("*", "").replace(")", "")
        except Exception:
            continue
        if ('Chop | Fish | Pickup | Mine' in cd):
            work_cd_secs = remaining_cooldown_in_seconds(time_str)
        elif ('Farm' in cd):
            farm_cd_secs = remaining_cooldown_in_seconds(time_str)
    return work_cd_secs, farm_cd_secs

#":white_check_mark: ~-~ **`Hunt`**\n:clock4: ~-~ **`Adventure`** (**0h 55m 10s**)\n:clock4: ~-~ **`Training`** (**5m 15s**)\n:white_check_mark: ~-~ **`Duel`**\n:clock4: ~-~ **`Quest | Epic quest`** (**0h 43m 3s**)"
def get_experience_cooldowns(experience_cds):
    hunt_cd_secs, adventure_cd_secs = 0, 0
    rewards_cds_splitted = experience_cds.split("\n")
    for cd in rewards_cds_splitted:
        try:
            time_str = cd.split("(",1)[1].replace("*", "").replace(")", "")
        except Exception:
            continue
        if ('Hunt' in cd):
            hunt_cd_secs = remaining_cooldown_in_seconds(time_str)
        elif ('Adventure' in cd):
            adventure_cd_secs = remaining_cooldown_in_seconds(time_str)
    return hunt_cd_secs, adventure_cd_secs

#":clock4: ~-~ **`Daily`** (**20h 34m 20s**)\n:clock4: ~-~ **`Weekly`** (**0d 12h 32m 41s**)\n:clock4: ~-~ **`Lootbox`** (**2h 49m 57s**)\n:clock4: ~-~ **`Vote`** (**6h 1m 6s**)"
def get_rewards_cooldowns(rewards_cds):
    daily_cd_secs, weekly_cd_secs, lootbox_cd_secs = 0, 0, 0
    rewards_cds_splitted = rewards_cds.split("\n")
    for cd in rewards_cds_splitted:
        try:
            time_str = cd.split("(",1)[1].replace("*", "").replace(")", "")
        except Exception:
            continue
        if ('Daily' in cd):
            daily_cd_secs = remaining_cooldown_in_seconds(time_str)
        elif ('Weekly' in cd):
            weekly_cd_secs = remaining_cooldown_in_seconds(time_str)
        elif ('Lootbox' in cd):
            lootbox_cd_secs = remaining_cooldown_in_seconds(time_str)
    return daily_cd_secs, weekly_cd_secs, lootbox_cd_secs

# Expected format -> '1d 02h 34m 20s'
def remaining_cooldown_in_seconds(cooldown):
    days, hours, minutes, seconds = 0, 0, 0, 0
    splitted = cooldown.split(" ")
    for item in splitted:
        if 'd' in item:
            days = int(item.replace('d', ''))
        elif 'h' in item:
            hours = int(item.replace('h', ''))
        elif 'm' in item:
            minutes = int(item.replace('m', ''))
        elif 's' in item:
            seconds = int(item.replace('s', ''))
    return days * 86400 + hours * 3600 + minutes * 60 + seconds

print(remaining_cooldown_in_seconds('0h 34m 20s'))
print(get_rewards_cooldowns(":clock4: ~-~ **`Daily`** (**20h 34m 20s**)\n:clock4: ~-~ **`Weekly`** (**0d 12h 32m 41s**)\n:clock4: ~-~ **`Lootbox`** (**2h 49m 57s**)\n:clock4: ~-~ **`Vote`** (**6h 1m 6s**)"))