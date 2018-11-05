import json
import requests

account_name = input("input account name to query first 100 actions:")
data = '{"account_name":"' + account_name + '","pos":0,"offset":100}'
response = requests.post('https://nodes.get-scatter.com/v1/history/get_actions', data=data)
actionInfo_of_account = json.loads(response.text)
print(actionInfo_of_account)
actions_array_of_account = actionInfo_of_account["actions"]
last_irreversible_block_of_account = actionInfo_of_account["last_irreversible_block"]
print("-------------\n")
first_action_of_account = actions_array_of_account[0]
all_keys_in_actions = first_action_of_account.keys()
print(first_action_of_account.keys())
for key in all_keys_in_actions:
    print(key)
    print(first_action_of_account[key])
    if key == "action_trace":
        trace_content = first_action_of_account[key]
        all_keys_in_trace_content = trace_content.keys()
        print(all_keys_in_trace_content)
        for each in all_keys_in_trace_content:
            print(each)
            print(trace_content[each])
            if each == "receipt":
                print("Found action on account")
                act_content = trace_content["act"]
                if act_content["account"] == "eosio.token" and act_content["name"] == "transfer":
                    print("found transfer token to me, show data in act ")
                    data_in_act = act_content["data"]
                    print(data_in_act)
                    print(data_in_act['to'])
                    print(data_in_act['quantity'])
                    print(data_in_act['memo'])
            print("+++++++++")
        print()
    print("-------")

action_trace_of_this = first_action_of_account



