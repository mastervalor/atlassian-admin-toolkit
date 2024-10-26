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
    blocks.append({
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": greeting_text
        }
    })

    # First paragraph
    paragraph1 = (
        f"We are reaching out as you have been identified as the creator or updater of the Looker dashboard "
        f"<https://looker.robot.car/dashboards/{str(dashboard_id)}|{dashboard_name}>. We want to inform you that this dashboard currently uses the Jira direct database "
        "as a data source, which will no longer be available after our migration to the cloud. Since Jira is moving "
        "off AWS in line with company initiatives, this database connection will be discontinued."
    )
    blocks.append({
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": paragraph1
        }
    })

    paragraph2 = (
        "We recommend switching to the BQ pipeline as your new data source. You don’t need to wait for the migration—you "
        "can start making the switch now."
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
            "text": header,
            "emoji": True
        }
    })

    # Bullet points
    bullet_points = [
        "- Please go and create a ticket at <https://jira.robot.car/secure/CreateIssue.jspa?issuetype=10202&pid=1900|go/rds> then give us the ticket number here.",
        "- We will work with the data ingest team to get your Jira data part of their pipeline to BQ",
        "- If this dashboard is no longer needed, please do nothing and we will shut down the service alongside our old version of Jira"
    ]

    # Format bullets
    bullets_text = ""
    for point in bullet_points:
        if point.startswith("-"):
            content = point.strip("- ").strip()
            bullets_text += f"• {content}\n"
        else:
            bullets_text += f"{point}\n"

    blocks.append({
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": bullets_text.strip()
        }
    })

    # Closing paragraph
    closing_paragraph = (
        "If you need additional assistance preparing for migration, please let us know how we can help!\n\n"
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
