def api_message_block(name, svc_name):
    blocks = []

    # Greeting block
    greeting_text = f":wave: Hello {name},"
    blocks.append({
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": greeting_text
        }
    })

    # First paragraph
    paragraph1 = (
        f"We are reaching out to you as the last recorded owner (or manager of the last recorded owner) "
        f"of *{svc_name}*."
    )
    blocks.append({
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": paragraph1
        }
    })

    # Second paragraph
    paragraph2 = (
        "Jira is migrating to the Cloud, and the API between our current version and new version of Jira is different. "
        "We are reaching out to inform you that you must review the new API changes and prepare your services for the cutover."
    )
    blocks.append({
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": paragraph2
        }
    })

    # Divider
    blocks.append({"type": "divider"})

    # Header
    header = "What is needed from you:"
    blocks.append({
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": header
        }
    })

    # Bullet points
    bullet_points = [
        "- To join upcoming UAT sessions, please request access <https://iop.robot.car/groups/cruise/app-atlassian-cloud-test-users?membership|here.>",
        "- Review the documentation of the new API <https://getcruise.atlassian.net/wiki/spaces/IT/pages/99188790/Jira+-+Cloud+API+Changes|here.>",
        "- If your service is no longer needed, please do nothing and we will shut down the service alongside our old version of Jira"
    ]

    # Format bullets
    bullets_text = ""
    for point in bullet_points:
        if point.startswith("-"):
            # Bullet
            content = point.strip("- ").strip()
            bullets_text += f" • {content}\n"
        else:
            bullets_text += f"{point}\n"

    blocks.append({
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": bullets_text
        }
    })

    # Closing paragraph
    closing_paragraph = (
        "If you need additional assistance preparing your service for migration, please let us know how we can help!\n\n"
        "Thank you,\n"
        "*ET Corporate Engineering*"
    )
    blocks.append({
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": closing_paragraph
        }
    })

    return blocks

def looker_message_block(creator, updater, dashboard_name, dashboard_id):
    blocks = []

    # Greeting block
    greeting_text = f":wave: Hello {creator} and {updater},"
    