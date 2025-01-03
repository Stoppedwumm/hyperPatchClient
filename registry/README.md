# Registry Guidelines
## General Rules
* No malware
* Code has to work
* If you get banned for modding the game with your patch, it is considered part malware
* Sponsorships are okay, paywalls not
* The user has to own the game, else it is piracy.
* You have to publish it on github

## Format
A patch is structured like this:
```json
{
  "owner": "bBcLn06G22SLux2kEC8Sovf0lQE2",
  "downloadYear": 2025,
  "downloads": {
    "January": 4,
    "February": 0,
    "March": 0,
    "April": 0,
    "May": 0,
    "June": 0,
    "July": 0,
    "August": 0,
    "September": 0,
    "October": 0,
    "November": 0,
    "December": 0
  },
  "game_name": "Half Life 2",
  "language": "python",
  "github": "https://github.com/Stoppedwumm/halflife2patcher",
  "downloadableExec": true
}
```

### Explanation
#### Owner
The UserId of the owner

#### Download Year
Last Year where analytics were updated

#### Downloads
Downloads in months (needed for analytics)

#### Game Name
The name of the game to be patched.

#### Language
The language the patch/patcher is written in

#### Github
The github URL

#### downloadableExec
An boolean, representing if you can download an build from GitHub Releases.

### Code format
The format of code and codebase is not defined, the only rules you have to follow are
a) If you have ```downloadableExec``` enabled, you have to only publish **one asset so you can execute it with ```./executable```**

b) If you don't have ```downloadableExec``` enabled, you have to have a ```install.sh``` script in the root of the repo

## Requesting the Patch.
Almost there! Fill out this form:
<https://form.jotform.com/243494798522066>
(We are working on a dashboard, jotform is only temporary)
