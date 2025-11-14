import traceback

def LogError(msg: str) -> None:
    print(traceback.format_exc())
    print(msg)
