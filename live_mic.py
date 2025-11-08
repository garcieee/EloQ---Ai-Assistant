import assemblyai as aai
from assemblyai.streaming.v3 import (
    BeginEvent,
    StreamingClient,
    StreamingClientOptions,
    StreamingError,
    StreamingEvents,
    StreamingParameters,
    TerminationEvent,
    TurnEvent,
)
import os
from responses import get_response, get_intent

# --- LOAD API KEY ---
with open("api_key.txt", "r") as f:
    api_key = f.read().strip()

# --- CALLBACKS ---
def on_begin(client: StreamingClient, event: BeginEvent):
    print("Session started! Talk now...")

def on_turn(client: StreamingClient, event: TurnEvent):
    # Only print when you FINISH talking
    if event.transcript and event.end_of_turn:
        text = event.transcript
        # Get intent and response
        intent = get_intent(text)
        response = get_response(intent)
        
        if not response:
            response = "I received your message: " + text
            
        print(f"You said: {text}")
        print(f"Bot response: {response}")

def on_terminated(client: StreamingClient, event: TerminationEvent):
    print(f"Session ended: {event.audio_duration_seconds} seconds")

def on_error(client: StreamingClient, error: StreamingError):
    print(f"Error: {error}")

# --- START LIVE MIC ---
def start_mic():
    client = StreamingClient(
        StreamingClientOptions(
            api_key=api_key,
            api_host="streaming.assemblyai.com",
        )
    )

    client.on(StreamingEvents.Begin, on_begin)
    client.on(StreamingEvents.Turn, on_turn)
    client.on(StreamingEvents.Termination, on_terminated)
    client.on(StreamingEvents.Error, on_error)

    client.connect(
        StreamingParameters(
            sample_rate=16000,
            format_turns=True,
        )
    )

    print("\nLIVE MIC ON! Talk now. (Ctrl+C to stop)\n")
    try:
        mic_stream = aai.extras.MicrophoneStream(sample_rate=16000)
        client.stream(mic_stream)
    except KeyboardInterrupt:
        print("\nStopping...")
    finally:
        client.disconnect(terminate=True)

if __name__ == "__main__":
    start_mic()