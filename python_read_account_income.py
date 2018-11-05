import json
import requests

account_name = input("input account name to query first 100 actions:")
data = '{"account_name":"' + account_name + '","pos":0,"offset":100}'
response = requests.post('https://nodes.get-scatter.com/v1/history/get_actions', data=data)
actionInfo_of_account = json.loads(response.text)
actions_array_of_account = actionInfo_of_account["actions"]
last_irreversible_block_of_account = actionInfo_of_account["last_irreversible_block"]
print("-------------\n")
for first_action_of_account in actions_array_of_account:
    all_keys_in_actions = first_action_of_account.keys()
    for key in all_keys_in_actions:
        if key == "action_trace":
            trace_content = first_action_of_account[key]
            all_keys_in_trace_content = trace_content.keys()
            for each in all_keys_in_trace_content:
                if each == "receipt":
                    act_content = trace_content["act"]
                    if act_content["account"] == "eosio.token" and act_content["name"] == "transfer":
                        data_in_act = act_content["data"]
                        if data_in_act['to'] == account_name:
                            print("found transfer token related with me, show data in act ")
                            print(data_in_act)
                            print(data_in_act['to'])
                            print(data_in_act['quantity'])
                            print(data_in_act['memo'])




