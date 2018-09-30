# -*- coding: utf-8 -*-
import web
import json
from jwcrypto import jwk, jwe
from jwcrypto.common import json_encode, json_decode

urls = (
    '/', 'fetch',
)
predefine_pub = {"e":"AQAB","kty":"RSA","n":"nkSX9v8WZbd5FeE5n0oTKznmjnwN1e9UJ29gaghNbpM1GOCE0y708YXXOUvLvaI4nxHrRjq9WgRrWY_0ys_Ny0TyeyyhUmJhGk2OahwbIJ0kSb7ERTvvZ6rVXwjQ1Kge27NP9YJIX5QOZUawLRRuc6Vw4Z66BTlPZ0WrNTY96BBsQiaseR1B_PKvZgcORcFNdah62GkQRTFq05L3nheLrOKl6h4BFCP_rI8F2oQmgYjMLpumDlPZWfjA6sEckz64l1wmgPhrIodKTf4GqTOQ9K5xwGkYwdz41SUechvuz9_SSRRNjjowFdTo4s8lVK_C4S4IHJ8ulRjMhE-uzCXNxQ"}

predefine_priv = {"d":"djzmjvd5gxoz0t3FT7RmZ7fFABO7vmUjKKbzj6OOPZqqY2Bwutjs03dbGAoBNzX3OReI_pmplpOQo4OBrPbcVwy2XsEz8DlhM-ZXC_zdY1sinhlvxg2FyJv-9hW-9fB3xUjL5q2jZgxVSOIrgjIuZiVmFJihfn-XS57nzkQssa5OTd7awDT118CX1Ugs3Yg5Q-C9Au0dMig2F9X0TFKEfp_efpckUb5WlX7T42IliX4k91N1sXeTes2MltJ2JvcOm7XQtt54Ap3UXqjI7cTDcZN0qsPCUmUwAoBzXY9YjTOLuVTS3T6RDi3WqNgILbLK_1ZooogM64Nzr3DR4yeXAQ","dp":"ddhsudpiQw1gGKRmgU-JgjrGdIsjyTKdPoACoSdoCvXgjoOmSh1gJbS2chaLPE9_1htooYiVwEC_4QcBdM3QOlRwHekjOR_n0RFez3eJF2jMnwYka_H4qZDF3LNUvIwwSNNONoWnJKd50-vxTQFOfL4dPzESsuVPi4mtGB_OGYE","dq":"PvGRC32t1MpuBpB1ooXkaY7aj8ctZWv1ibqlXWQ-lfR-6imLLpyJKQmb552UhOsARFx8veYsUwnb38i_IuxunG_JE8F0V4vKb4iI45p2X2UrzHQC-1oPhCH01OtLE8N4AlsJZ6sOFg4yMGqWbIQ76iV9s5x_YiKyFhJkC1FzHw0","e":"AQAB","kty":"RSA","n":"nkSX9v8WZbd5FeE5n0oTKznmjnwN1e9UJ29gaghNbpM1GOCE0y708YXXOUvLvaI4nxHrRjq9WgRrWY_0ys_Ny0TyeyyhUmJhGk2OahwbIJ0kSb7ERTvvZ6rVXwjQ1Kge27NP9YJIX5QOZUawLRRuc6Vw4Z66BTlPZ0WrNTY96BBsQiaseR1B_PKvZgcORcFNdah62GkQRTFq05L3nheLrOKl6h4BFCP_rI8F2oQmgYjMLpumDlPZWfjA6sEckz64l1wmgPhrIodKTf4GqTOQ9K5xwGkYwdz41SUechvuz9_SSRRNjjowFdTo4s8lVK_C4S4IHJ8ulRjMhE-uzCXNxQ","p":"0LmLpVVOc9Bd6ZZcnBGeyvbi1y2DMRjFfZuiMU1CwK5Q-jQkyouFbLlVxJANoqyFmClH-SUs4SWRkIxhcIEbcJ_rGDWyHOLEzD5gc0d48VT5SayH5QjDWUz4xf1FK7e_m_R7G35NedqL3HNv_XjV9phOBcW0Hf-2ZH5PMDNoBcE","q":"wh1q2mM07Qeoy52bTZwfK3Fe-Fjq0UOOZdffz-4Gv5m2L-DXAfXOUKwuCEgi0gNETtdhZonpMtOMIe4uqgTcdhWhMEbVpQCdOQDuw1y4uBzzNtJArpcfJHuDIvjz5_AMNoj3OgJoBdV6lJc95WjGBlp3oouz_ogB78qKAEhz8QU","qi":"e8tF0pisWwcZSH1j4WiGcZoYy6yXAinOfdNfdYhqC6WvCzw0y--n8-xW9CJ5JPPdJ-rXlUnOMOdyRyOtieKLrv4QvOASEMkJut0oztxlqaRxu26QyuWB1QeokJfrKfbH5OgzASOomQesPbFiU_5U7jltVfrgj0atKCcORfwM-t8"}
merge_priv = {**predefine_pub, **predefine_priv}
merge_priv["use"] = "enc"

print('paste jwe result generated by web console')
class fetch:
    def GET(self):
        web.header('Access-Control-Allow-Origin',      '*')
        web.header('Content-Type', 'application/json')
        mixindata = web.input(code = "no")
        print(mixindata)
        if mixindata.code == "code":
            return "I don't know you, can not give your bonus"
        print(mixindata.code)
        print("-------private key-------")
        print(type(mixindata.code))
        print(len(mixindata.code))
        private_key = jwk.JWK(**merge_priv)
        jwetoken = jwe.JWE()
        jwetoken.deserialize(mixindata.code, key=private_key)
        payload = jwetoken.payload
        print(payload)
        result = json.loads(payload)
        result["use"] = "enc"
        public_key = jwk.JWK(**result)
        toclient_payload = json.dumps([{"type":"ss", "server":"1.1.1.1", "port":1984, "method":"aes-cfb-256", "key":"romanholidy3947"},{"type":"ss", "server":"2.2.1.1", "port":11984, "method":"aes-cfb-256", "key":"juventus_suck"}])
        if "alg" in result:
            algorithm = result["alg"]
        else:
            algorithm = "RSA-OAEP"
        if "enc" in result:
            enc = result["enc"]
        else:
            enc = "A256GCM"
        protected_header = {"alg": algorithm ,"enc": enc,"typ": "JWE"}
        jweresult = jwe.JWE(toclient_payload.encode('utf-8'), recipient=public_key, protected=protected_header)
        print(jweresult.serialize(True))
        return  jweresult.serialize(True)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()