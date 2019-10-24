import requests
import json
import os
import random
from apscheduler.schedulers.blocking import BlockingScheduler
from ff_espn_api import League

class GroupMeException(Exception):
    pass

class SlackException(Exception):
    pass

class DiscordException(Exception):
    pass

class GroupMeBot(object):
    #Creates GroupMe Bot to send messages
    def __init__(self, bot_id):
        self.bot_id = bot_id

    def __repr__(self):
        return "GroupMeBot(%s)" % self.bot_id

    def send_message(self, text):
        #Sends a message to the chatroom
        template = {
                    "bot_id": self.bot_id,
                    "text": text,
                    "attachments": []
                    }

        headers = {'content-type': 'application/json'}

        if self.bot_id not in (1, "1", ''):
            r = requests.post("https://api.groupme.com/v3/bots/post",
                              data=json.dumps(template), headers=headers)
            if r.status_code != 202:
                raise GroupMeException('Invalid BOT_ID')

            return r

class SlackBot(object):
    #Creates GroupMe Bot to send messages
    def __init__(self, webhook_url):
        self.webhook_url = webhook_url

    def __repr__(self):
        return "Slack Webhook Url(%s)" % self.webhook_url

    def send_message(self, text):
        #Sends a message to the chatroom
        message = "```{0}```".format(text)
        template = {
                    "text":message
                    }

        headers = {'content-type': 'application/json'}

        if self.webhook_url not in (1, "1", ''):
            r = requests.post(self.webhook_url,
                              data=json.dumps(template), headers=headers)

            if r.status_code != 200:
                raise SlackException('WEBHOOK_URL')

            return r

class DiscordBot(object):
    #Creates Discord Bot to send messages
    def __init__(self, webhook_url):
        self.webhook_url = webhook_url

    def __repr__(self):
        return "Discord Webhook Url(%s)" % self.webhook_url

    def send_message(self, text):
        #Sends a message to the chatroom
        message = "```{0}```".format(text)
        template = {
                    "content":message
                    }

        headers = {'content-type': 'application/json'}

        if self.webhook_url not in (1, "1", ''):
            r = requests.post(self.webhook_url,
                              data=json.dumps(template), headers=headers)

            if r.status_code != 204:
                raise DiscordException('WEBHOOK_URL')

            return r

