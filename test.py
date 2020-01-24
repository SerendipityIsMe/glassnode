import glassnode as gn

df = gn.glassnode(
    '/v1/metrics/indicators/puell_multiple', 
    start = [2020, 1, 13], 
    until = [2020, 1, 15],
    api_key = 'a2b123be-2c50-4dc9-bdf4-cded52c3d1fc', # Generate a key and paste it here! This one is only illustrative.
    status = True, 
    headers = False,
    wait = 2
    )

print(df)

'''
Result:

<Response [200]>
            t         v
0  1578787200  1.092287
1  1578873600  1.033769
'''