# obs-control

### Prerequisites

- OBS Studio 30.0.2
- Python 3.10.13
    - [obs-websocket-py](https://github.com/Elektordi/obs-websocket-py)
    - [simpleobsws](https://github.com/IRLToolkit/simpleobsws)
- macOS Monterey (12.6.1)

### Features

- Output to 2 Monitors from 1 Camera Source.
- Sync 2 Movie Souces.
- Put OBS into operational state when booting OS.

### System Diagram

![SystemDiagram](https://github.com/tomoya-ntticc/obs-control/assets/94507251/17d21309-7441-4be7-aa94-b821e37f03c3)

## Setup

### OBS WebSocket Server

Turn ON `Enable WebSocket server` of `WebScoket Server Settings` of `Tools`
![スクリーンショット 2024-01-10 16 27 23](https://github.com/tomoya-ntticc/obs-control/assets/94507251/61e7822d-f76d-4ed3-9b07-d2fff31d779e)

### OBS Scenes and Sources

Set Scenes name `Moniter` and `ChromaKey` .  
Set Sources name `Text` and `Movie` to sync movies.
![スクリーンショット 2024-01-10 12 29 52](https://github.com/tomoya-ntticc/obs-control/assets/94507251/96fe2b2f-6db3-4bde-a3b2-0e8f3d40ed2f)

Add Filters.
![スクリーンショット 2024-01-10 12 31 43](https://github.com/tomoya-ntticc/obs-control/assets/94507251/2e2208f6-c517-4b10-9782-9a429bb41459)

### OBS Studio Mode

Turn ON `Stduio Mode` of `Controls`

## Additional Documentation and Acknowledgments

* obs-websocket docs: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md
