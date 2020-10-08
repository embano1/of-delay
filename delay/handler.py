import time

# in seconds
sleepSeconds = 1
counter = 0

def handle(event, context):
    global counter
    counter += 1
    # max delay
    if counter > 3:
        counter = 3

    delay = counter * sleepSeconds
    print(f"delaying execution for {delay} seconds")
    time.sleep(delay)
    
    print(event.body,flush=True)
    return {
        "statusCode": 200,
        "body": ""
    }
