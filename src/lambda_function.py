import json
import os
import slackweb

print('Loading function')

def lambda_handler(event, context):
    url = os.getenv("SLACKURL", None)
    if url is None: exit(1)

    print("Received event: " + json.dumps(event, indent=2))

    channel = os.getenv("CHANNEL", "#sns")
    name = os.getenv("NAME", "SNS")
    color = os.getenv("COLOR", "good")
    slack = slackweb.Slack(url=url)
    message = event['Records'][0]['Sns']['Message']

    slack.notify(channel=channel,
                 username=name,
                 attachments=[
                     {
                         'color': color,
                         'text': message,
                     }
                 ]
    )

    return message
