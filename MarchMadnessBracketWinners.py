def calculate_win_loss_ratio(wins, losses):
    winsToLosses = float(wins) / (wins + losses)
    return winsToLosses
def make_WLFGP(winsToLosses, fieldGoalPercentage):
    WLFGP = winsToLosses + fieldGoalPercentage
    return WLFGP

class Team:
    def __init__(self, name, wins, losses, fieldGoalPercentage):
        self.name = name
        self.wins = wins
        self.losses = losses
        self.rank = 0
        self.fieldGoalPercentage = fieldGoalPercentage
        self.winsToLosses = calculate_win_loss_ratio(self.wins, self.losses)
        self.WLFGP = make_WLFGP(self.winsToLosses, self.fieldGoalPercentage)  
        
def rankTeams(teams):
    WLFGP_scores = [] 
    for team in teams:
        WLFGP_scores.append(team.WLFGP)
    rank = sorted(WLFGP_scores)
    rankList = []
    used = []
    for score in rank:
        for team in teams:
            if team.WLFGP == score and team not in used:
                rankList.append(team)
                used.append(team)
    for i, team in enumerate(reversed(rankList)):
        team.rank = i+1
    return reversed(rankList)
       
class TeamRankList:
    def __init__(self, teams):
       self.teams = teams
       self.rankList = rankTeams(self.teams)
    def printRanks(self):
        for team in self.rankList:
            print(team.name, team.rank)
    def compare(self, teamName1, teamName2):
        teamDict = {}
        for team in self.teams:
            teamDict[team.name] = team.rank
        if teamDict[teamName1] < teamDict[teamName2]:
            winner = teamName1
        else:
            winner = teamName2
        return winner
            
names = ["Abilene Christian","Air Force","Akron","Alabama A&M","Alabama-Birmingham","Alabama State","Alabama","Albany (NY)","Alcorn State","American","Appalachian State","Arizona State","Arizona","Little Rock","Arkansas-Pine Bluff","Arkansas State","Arkansas","Army","Auburn","Austin Peay","Ball State","Baylor","Belmont","Bethune-Cookman","Binghamton","Boise State","Boston College","Boston University","Bowling Green State","Bradley","Brigham Young","Brown","Bryant","Bucknell","Buffalo","Butler","Cal Poly","Cal State Bakersfield","Cal State Fullerton","Cal State Northridge","California Baptist","UC-Davis","UC-Irvine","UC-Riverside","UC-Santa Barbara","University of California","Campbell","Canisius","Central Arkansas","Central Connecticut State","Central Florida","Central Michigan","Charleston Southern","Charlotte","Chattanooga","Chicago State","Cincinnati","Citadel","Clemson","Cleveland State","Coastal Carolina","Colgate","College of Charleston","Colorado State","Colorado","Columbia","Connecticut","Coppin State","Cornell","Creighton","Dartmouth","Davidson","Dayton","Delaware State","Delaware","Denver","DePaul","Detroit Mercy","Drake","Drexel","Duke","Duquesne","East Carolina","East Tennessee State","Eastern Illinois","Eastern Kentucky","Eastern Michigan","Eastern Washington","Elon","Evansville","Fairfield","Fairleigh Dickinson","Florida A&M","Florida Atlantic","Florida Gulf Coast","Florida International","Florida State","Florida","Fordham","Fresno State","Furman","Gardner-Webb","George Mason","George Washington","Georgetown","Georgia Southern","Georgia State","Georgia Tech","Georgia","Gonzaga","Grambling","Grand Canyon","Green Bay","Hampton","Hartford","Harvard","Hawaii","High Point","Hofstra","Holy Cross","Houston Baptist","Houston","Howard","Idaho State","Idaho","Illinois-Chicago","Illinois State","Illinois","Incarnate Word","Indiana State","Indiana","Iona","Iowa State","Iowa","Purdue-Fort Wayne","IUPUI","Jackson State","Jacksonville State","Jacksonville","James Madison","Kansas State","Kansas","Kennesaw State","Kent State","Kentucky","La Salle","Lafayette","Lamar","Lehigh","Liberty","Lipscomb","Long Beach State","Long Island University","Longwood","Louisiana","Louisiana-Monroe","Louisiana State","Louisiana Tech","Louisville","Loyola (IL)","Loyola Marymount","Loyola (MD)","Maine","Manhattan","Marist","Marquette","Marshall","Maryland-Baltimore County","Maryland-Eastern Shore","Maryland","Massachusetts-Lowell","Massachusetts","McNeese State","Memphis","Mercer","Miami (FL)","Miami (OH)","Michigan State","Michigan","Middle Tennessee","Milwaukee","Minnesota","Mississippi State","Mississippi Valley State","Mississippi","Missouri-Kansas City","Missouri State","Missouri","Monmouth","Montana State","Montana","Morehead State","Morgan State","Mount St. Marys","Murray State","Navy","Omaha","Nebraska","Nevada-Las Vegas","Nevada","New Hampshire","New Mexico State","New Mexico","New Orleans","Niagara","Nicholls State","NJIT","Norfolk State","North Alabama","North Carolina-Asheville","North Carolina A&T","North Carolina Central","North Carolina-Greensboro","North Carolina State","North Carolina-Wilmington","North Carolina","North Dakota State","North Dakota","North Florida","North Texas","Northeastern","Northern Arizona","Northern Colorado","Northern Illinois","Northern Iowa","Northern Kentucky","Northwestern State","Northwestern","Notre Dame","Oakland","Ohio State","Ohio","Oklahoma State","Oklahoma","Old Dominion","Oral Roberts","Oregon State","Oregon","Pacific","Penn State","Pennsylvania","Pepperdine","Pittsburgh","Portland State","Portland","Prairie View","Presbyterian","Princeton","Providence","Purdue","Quinnipiac","Radford","Rhode Island","Rice","Richmond","Rider","Robert Morris","Rutgers","Sacramento State","Sacred Heart","Saint Francis (PA)","Saint Josephs","Saint Louis","Saint Marys (CA)","Saint Peters","Sam Houston State","Samford","San Diego State","San Diego","San Francisco","San Jose State","Santa Clara","Savannah State","Seattle","Seton Hall","Siena","South Alabama","South Carolina State","South Carolina Upstate","South Carolina","South Dakota State","South Dakota","South Florida","Southeast Missouri State","Southeastern Louisiana","Southern California","SIU Edwardsville","Southern Illinois","Southern Methodist","Southern Mississippi","Southern Utah","Southern","St. Bonaventure","St. Francis (NY)","St. Johns (NY)","Stanford","Stephen F. Austin","Stetson","Stony Brook","Syracuse","Temple","Tennessee-Martin","Tennessee State","Tennessee Tech","Tennessee","Texas A&M-Corpus Christi","Texas A&M","Texas-Arlington","Texas Christian","Texas-El Paso","Texas-Rio Grande Valley","Texas-San Antonio","Texas Southern","Texas State","Texas Tech","Texas","Toledo","Towson","Troy","Tulane","Tulsa","UCLA","Utah State","Utah Valley","Utah","Valparaiso","Vanderbilt","Vermont","Villanova","Virginia Commonwealth","VMI","Virginia Tech","Virginia","Wagner","Wake Forest","Washington State","Washington","Weber State","West Virginia","Western Carolina","Western Illinois","Western Kentucky","Western Michigan","Wichita State","William & Mary","Winthrop","Wisconsin","Wofford","Wright State","Wyoming","Xavier","Yale","Youngstown State"]

