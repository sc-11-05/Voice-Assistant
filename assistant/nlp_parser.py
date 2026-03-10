def parse_command(command):

    command = command.lower()

    if command.startswith("open"):

        entity = command.replace("open", "").strip()

        browsers = ["chrome", "google chrome", "edge", "microsoft edge", "firefox"]

        if entity in browsers or entity == "":
            return {"intent": "open_browser", "entity": None}

        return {"intent": "open_website", "entity": entity.split()[0]}
        
    if command.startswith("search"):
        query = command.replace("search", "").strip()
        return {"intent": "search_google", "entity": query}

    if "best browser" in command:
        return {"intent": "optimize_browser", "entity": None}
    
    if "browser" in command:
        return {"intent": "open_browser", "entity": None}
    
    if "youtube" in command:
        return {"intent": "open_youtube", "entity": None}

    if "resume" in command:
        return {"intent": "find_resume", "entity": None}



    if "schedule study" in command:
        return {"intent": "schedule", "entity": None}

    if "logic demo" in command:
        return {"intent": "reasoning", "entity": None}

    if "minimax" in command:
        return {"intent": "minimax", "entity": None}

    if "genetic" in command:
        return {"intent": "genetic", "entity": None}
    
    if "annealing" in command:
        return {"intent": "annealing", "entity": None}

    if "dls" in command:
        return {"intent": "dls", "entity": None}
    
    if "iddfs" in command:
        return {"intent": "iddfs", "entity": None}
    
    if "bidirectional" in command:
        return {"intent": "bidirectional", "entity": None}

    if "rbfs" in command:
        return {"intent": "rbfs", "entity": None}

    

    return None