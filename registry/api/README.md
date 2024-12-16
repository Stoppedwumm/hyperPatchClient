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
  "game_name": "Half Life 2",
  "language": "python",
  "downloadableExec": true,
  "github": "https://github.com/Stoppedwumm/halflife2patcher"
}
```
