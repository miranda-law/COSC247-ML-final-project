# COSC247-ML-final-project
## Amherst College COSC-247 Machine Learning Final Project

**See `final-project.ipynb` for final results and analysis.**

### Description

[League of Legends](https://en.wikipedia.org/wiki/League_of_Legends) is a multiple online battle arena (MOBA) video game that involves two teams of five players. Each team wins by destroying the enemy "nexus" located in the enemy base. Each player earns experience points (exp) and gold to give their character extra statistics in order to defeat the enemy. 

In this project, I classified League of Legends games as either `win` or `loss` based on player game statistics at the end of the game, such as number of kills/deaths, gold earned, and damage dealt. I explored how these different statistics in the game affect the outcome of these games. In particular, I looked at my own ranked solo/duo games under the summoner name `Mirinda`.  

I obtained my data through the [RiotAPI](https://developer.riotgames.com/apis). I pulled a list of matches and chose a particular player to view their statistics.

In order to explore how different post-game statistics affect the outcome of the game, I trained multiple classifications models using different sets of features. The classification models are as follows:

- Perceptron
- Logistic regression
- Decision tree
- Random forest
- Support vector machine with radial basis function kernel

### Feature selections

These are the 7 sets of features I used to compare with one another:

1. all features
2. player combat -- offensive: 'largestCriticalStrike', 'magicDamageDealt','magicDamageDealtToChampions', 'physicalDamageDealt', 'physicalDamageDealtToChampions', 'totalDamageDealt', 'totalDamageDealtToChampions'
3. player combat -- defensive: 'damageSelfMitigated', 'magicDamageTaken', 'physicalDamageTaken', 'totalDamageShieldedOnTeammates', 'totalDamageTaken', 'totalHeal', 'totalHealsOnTeammates', 'trueDamageTaken'
4. player combat -- offensive AND defensive
5. spell casts: 'spell1Casts', 'spell2Casts', 'spell3Casts', 'spell4Casts'
6. KDA, kill streaks: 'assists', 'bountyLevel', 'deaths', 'doubleKills', 'killingSprees', 'kills', 'largestKillingSpree', 'largestMultiKill', 'pentaKills', 'quadraKills', 'tripleKills'
7. vision: 'detectorWardsPlaced', 'sightWardsBoughtInGame', 'visionScore', 'visionWardsBoughtInGame', 'wardsKilled', 'wardsPlaced'
