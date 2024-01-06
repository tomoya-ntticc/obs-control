import logging
logging.basicConfig(level=logging.DEBUG)
import asyncio
import simpleobsws

parameters = simpleobsws.IdentificationParameters(ignoreNonFatalRequestChecks = False) # Create an IdentificationParameters object (optional for connecting)

ws = simpleobsws.WebSocketClient(url = 'ws://localhost:4455', password = '', identification_parameters = parameters) # Every possible argument has been passed, but none are required. See lib code for defaults.

async def make_request():
    await ws.connect() # Make the connection to obs-websocket
    await ws.wait_until_identified() # Wait for the identification handshake to complete

    requests = []

    requests.append(simpleobsws.Request('OpenSourceProjector', {'sourceName': 'Camera-1', 'monitorIndex': 0}))
    requests.append(simpleobsws.Request('SetCurrentProgramScene', {'sceneName': 'ChromaKey'}))
    requests.append(simpleobsws.Request('OpenVideoMixProjector', {'videoMixType': 'OBS_WEBSOCKET_VIDEO_MIX_TYPE_PREVIEW', 'monitorIndex': 1}))

    await ws.call_batch(requests, halt_on_failure=False) # Perform the request

    await ws.disconnect() # Disconnect from the websocket server cleanly

loop = asyncio.get_event_loop()
loop.run_until_complete(make_request())