INTENTS = {

    "open_youtube": [
        "youtube",
        "open youtube",
        "play youtube",
        "watch youtube"
    ],

    "open_browser": [
        "browser",
        "open browser",
        "internet"
    ],

    "open_vscode": [
        "vscode",
        "code editor",
        "open vscode"
    ],

    "open_project": [
        "open project",
        "project"
    ],

    "search_google": [
        "search",
        "google"
    ]

}


def detect_intent(command):

    for intent, phrases in INTENTS.items():

        for phrase in phrases:

            if phrase in command:
                return intent

    return None