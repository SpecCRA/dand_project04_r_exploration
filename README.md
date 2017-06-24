## Link to data source : https://www.kaggle.com/sfu-summit/starcraft-ii-replay-analysis

# Description of each variable

GameID: Unique ID for each game

LeagueIndex: 1-8 for Bronze, Silver, Gold, Diamond, Diamond, Platinum, Master, Grand Master, and Professional leagues

Age: Age of each player

HoursPerWeek: Hours spent playing per week

TotalHours: Total hours spent playing

APM: Actions per minute (a mouse click or keyboard input)

SelectByHotKeys: Number of unit selections made using hotkeys per timestamp

AssignToHotKeys: Number of unique hotkeys used per timestamp

UniqueHotKeys: Number of unique hotkeys used per timestamp

MinimapAttacks: Number of attacks actions on minimal per timestamp

MinimapRightClicks: Number of right clicks on minimal per timestamp

NumberOfPACs: Number of PACS# per timestamp

GapBetweenPACs: Mean duration between PACs in milliseconds

ActionLatency: Mean latency from the onset of PACs to their first action in milliseconds

ActionsInPAC: Mean number of actions within each PAC

TotalMapExplored: Number of 24x24 game coordinate grids viewed by player per timestamp

WorkersMade: Number of SCVs, drones, or probes trained per timestamp

UniqueUnitsMade: Unique units made per timestamp

ComplexUnitsMade: Number of ghosts, infestors, and high templars trained per timestamp

ComplexAbilityUsed: Abilities requiring specific targeting instructions used per timestamp

MaxTimeStamp: Time stamp of game's last recorded event

# PAC stands for Perception Action Cycle. An APM is a single action by the user. 

One PAC is defined as a shift of the screen to a new location for some time followed by at least one action then shift to another location. The delay to the first action in a PAC turns out to be one of the best predictors across all leagues, and the best in certain leagues (beating out the venerable APM, which, despite it’s faults, is a good predictor of league).
