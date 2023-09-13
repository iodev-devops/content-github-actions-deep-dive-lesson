from github import Github


def lambda_handler(event, context):
    """Lambda function wrapper
    Args:
        event: trigger event dict
        context: lambda methods and properties
    Returns:
        string: greeting response
    """
    print("Starting functions\n---------------------------------------------")






    def something(myvar: str):
        print(myvar)

    something("hey")

    if event["input"] == "Hello":
        return "World"

    else:
        raise