wins = [23,13,15,5,17,11,17,11,10,15,10,20,17,10,12,12,15,13,20,21,15,19,25,14,9,11,14,14,20,17,19,18,10,19,26,15,6,16,14,13,15,11,25,9,19,7,19,14,11,11,22,20,15,7,12,3,25,12,17,10,14,21,23,12,17,9,14,6,13,16,11,21,19,5,16,8,14,11,23,13,25,19,10,23,14,13,14,12,11,11,9,17,11,17,14,18,23,17,11,20,24,20,16,8,18,20,21,13,11,29,14,18,16,14,17,16,16,16,25,15,11,27,15,10,5,16,16,11,6,15,15,14,20,21,17,16,11,23,12,13,23,22,6,20,24,9,10,18,19,26,24,13,15,15,17,15,24,18,19,19,20,11,5,10,12,23,16,19,6,21,15,10,9,18,11,12,15,23,26,9,9,18,21,6,19,10,16,13,11,14,22,12,9,9,25,11,19,15,16,26,4,26,12,17,13,12,21,19,10,4,17,15,26,20,9,24,15,12,16,20,20,9,20,13,14,23,11,12,13,15,18,13,10,18,23,11,17,17,14,12,17,13,12,14,7,17,17,16,16,22,16,20,14,12,12,16,16,14,13,15,16,13,18,20,9,20,16,19,18,21,4,16,10,16,16,16,14,7,6,14,24,13,18,10,15,15,10,17,13,17,14,6,15,17,20,15,14,7,23,19,21,11,9,8,26,12,13,15,18,8,18,16,18,23,25,16,23,10,11,4,18,16,24,21,15,14,9,23,22,23,10,22,27,13,11,11,23,16,11,7,9,18,8,15,14,18,20,26,19,6,16,19,12]
losses = [6,15,14,25,13,16,12,19,18,14,19,9,13,19,18,17,14,18,9,10,14,10,4,15,21,18,14,17,9,14,12,10,19,11,3,14,21,12,15,17,13,17,5,21,9,22,11,16,18,20,6,9,14,20,19,27,4,17,12,21,14,10,8,17,11,17,15,24,15,13,17,8,10,23,15,22,13,19,8,18,4,10,18,8,17,18,15,17,20,20,21,13,19,12,18,11,6,12,18,8,6,11,13,21,11,10,9,17,18,2,15,10,15,15,13,9,12,14,6,16,16,2,15,17,24,15,15,18,23,15,14,15,9,8,14,15,18,8,20,18,7,7,26,9,5,19,19,12,10,6,6,18,15,16,12,13,5,12,11,12,10,20,25,20,18,6,13,12,24,9,15,19,20,12,19,16,14,6,4,20,22,11,8,25,10,20,15,15,20,14,7,19,19,22,4,18,10,14,13,3,24,4,16,11,18,17,11,11,22,26,12,14,5,9,22,5,15,17,16,10,10,20,9,16,17,8,18,17,16,16,11,15,19,11,6,20,11,12,17,17,11,17,17,15,24,12,14,9,13,7,13,10,14,17,17,14,15,14,14,16,13,16,11,11,21,9,15,10,13,9,24,14,19,13,12,15,15,24,25,15,7,16,11,21,14,14,20,14,15,11,14,23,14,14,10,14,14,24,7,11,8,18,21,23,3,17,15,15,12,19,14,13,11,7,5,14,6,21,17,24,12,13,6,8,13,17,20,6,8,6,20,6,2,16,17,18,6,13,18,24,20,12,21,13,16,11,9,4,12,23,13,6,19]
fieldGoalPercentages = [0.474,0.453,0.405,0.411,0.454,0.405,0.447,0.415,0.411,0.48,0.455,0.446,0.428,0.485,0.425,0.418,0.446,0.428,0.45,0.476,0.473,0.447,0.504,0.444,0.431,0.467,0.437,0.478,0.445,0.438,0.473,0.446,0.422,0.446,0.465,0.446,0.411,0.433,0.459,0.465,0.455,0.432,0.45,0.445,0.455,0.429,0.457,0.436,0.425,0.414,0.472,0.453,0.428,0.414,0.443,0.412,0.435,0.45,0.461,0.436,0.455,0.476,0.481,0.48,0.459,0.45,0.445,0.381,0.433,0.484,0.456,0.454,0.504,0.354,0.456,0.438,0.467,0.417,0.471,0.462,0.482,0.425,0.419,0.489,0.431,0.424,0.453,0.421,0.436,0.425,0.434,0.471,0.438,0.413,0.453,0.444,0.449,0.421,0.407,0.45,0.475,0.484,0.452,0.412,0.448,0.505,0.469,0.434,0.454,0.534,0.445,0.46,0.453,0.434,0.454,0.468,0.453,0.445,0.492,0.461,0.456,0.447,0.433,0.449,0.444,0.46,0.436,0.429,0.458,0.443,0.454,0.452,0.48,0.463,0.48,0.456,0.4,0.459,0.455,0.439,0.434,0.467,0.381,0.434,0.476,0.406,0.449,0.455,0.488,0.49,0.483,0.43,0.44,0.421,0.445,0.451,0.461,0.438,0.437,0.497,0.456,0.459,0.433,0.406,0.449,0.468,0.44,0.434,0.389,0.458,0.474,0.439,0.462,0.461,0.449,0.436,0.432,0.488,0.451,0.422,0.42,0.438,0.474,0.381,0.464,0.432,0.453,0.427,0.405,0.455,0.492,0.426,0.399,0.418,0.497,0.407,0.48,0.427,0.43,0.464,0.376,0.456,0.427,0.443,0.422,0.42,0.447,0.442,0.389,0.404,0.462,0.46,0.461,0.468,0.441,0.47,0.451,0.463,0.447,0.444,0.483,0.432,0.466,0.47,0.419,0.483,0.41,0.403,0.398,0.469,0.445,0.438,0.421,0.444,0.419,0.457,0.466,0.447,0.425,0.417,0.455,0.442,0.42,0.426,0.416,0.431,0.447,0.413,0.417,0.451,0.423,0.463,0.422,0.428,0.48,0.447,0.435,0.418,0.447,0.463,0.435,0.41,0.419,0.473,0.425,0.442,0.469,0.448,0.46,0.468,0.404,0.45,0.397,0.444,0.446,0.431,0.459,0.426,0.415,0.424,0.505,0.442,0.432,0.44,0.437,0.458,0.417,0.47,0.433,0.469,0.443,0.435,0.436,0.422,0.458,0.462,0.443,0.405,0.421,0.424,0.438,0.444,0.432,0.416,0.502,0.429,0.438,0.408,0.455,0.408,0.412,0.436,0.441,0.453,0.474,0.438,0.454,0.432,0.454,0.408,0.456,0.462,0.469,0.486,0.466,0.453,0.427,0.453,0.442,0.443,0.426,0.478,0.482,0.39,0.396,0.453,0.458,0.481,0.411,0.455,0.438,0.453,0.429,0.408,0.474,0.459,0.459,0.489,0.441,0.413,0.47,0.497,0.426]        

teams = []
for i in range(len(names)):
    team = Team(names[i], wins[i], losses[i], fieldGoalPercentages[i])
    teams.append(team)
    
teamRankList = TeamRankList(teams)
