from workspace.support_ticket_app3.page1 import Context, State

import requests
import json

def assign_issue(state: State, context: Context) -> Context:
    api_key = "lin_api_7BiIKFv9ct2MAnQVqMsfoq42vdujJZVCz69BqnjQ"
    url = 'https://api.linear.app/graphql'

    mark_id = "18606178-4a5c-49b7-825c-e8bee0fdc8d1"
    eng_id = "7df6ca51-cd91-4f42-8d3d-15a99cc54596"

    headers = {
        'Authorization': api_key,
        'Content-Type': 'application/json'
    }

    mutation = '''
    mutation CreateIssue($title: String!, $description: String!, $teamId: String!, $priority: Int!) {
        issueCreate(input: {
            title: $title,
            description: $description,
            teamId: $teamId
            priority: $priority
        }) {
            success
            issue {
                id
                title
            }
        }
    }
    '''

    linear_title = state.widgets.widget1.title
    string_priority = state.widgets.widget1.priority
    linear_priority = int(string_priority)
    linear_team = state.widgets.widget1.team
    team_id = ""
    linear_description = state.widgets.widget1.description

    if linear_team == "MARK":
        team_id = mark_id
    elif linear_team == "ENG":
        team_id = eng_id

    variables = {
        'title': linear_title,
        'description': linear_description,
        'teamId': team_id,
        'priority': linear_priority
    }

    response = requests.post(url, headers=headers, json={'query': mutation, 'variables': variables})
    response_data = response.json()

    issue_data = response_data.get("data", {}).get("issueCreate", {}).get("issue")
    issue_id = issue_data.get("id")

    context.widgets.widget1.message = issue_id
    return context
