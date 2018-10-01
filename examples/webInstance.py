# -*- coding: utf-8 -*-
import web
import json
from jwcrypto import jwk, jwe, jws
from jwcrypto.common import json_encode, json_decode
import base64
import base58
import hashlib
import time
urls = (
    '/', 'fetch',
)
predefine_pub = {"kid":"server_kid", "e":"AQAB","kty":"RSA","n":"nkSX9v8WZbd5FeE5n0oTKznmjnwN1e9UJ29gaghNbpM1GOCE0y708YXXOUvLvaI4nxHrRjq9WgRrWY_0ys_Ny0TyeyyhUmJhGk2OahwbIJ0kSb7ERTvvZ6rVXwjQ1Kge27NP9YJIX5QOZUawLRRuc6Vw4Z66BTlPZ0WrNTY96BBsQiaseR1B_PKvZgcORcFNdah62GkQRTFq05L3nheLrOKl6h4BFCP_rI8F2oQmgYjMLpumDlPZWfjA6sEckz64l1wmgPhrIodKTf4GqTOQ9K5xwGkYwdz41SUechvuz9_SSRRNjjowFdTo4s8lVK_C4S4IHJ8ulRjMhE-uzCXNxQ"}

predefine_priv = {"kid":"server_kid","d":"djzmjvd5gxoz0t3FT7RmZ7fFABO7vmUjKKbzj6OOPZqqY2Bwutjs03dbGAoBNzX3OReI_pmplpOQo4OBrPbcVwy2XsEz8DlhM-ZXC_zdY1sinhlvxg2FyJv-9hW-9fB3xUjL5q2jZgxVSOIrgjIuZiVmFJihfn-XS57nzkQssa5OTd7awDT118CX1Ugs3Yg5Q-C9Au0dMig2F9X0TFKEfp_efpckUb5WlX7T42IliX4k91N1sXeTes2MltJ2JvcOm7XQtt54Ap3UXqjI7cTDcZN0qsPCUmUwAoBzXY9YjTOLuVTS3T6RDi3WqNgILbLK_1ZooogM64Nzr3DR4yeXAQ","dp":"ddhsudpiQw1gGKRmgU-JgjrGdIsjyTKdPoACoSdoCvXgjoOmSh1gJbS2chaLPE9_1htooYiVwEC_4QcBdM3QOlRwHekjOR_n0RFez3eJF2jMnwYka_H4qZDF3LNUvIwwSNNONoWnJKd50-vxTQFOfL4dPzESsuVPi4mtGB_OGYE","dq":"PvGRC32t1MpuBpB1ooXkaY7aj8ctZWv1ibqlXWQ-lfR-6imLLpyJKQmb552UhOsARFx8veYsUwnb38i_IuxunG_JE8F0V4vKb4iI45p2X2UrzHQC-1oPhCH01OtLE8N4AlsJZ6sOFg4yMGqWbIQ76iV9s5x_YiKyFhJkC1FzHw0","e":"AQAB","kty":"RSA","n":"nkSX9v8WZbd5FeE5n0oTKznmjnwN1e9UJ29gaghNbpM1GOCE0y708YXXOUvLvaI4nxHrRjq9WgRrWY_0ys_Ny0TyeyyhUmJhGk2OahwbIJ0kSb7ERTvvZ6rVXwjQ1Kge27NP9YJIX5QOZUawLRRuc6Vw4Z66BTlPZ0WrNTY96BBsQiaseR1B_PKvZgcORcFNdah62GkQRTFq05L3nheLrOKl6h4BFCP_rI8F2oQmgYjMLpumDlPZWfjA6sEckz64l1wmgPhrIodKTf4GqTOQ9K5xwGkYwdz41SUechvuz9_SSRRNjjowFdTo4s8lVK_C4S4IHJ8ulRjMhE-uzCXNxQ","p":"0LmLpVVOc9Bd6ZZcnBGeyvbi1y2DMRjFfZuiMU1CwK5Q-jQkyouFbLlVxJANoqyFmClH-SUs4SWRkIxhcIEbcJ_rGDWyHOLEzD5gc0d48VT5SayH5QjDWUz4xf1FK7e_m_R7G35NedqL3HNv_XjV9phOBcW0Hf-2ZH5PMDNoBcE","q":"wh1q2mM07Qeoy52bTZwfK3Fe-Fjq0UOOZdffz-4Gv5m2L-DXAfXOUKwuCEgi0gNETtdhZonpMtOMIe4uqgTcdhWhMEbVpQCdOQDuw1y4uBzzNtJArpcfJHuDIvjz5_AMNoj3OgJoBdV6lJc95WjGBlp3oouz_ogB78qKAEhz8QU","qi":"e8tF0pisWwcZSH1j4WiGcZoYy6yXAinOfdNfdYhqC6WvCzw0y--n8-xW9CJ5JPPdJ-rXlUnOMOdyRyOtieKLrv4QvOASEMkJut0oztxlqaRxu26QyuWB1QeokJfrKfbH5OgzASOomQesPbFiU_5U7jltVfrgj0atKCcORfwM-t8"}
merge_priv = {**predefine_pub, **predefine_priv}
merge_priv["use"] = "enc"
merge_signature_priv = {**predefine_pub, **predefine_priv}
merge_signature_priv["use"] = "sig"

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
        private_key_server = jwk.JWK(**merge_priv)
        jwetoken = jwe.JWE()
        print("before decrypt")
        jwetoken.deserialize(mixindata.code, key=private_key_server)

        print("after decrypt")
        payload_from_client = jwetoken.payload
        print(payload_from_client)
        client_payload = json.loads(payload_from_client)
        client_public_key_in_jwk = client_payload["key"]
        client_public_key_in_jwk["use"] = "sig"
        public_key_verify = jwk.JWK(**client_public_key_in_jwk)
        client_id_signature = client_payload["signature"]
        client_request = client_payload["request"]
        jws_verify_token = jws.JWS()
        jws_verify_token.deserialize(client_id_signature)
        jws_verify_token.verify(public_key_verify, "RS256")
        client_signature_payload = jws_verify_token.payload.decode("utf-8")
        print("verify signature of client")
        print(client_signature_payload)
        dict_client_signature_payload = json.loads(client_signature_payload)
        client_public_key_kid_payload = dict_client_signature_payload["kid"]
        ts_of_sign = dict_client_signature_payload["ts"]/1000
        print("signature happen on ")
        print(ts_of_sign)
        current_server_ts = time.time()
        print(current_server_ts)
        ts_diff = current_server_ts - ts_of_sign
        if ts_diff < 60 and ts_diff >= 0:
            print("client's ts is very close to me")
            print(ts_diff)
        else:
            return web.notfound

        firstHashEngine = hashlib.sha256()
        firstHashEngine.update(client_public_key_in_jwk["n"].encode('utf-8'))
        single_hash256_result = firstHashEngine.digest()
        secondHashEngine = hashlib.sha256()
        secondHashEngine.update(single_hash256_result)
        double_hash256_result = secondHashEngine.digest()
        print("raw hash256 result is:")
        print(single_hash256_result)
        encoded_result = base58.b58encode(single_hash256_result).decode("utf-8")
        print("base58 encode of SHA256 result of client's public key:" + encoded_result)

        print("raw double sha256:")
        print(double_hash256_result)
        doublehash_encoded_result = base58.b58encode(double_hash256_result).decode("utf-8")
        print("base58 encode of double SHA256 result of client's public key:" + doublehash_encoded_result)
        if client_public_key_kid_payload == doublehash_encoded_result:
            print("the signature is verified by client's public key, the payload is same as my calculated result")
        else:
            return web.notfound
        if client_request == "ss_cert":
            print("got your command")
        else:
            return web.notfound
        client_public_key_in_jwk["use"] = "enc"
        public_key_enc = jwk.JWK(**client_public_key_in_jwk)
        toclient_payload = json.dumps([{"type":"ss", "server":"1.1.1.1", "port":1984, "method":"aes-cfb-256", "key":"romanholidy3947"},{"type":"ss", "server":"2.2.1.1", "port":11984, "method":"aes-cfb-256", "key":"juventus_suck"}])
        jwstoken = jws.JWS(toclient_payload.encode('utf-8'))
        print("before sign")
        key_for_signature = jwk.JWK(**merge_signature_priv)
        if "kid" in merge_signature_priv:
            kid = merge_signature_priv["kid"]
        else:
            kid = "hello"
        jwstoken.add_signature(key_for_signature, "RS256", json_encode({"alg":"RS256", "kid":kid}), None)
        print("after sign")
        signed_payload = jwstoken.serialize()
        print("signed:" + signed_payload)
        if "alg" in client_public_key_in_jwk:
            algorithm = client_public_key_in_jwk["alg"]
        else:
            algorithm = "RSA-OAEP"
        if "enc" in client_public_key_in_jwk:
            enc = client_public_key_in_jwk["enc"]
        else:
            enc = "A256GCM"

        protected_header = {"alg": algorithm ,"enc": enc,"typ": "JWE"}
        jweresult = jwe.JWE(signed_payload.encode('utf-8'), recipient=public_key_enc, protected=protected_header)
        print(jweresult.serialize(True))
        return  jweresult.serialize(True)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