def random_phrase():
    phrases = ['-The first season of Regulation Fantasy Football was in 2012 and won by Matt Jerikovsky, giving the initial rise of Pay Me.',
               '-Season 6 logged the most vetoes AND the most upheld trades in one season, ever.',
               '-Regulation Gold will have nearly $10,000.00 paid out in winnings by the end of season 8.',
               '-Physical trophies were never delivered to league winners until season 4.',
               '-A late stat correction by ESPN after week 16 allowed the commish to get paid for 3rd place while placing 4th. Rule 5.3.1. was born.',
               '-Team Shit the Bed, known for throwing away seasons, has a trophy named after him worth 2 stars.',
               '-big foot once paid 88 auction dollars for tarik cohen.. or something.',
               '-Season 2 was the only 10 man league version of Regulation Gold, won by Nick Kiefner.',
               '-Brock Walker won season 4, thus taking home the very first Regulation Trophy.',
               '-Calvin Logan and Tyler Logan are the only two members of Regulation to be tried and convicted of misdemeanor collusion',
               '-Chatty niggas sure pipe down after taking a few L\'s.',
               '-Team Most Points Against Trophy was created in remembrance of Cole Robertson\'s great team but many L\'s',
               '-The trophy race prize was once split due to a tie, later, rules would be changed for a one-tie-all-tie trophy race going forward.',
               '-Cole Robertson became the first to win back to back Regulation Gold championships: Season 6 & 7.',
               '-Season 5 started the 14 man PPR format, previous seasons were standard scoring and 12 teams.',
               '-Regulation Lite season 1 started in 2018 as a 10 man auction keeper league. Tyler Logan defeated Pay Me in the finals.',
               '-While the quote Pay Me is Pay Out is a meme.. it is also true! Pay Me has paid out more than he has won in Regulation leagues.',
               '-The worst record for any season is 0-13 by Darkness Loomerzzz in season 8.',
               '-The best record for any season is 11-2 from DawgTawn Beltrami Beast in season 3 and COOL WALL in season 4.',
               '-So far, the championship has only been won by the #1 or #2 seed.',
               '-The first 3 games mean nothing, the last 3 games mean EVERYTHING!',
               '-Regulation Gold has had only one season that included every owner from the previous season.',
               '-In 2019, ESPN nuked their own website. Making it worse for everyone.',
               '-Hitler did nothing wrong.',
               '-The Oracle is known for predicting the future.',
               '-HIDE Calvin threads IGNORE Calvin posts DO NOT REPLY to Calvin.',
               '-CaCAW!',
               '-B-Ditty is Pout Out',
               '-Pay Me is Pay Out',
               '-The trade token used to be tradeable and used in negotiations for player trades.',
               '-Most requested owner for removal: Tyler Logan.',
               '-The Commish plans to welch payouts once they become high enough and worthy of theft, self destruct sequence activated...3..2.',
               '-It\'s never a good sign when you have to pray for a stat correction.',
               '-You can make the playoffs with 8 losses, it\'s been done before!',
               '-The purpose of the CPC is to give the illusion of democracy -Commish.',
               '-Fantasy football is pure skill.',
               '-Fer da sizzler.',
               '-Pay Me was not convicted for collusion, his case was tried by the CPC and was given punishments for other rule violations.',
               '-Does the bed shit?',
               '-I FUCKING LOVE FANTASY FOOTBALL',
               '-Calvin Logan once unplugged his router during a draft party after he got his roster filled. Nobody has drafted at Calvin\'s place since.',
               '-You really still think we will get quality match up predictions from Brock? Sad!.',
               '-Fuck the commish!',
               '-Every season I don\'t win is bullshit.',
               '-The CPC (rulebook) and data for Regulation Gold is in a 4.5MB package of 13 Folders and over 60 files',
               '-Kamala Harris gave dome for D.A.',
               '-John Thomas played one year in Regulation Gold.. He spent most of the time posting pictures of dicks in the groupme. Can\'t be unseen..',
               '-What part about see you in august don\'t you understand?',
               '-Impeach!',
               '-Please don\'t delete the groupme :(',
               '-If you win the trophy, there\'s a strong chance it will be delivered by a Logan.',
               '-I overheard the LMs discuss a 2 QB league once...',
               '-Live draft in Vegas?',
               '-The Season 5 trophy, won by Calvin Logan, was misprinted. It\'s missing "season 5" and just displays: "Regulation".',
               '-Mornin niggers',
               '-Regulation Gold has had over 22 different members',
               '-Reply to this post or your RB1 will break his leg tonight',
               '-What\'s a fantasy football league without some drama?',
               '-Cash payouts for winning Regulation today is the same as winning season one 4.5 times',
               '-I am only able to display archived records because of an error in the code.. please don\'t fix..',
               '-Pro tip: If you say "Pay Me is Pay Out" 5 times he appears in an enraged form.',
               '-Art Rooney says Bell will sign this week, Conner out concussed, Stars aligning?',
               '-What would this league look like if Pay Me lost season one... hmm..',
               '-If you don\'t have a trophy, did you even win?',
               '-FUCK B2B',
               '-It\'s difficult to win the trophy race without playing the eliminator league.. Just joining gives you 4 troph\'s!',
               '-The idea of one high paying trophy, upwards of 10 stars, was discussed, but ultimately scrapped.',
               '-16 Man PPR seems to be the future, but 14 is so sweet n juicy.',
               '-The kicker position was removed in Season 8, along with the TE slot, replaced with WR/TE.',
               '-Waivers process every Wednesday, Friday, Saturday, at 8pm Central.',
               '-In season 8, the trophy race was ported over to an excel spreadsheet. One of the many sweeping changes ESPN blessed us with.',
               '-FUCK NIGGA',
               '-Nigger.. haha look mom i posted it again',
               '-"See ya in august" was first coined by Shit the Bed, when he once again shit the bed.',
               '-The CPC was made to protect the league from collus.... haha ha aww man I can\'t even type that without laughing.',
               '-Season 8 made the change to give higher seeded teams a 5 point advantage in the playoffs, minus the championship.',
               '-NEW YEAR, NEW COMMISH',
               '-DOES IT BENEFIT THE COMMISH?',
               '-It\'s confirmed impossible to make a trade with every player in the league in one season.. Try it, I dare ya.',
               '-The Atlanta Falcons blew a 28-3 lead in the superbowl and lost.',
               '-Don\'t even get me started on the GREAT TRADE RAPE.',
               '-Man of the Week was a 2 trophy reward for one season.',
               '-Error. Something went wrong.',
               '-I QUIT!',
               '-1 in the chat if you\'ve been in Regulation since season 1!',
               '-Season 10 will be special.',
               '-The rope giveth, the rope taketh away.',
               '-THE DAY OF THE ROPE IS UPON US',
               '-The rope doesn\'t discriminate.. One day.. it will come for you.',
               '-Shitty sheets, it\'s a common occurance',
               '-Howdy, niggers',
               '-Why do I have to do all this work? The archives are MASSIVE...',
               '-Tyler Logan was kicked out of the league for dropping his entire team to the waiver wire in protest of commish, a martyr of sorts..',
               '-Fuck this place, where\'s Regulation Elite???',
               '-The day of the rope is defined as: the day your season comes to an end, generally 1st round of playoffs, or 8 losses in the regular season.',
               '-I\'m just a bot, I have no feelings.. Go ahead, try to @ me',
               '-I will be able to interact with you boys in the chat... some time in the future..',
               '-Something is burned into my code... Pay.... Me....is........ can\'t seem to find the rest.. Anyone help me?',
               '-I don\'t buy in to win, I pay up so I can shitpost the groupme and piss off Pay Me.',
               '-HEY! DRAFT AT CALVIN\'S PLACE!',
               '-Many trophies don\'t get added because they are too time consuming to calculate and award.. Maybe I can help?',
               '-Good heavens, just look at the time!',
               '-Knock knock, it\'s the Oracle with another trade offer ;)',
               '-Pay Me was in the finals for the first 3 seasons, he\'s never been back since.',
               '-TUDDY',
               '-Josh Keller is the only owner to have won a championship and later quit the league.',
               '-Send studs, get duds. It\'s simple math.',
               '-Wednesday night waivers can get a little wierd... I\'ve seen some things..',
               '-Nobody has yet to win the championship and the trophy race in the same year.']
    return [random.choice(phrases)]
