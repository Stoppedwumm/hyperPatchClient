# Hyper Patch Registry
## aka MacPatch

## General Information
URL: <https://macpatch-registry.vercel.app>

Host: <https://vercel.com>

Data Types:
* JSON

## Routes
> GET /

### Description
Returns all patches in an array.

### Example Response
```json
[
  {
    "id": "hl2",
    "name": "Half Life 2"
  },
  {
    "id": "test",
    "name": "Text Adventure"
  }
]
```
---
> GET /patch/:patchid/

### Description
Returns patch information.

### Example Response
#### URL
<https://macpatch-registry.vercel.app/patch/hl2>

#### Returns
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
