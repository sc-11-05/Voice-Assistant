from assistant.controller import handle_command
from assistant.voice import listen, speak

speak("Voice assistant started")

try:

    while True:

        command = listen()

        if not command:
            continue

        if "exit" in command:
            speak("Goodbye")
            break

        handle_command(command)

except KeyboardInterrupt:
    speak("Assistant stopped")