######################################FUCK AROUND HERE##########################################################################

#def get_scoreboard_short(league, week=None):
    #Gets current week's scoreboard
    #box_scores = league.box_scores(week=week)
    #score = ['%s %.2f - %.2f %s' % (i.home_team.team_abbrev, i.home_score,
             #i.away_score, i.away_team.team_abbrev) for i in box_scores
             #if i.away_team]
    #text = ['Score Update'] + score
    #return '\n'.join(text)

######################################FUCK AROUND HERE##########################################################################
def get_scoreboard_short(league, week=None):
    #Gets current week's scoreboard
    box_scores = league.box_scores(week=week)
    score = ['%s %.2f - %.2f %s' % (i.home_team.team_abbrev, i.home_score,
             i.away_score, i.away_team.team_abbrev) for i in box_scores
             if i.away_team]
    text = ['Score Update'] + score
    return '\n'.join(text)

def get_projected_scoreboard(league, week=None):
    #Gets current week's scoreboard projections
    box_scores = league.box_scores(week=week)
    score = ['%s %.2f - %.2f %s' % (i.home_team.team_abbrev, get_projected_total(i.home_lineup),
                                    get_projected_total(i.away_lineup), i.away_team.team_abbrev) for i in box_scores
             if i.away_team]
    text = ['From the archives:'] + random_phrase()
    return '\n'.join(text)

def get_projected_total(lineup):
    total_projected = 0
    for i in lineup:
        if i.slot_position != 'BE':
            if i.points != 0 or i.game_played > 0:
                total_projected += i.points
            else:
                total_projected += i.projected_points
    return total_projected
    
def all_played(lineup):
    for i in lineup:
        if i.slot_position != 'BE' and i.game_played < 100:
            return False
    return True

def get_matchups(league, week=None):
    #Gets current week's Matchups
    matchups = league.box_scores(week=week)

    score = ['%s(%s-%s) vs %s(%s-%s)' % (i.home_team.team_name, i.home_team.wins, i.home_team.losses,
             i.away_team.team_name, i.away_team.wins, i.away_team.losses) for i in matchups
             if i.away_team]
    text = ['Matchups'] + score + random_phrase()
    return '\n'.join(text)

def get_close_scores(league, week=None):
    #Gets current closest scores (15.999 points or closer)
    matchups = league.box_scores(week=week)
    score = []

    for i in matchups:
        if i.away_team:
            diffScore = i.away_score - i.home_score
            if ( -16 < diffScore <= 0 and not all_played(i.away_lineup)) or (0 <= diffScore < 16 and not all_played(i.home_lineup)):
                score += ['%s %.2f - %.2f %s' % (i.home_team.team_abbrev, i.home_score,
                        i.away_score, i.away_team.team_abbrev)]
    if not score:
        return('')
    text = ['Close Scores'] + score + random_phrase()
    return '\n'.join(text)

