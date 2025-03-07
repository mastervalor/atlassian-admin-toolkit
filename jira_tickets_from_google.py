import os.path
import yaml
from jira import JIRA
from credentials import JIRA_CREDENTIALS
import time
import gspread

JIRA_USER = JIRA_CREDENTIALS['user']
JIRA_PASSWORD = JIRA_CREDENTIALS['password']
JIRA_SERVER = 'https://jira.robot.car'
ODD_TEMPLATES = os.environ['HOME'] + "/rim_sandbox/notebooks/odd_templates/"
APPROVED_REQUESTERS = {
    "carpus.chang@getcruise.com",
    "jonathan.tang@getcruise.com",
    "daniel.greinke@getcruise.com",
    "vincent.carrington@getcruise.com"
}

JIRA = JIRA(basic_auth=(JIRA_USER, JIRA_PASSWORD), options={'server': JIRA_SERVER})
SERVICE_ACCOUNT = gspread.service_account(
    os.environ['HOME'] + "/rim_sandbox/notebooks/cruise-systems-test-prd-7c60-023be643b6f7.json")
SHEET = SERVICE_ACCOUNT.open_by_key('1VBNt9yF40RLJ5WdtCb1bp22Lam-T__vUUE-Sw22NbqU')
WORKSHEET = SHEET.worksheet("Form Responses 1")


def format_fields(responses, file):
    # Convert the JIRA ticket yaml template into a dictionary
    with open(file) as f:
        ticket_fields_dict = yaml.safe_load(f)
        # print(ticket_fields_dict)
        for key in ticket_fields_dict:
            if type(ticket_fields_dict[key]) == str:
                ticket_fields_dict[key] = ticket_fields_dict[key].replace("{odd}", responses['odd'])
                ticket_fields_dict[key] = ticket_fields_dict[key].replace("{doc}", responses['doc'])
                ticket_fields_dict[key] = ticket_fields_dict[key].replace("{usr}", responses['usr'])
                ticket_fields_dict[key] = ticket_fields_dict[key].replace("{tod}", responses['tod'])
                ticket_fields_dict[key] = ticket_fields_dict[key].replace("{mkt}", responses['mkt'])
                ticket_fields_dict[key] = ticket_fields_dict[key].replace("{cmt}", responses['cmt'])
            elif type(ticket_fields_dict[
                          key]) == list:  # key == "labels": # only affects MILE tickets for now (02/27/2023)
                # new_list = [i.replace("{mkt}",responses['mkt'].lower()) for i in ticket_fields_dict[key]]
                new_list = []
                for i in ticket_fields_dict[key]:
                    if type(i) == str:
                        new_list.append(i.replace("{mkt}", responses['mkt'].lower()))
                    elif type(i) == dict and bool('value' in i):
                        i['value'] = i['value'].replace("{mkt}", responses['mkt'].upper())
                        new_list.append(i)
                    else:
                        new_list.append(i)
                ticket_fields_dict[key] = new_list
        ticket_fields_dict['description'] = """
                                            | *Requester* | {usr} |
                                            | *Market location* | {mkt} | \n
                                            *Requester comments:*\n{cmt}\n*Details:*\n""".format(usr=responses['usr'],
                                                                                                 mkt=responses['mkt'],
                                                                                                 cmt=responses['cmt'],
                                                                                                 ) + ticket_fields_dict[
                                                'description']
        print(ticket_fields_dict)
        return ticket_fields_dict


def link_tasks(odd):
    # JQL queries
    milestone_query = 'reporter = release_tools and issuetype = Epic and text ~ "{odd}" and createddate > -10m order by createddate desc'.format(
        odd=odd)
    task_query = 'reporter = release_tools and project not in (Milestones, AVBE, QA) and issuetype != Epic and text ~ "{odd}" and createddate > -10m order by createddate desc'.format(
        odd=odd)
    # Identify our milestone ticket
    milestone = JIRA.search_issues(milestone_query)[0]
    # Get a list of the tasks that we created & iterate over them to link to milestone
    tasks = JIRA.search_issues(task_query)
    for task in tasks:
        JIRA.create_issue_link(type='is implemented by', inwardIssue=str(milestone), outwardIssue=str(task))
    return


def get_form_response(wks):
    data = wks.get("A1:H9999")
    # Column indices are indexed to zero
    responses = list()
    for row in range(len(data)):
        if len(data[row]) < 8:
            print("ODD: " + data[row][1])
            print("URL: " + data[row][2])
            print("Row: " + str(row))
            responses.append(data[row] + [row + 1])
    return responses


def create_tickets(responses):
    for filename in os.listdir(ODD_TEMPLATES):
        f = os.path.join(ODD_TEMPLATES, filename)
        if os.path.isfile(f):
            my_dict = format_fields(responses=responses, file=f)
            print(my_dict)
            JIRA.create_issue(fields=my_dict)
    # time.sleep(5)
    # exit()
    link_tasks(odd=responses['odd'])


def main():
    # Check the google sheet
    new_responses = get_form_response(WORKSHEET)
    if len(new_responses) == 0:
        print("No new responses!")
        return
    print(new_responses)
    for response in new_responses:
        response_dict = {
            'odd': response[1],  # ODD name
            'doc': response[2],  # ODD Change doc
            'usr': response[3],  # User who submitted the request
            'tod': response[4],  # Time of day (day/night)
            'mkt': response[5],  # Market location (e.g. AUS, PHX, SFO)
            'cmt': response[6],  # Freeform comment
            'tix': response[7]  # Check that we created tickets (filled in by bot in spreadsheet)
        }
        print("ODD: " + response_dict['odd'] + "\n" +
              "Doc: " + response_dict['doc'] + "\n" +
              "Requester: " + response_dict['usr']
              )
        # Check that responses are from approved users,
        # if not approved user, mark response as rejected
        # without creating any tickets
        if response_dict['usr'] not in APPROVED_REQUESTERS:
            WORKSHEET.update_cell(response_dict['tix'], 8, "rejected")
            continue

        # Try/Except block updates worksheet with error if we fail to generate some tickets.
        # This prevents us from trying to create the same tickets multiple times if there's an issue with
        # one of the templates.
        try:
            create_tickets(responses=response_dict)
        except:
            WORKSHEET.update_cell(response_dict['tix'], 8, "Error: Failed to create tickets")
            exit()

        WORKSHEET.update_cell(response_dict['tix'], 8, "y")
    return


if __name__ == '__main__':
    main()
    # issue = JIRA.search_issues("key=DIS-6233")[0]
    # print(str(issue.raw))
    # print(type(issue.fields.customfield_26407[0]))
    # print(issue.fields.customfield_26407)