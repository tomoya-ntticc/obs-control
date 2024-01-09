import logging
logging.basicConfig(level=logging.DEBUG)
import asyncio
import simpleobsws
import time

parameters = simpleobsws.IdentificationParameters(ignoreNonFatalRequestChecks = False) # Create an IdentificationParameters object (optional for connecting)

ws = simpleobsws.WebSocketClient(url = 'ws://localhost:4455', password = '', identification_parameters = parameters) # Every possible argument has been passed, but none are required. See lib code for defaults.

async def make_requests(requests = []):
    await ws.connect() # Make the connection to obs-websocket
    await ws.wait_until_identified() # Wait for the identification handshake to complete

    await ws.call_batch(requests, halt_on_failure=False) # Perform the requests
    await ws.disconnect() # Disconnect from the websocket server cleanly

loop = asyncio.get_event_loop()
program_out = [
    simpleobsws.Request('OpenVideoMixProjector', {'videoMixType': 'OBS_WEBSOCKET_VIDEO_MIX_TYPE_PROGRAM', 'monitorIndex': 0}),
    simpleobsws.Request('SetCurrentProgramScene', {'sceneName': 'Monitor'})
]
loop.run_until_complete(make_requests(program_out))
time.sleep(1)
preview_out = [
    simpleobsws.Request('OpenVideoMixProjector', {'videoMixType': 'OBS_WEBSOCKET_VIDEO_MIX_TYPE_PREVIEW', 'monitorIndex': 1}),
    simpleobsws.Request('SetCurrentPreviewScene', {'sceneName': 'ChromaKey'})
]
loop.run_until_complete(make_requests(preview_out))
time.sleep(1)
movies_sync = [
    simpleobsws.Request('TriggerMediaInputAction', {'inputName': 'Text', 'mediaAction': 'OBS_WEBSOCKET_MEDIA_INPUT_ACTION_RESTART'}),
    simpleobsws.Request('TriggerMediaInputAction', {'inputName': 'Movie', 'mediaAction': 'OBS_WEBSOCKET_MEDIA_INPUT_ACTION_RESTART'})
]
loop.run_until_complete(make_requests(movies_sync))