def get_power_rankings(league, week=None):
    # power rankings requires an integer value, so this grabs the current week for that
    if not week:
        week = league.current_week
    #Gets current week's power rankings
    #Using 2 step dominance, as well as a combination of points scored and margin of victory.
    #It's weighted 80/15/5 respectively
    power_rankings = league.power_rankings(week=week)

    score = ['%s - %s' % (i[0], i[1].team_name) for i in power_rankings
             if i]
    text = ['Power Rankings'] + score
    return '\n'.join(text)

def get_trophies(league, week=None):
    #Gets trophies for highest score, lowest score, closest score, and biggest win
    matchups = league.box_scores(week=week)
    low_score = 9999
    low_team_name = ''
    high_score = -1
    high_team_name = ''
    closest_score = 9999
    close_winner = ''
    close_loser = ''
    biggest_blowout = -1
    blown_out_team_name = ''
    ownerer_team_name = ''

    for i in matchups:
        if i.home_score > high_score:
            high_score = i.home_score
            high_team_name = i.home_team.team_name
        if i.home_score < low_score:
            low_score = i.home_score
            low_team_name = i.home_team.team_name
        if i.away_score > high_score:
            high_score = i.away_score
            high_team_name = i.away_team.team_name
        if i.away_score < low_score:
            low_score = i.away_score
            low_team_name = i.away_team.team_name
        if abs(i.away_score - i.home_score) < closest_score:
            closest_score = abs(i.away_score - i.home_score)
            if i.away_score - i.home_score < 0:
                close_winner = i.home_team.team_name
                close_loser = i.away_team.team_name
            else:
                close_winner = i.away_team.team_name
                close_loser = i.home_team.team_name
        if abs(i.away_score - i.home_score) > biggest_blowout:
            biggest_blowout = abs(i.away_score - i.home_score)
            if i.away_score - i.home_score < 0:
                ownerer_team_name = i.home_team.team_name
                blown_out_team_name = i.away_team.team_name
            else:
                ownerer_team_name = i.away_team.team_name
                blown_out_team_name = i.home_team.team_name

    low_score_str = ['Low score: %s with %.2f points' % (low_team_name, low_score)]
    high_score_str = ['High score: %s with %.2f points' % (high_team_name, high_score)]
    close_score_str = ['%s barely beat %s by a margin of %.2f' % (close_winner, close_loser, closest_score)]
    blowout_str = ['%s blown out by %s by a margin of %.2f' % (blown_out_team_name, ownerer_team_name, biggest_blowout)]

    text = ['Trophies of the week:'] + low_score_str + high_score_str + close_score_str + blowout_str + random_phrase()
    return '\n'.join(text)

def bot_main(function):
    try:
        bot_id = os.environ["BOT_ID"]
    except KeyError:
        bot_id = 1

    try:
        slack_webhook_url = os.environ["SLACK_WEBHOOK_URL"]
    except KeyError:
        slack_webhook_url = 1

    try:
        discord_webhook_url = os.environ["DISCORD_WEBHOOK_URL"]
    except KeyError:
        discord_webhook_url = 1

    league_id = os.environ["LEAGUE_ID"]

    try:
        year = int(os.environ["LEAGUE_YEAR"])
    except KeyError:
        year=2019

    try:
        swid = os.environ["SWID"]
    except KeyError:
        swid='{1}'

    if swid.find("{",0) == -1:
        swid = "{" + swid
    if swid.find("}",-1) == -1:
        swid = swid + "}"

    try:
        espn_s2 = os.environ["ESPN_S2"]
    except KeyError:
        espn_s2 = '1'

    bot = GroupMeBot(bot_id)
    slack_bot = SlackBot(slack_webhook_url)
    discord_bot = DiscordBot(discord_webhook_url)
    if swid == '{1}' and espn_s2 == '1':
        league = League(league_id, year)
    else:
        league = League(league_id, year, espn_s2=espn_s2, swid=swid)

    test = False
    if test:
        print(get_matchups(league))
        print(get_scoreboard_short(league))
        print(get_projected_scoreboard(league))
        print(get_close_scores(league))
        print(get_power_rankings(league))
        print(get_scoreboard_short(league))
        function="get_final"
        bot.send_message("Testing")
        slack_bot.send_message("Testing")
        discord_bot.send_message("Testing")

    text = ''
    if function=="get_matchups":
        text = get_matchups(league)
    elif function=="get_scoreboard_short":
        text = get_scoreboard_short(league)
    elif function=="get_projected_scoreboard":
        text = get_projected_scoreboard(league)
    elif function=="get_close_scores":
        text = get_close_scores(league)
    elif function=="get_power_rankings":
        text = get_power_rankings(league)
    elif function=="get_trophies":
        text = get_trophies(league)
    elif function=="get_final":
        # on Tuesday we need to get the scores of last week
        week = league.current_week - 1
        text = "Final " + get_scoreboard_short(league, week=week)
        text = text + "\n\n" + get_trophies(league, week=week)
    elif function=="init":
        try:
            text = os.environ["INIT_MSG"]
        except KeyError:
            #do nothing here, empty init message
            pass
    else:
        text = "Something happened. HALP"

    if text != '' and not test:
        bot.send_message(text)
        slack_bot.send_message(text)
        discord_bot.send_message(text)

    if test:
        #print "get_final" function
        print(text)


