def get_api_info() -> dict[str]:
    """Get basic information about the API."""
    info = {
        "status": "success",
        "message": "Welcome to the Just'AIce API!",
        "version": "0.1",
    }

    return info


def get_answer_from_chat(query: str) -> str:
    return {"content": query + " " + "Et moi je suis le chat!"}
