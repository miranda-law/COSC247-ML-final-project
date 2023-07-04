# ==============================================================================
# Author: Miranda Law
# Course: COSC-247 Machine Learning
# Assignment: Final Project
# Last updated: 11/23/2022
# Desc: Pull data from Riot API and save to CSV to use for final project
# ==============================================================================

# ==============================================================================
# Imports
# ==============================================================================
from riotwatcher import LolWatcher, ApiError
import csv

# set API key
lol_watcher = LolWatcher("")

# Set user
my_region = 'na1'
mirinda = lol_watcher.summoner.by_name(my_region, 'Mirinda')
my_matches = []

"""
getMatches(): pull `count` matches from the RiotAPI
    inputs: 
        region - server region (e.g. 'na1')
        puuid - account puuid
        start - starting index
        count - number of matches
        matchList - list to hold match ids
    output: N/A
"""
def getMatches(region, puuid, start, count, matchList):

    matches = lol_watcher.match.matchlist_by_puuid(region, puuid, start=start, type='ranked', count=count)

    matchList += matches

# get all matches
for i in range(0,10):
    curr = i*100
    getMatches(my_region, mirinda['puuid'], start=curr, count=100, matchList=my_matches)

# split list into 2
my_matches1 = my_matches[:len(my_matches)//2] # len = 454
my_matches2 = my_matches[len(my_matches)//2:] # len = 454



# write to csv
file = open('game-data2.csv', 'w', newline='')
writer = csv.writer(file)

# desired statistics
features = ['assists', 'bountyLevel', 'champExperience', 'champLevel', 'consumablesPurchased', 'damageDealtToBuildings', 'damageDealtToObjectives', 'damageDealtToTurrets', 'damageSelfMitigated', 'deaths', 'detectorWardsPlaced', 'doubleKills', 'goldEarned', 'goldSpent', 'killingSprees', 'kills', 'largestCriticalStrike', 'largestKillingSpree', 'largestMultiKill', 'longestTimeSpentLiving', 'magicDamageDealt', 'magicDamageDealtToChampions', 'magicDamageTaken', 'neutralMinionsKilled', 'pentaKills', 'physicalDamageDealt', 'physicalDamageDealtToChampions', 'physicalDamageTaken', 'quadraKills', 'sightWardsBoughtInGame', 'spell1Casts', 'spell2Casts', 'spell3Casts', 'spell4Casts', 'timeCCingOthers', 'timePlayed', 'totalDamageDealt', 'totalDamageDealtToChampions', 'totalDamageShieldedOnTeammates', 'totalDamageTaken', 'totalHeal', 'totalHealsOnTeammates', 'totalMinionsKilled', 'totalTimeCCDealt', 'totalTimeSpentDead', 'totalUnitsHealed', 'tripleKills', 'trueDamageDealt', 'trueDamageDealtToChampions', 'trueDamageTaken', 'visionScore', 'visionWardsBoughtInGame', 'wardsKilled', 'wardsPlaced', 'win']

# write column names
writer.writerow(features)

# iterate through list of matches to write to csv
for matchID in my_matches2:
    matchStats = {}
    currentMatch = lol_watcher.match.by_id(my_region, matchID)

    for participant in currentMatch['info']['participants']:
        if participant['summonerName'] == mirinda['name']:
            print(currIndex)
            for f in features: 
                #print(matchStats[f] + participant[f])
                matchStats[f] = participant[f]
            break
        

    matchStats['id'] = matchID
    currIndex += 1
    writer.writerow(matchStats.values())



file.close()