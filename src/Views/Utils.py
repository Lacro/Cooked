
def UserActionSafe(action, parameters) -> None:
    try:
        action(*parameters)
    except Exception as ex:
        print(f"Error during user action {action} with parameters {parameters}: {ex}")