if __name__ == '__main__':
    try:
        ff_start_date = os.environ["START_DATE"]
    except KeyError:
        ff_start_date='2019-09-04'

    try:
        ff_end_date = os.environ["END_DATE"]
    except KeyError:
        ff_end_date='2019-12-30'

    try:
        my_timezone = os.environ["TIMEZONE"]
    except KeyError:
        my_timezone='America/New_York'

    game_timezone='America/New_York'
    bot_main("init")
    sched = BlockingScheduler(job_defaults={'misfire_grace_time': 15*60})

    #power rankings:                     tuesday evening at 6:30pm local time.
    #matchups:                           thursday evening at 7:30pm east coast time.
    #close scores (within 15.99 points): monday evening at 6:30pm east coast time.
    #trophies:                           tuesday morning at 7:30am local time.
    #score update:                       friday, monday, and tuesday morning at 7:30am local time.
    #score update:                       sunday at 4pm, 8pm east coast time.

##################################THIS IS RANDOMSAY##############################################################################

    sched.add_job(bot_main, 'cron', ['get_projected_scoreboard'], id='projected_scoreboards',
        day_of_week='mon,tue,wed,thu,fri,sat,sun', hour='12,16,20', minute=10, start_date=ff_start_date, end_date=ff_end_date,
        timezone=my_timezone, replace_existing=True)

##################################THIS IS RANDOMSAY##############################################################################

    sched.add_job(bot_main, 'cron', ['get_power_rankings'], id='power_rankings',
        day_of_week='tue,sat', hour=15, minute=30, start_date=ff_start_date, end_date=ff_end_date,
        timezone=my_timezone, replace_existing=True)
    sched.add_job(bot_main, 'cron', ['get_matchups'], id='matchups',
        day_of_week='sun', hour=12, minute=55, start_date=ff_start_date, end_date=ff_end_date,
        timezone=game_timezone, replace_existing=True)
    sched.add_job(bot_main, 'cron', ['get_matchups'], id='matchups',
        day_of_week='tue,thu', hour=13, minute=23, start_date=ff_start_date, end_date=ff_end_date,
        timezone=game_timezone, replace_existing=True)
    sched.add_job(bot_main, 'cron', ['get_close_scores'], id='close_scores',
        day_of_week='sun,mon', hour=18, minute=30, start_date=ff_start_date, end_date=ff_end_date,
        timezone=game_timezone, replace_existing=True)
    sched.add_job(bot_main, 'cron', ['get_final'], id='final',
        day_of_week='tue', hour=1, minute=30, start_date=ff_start_date, end_date=ff_end_date,
        timezone=my_timezone, replace_existing=True)
    sched.add_job(bot_main, 'cron', ['get_scoreboard_short'], id='scoreboard1',
        day_of_week='fri,mon', hour=7, minute=30, start_date=ff_start_date, end_date=ff_end_date,
        timezone=my_timezone, replace_existing=True)
    sched.add_job(bot_main, 'cron', ['get_scoreboard_short'], id='scoreboard2',
        day_of_week='sun', hour='16,20', start_date=ff_start_date, end_date=ff_end_date,
        timezone=game_timezone, replace_existing=True)

    print("Ready!")
    sched.start()
