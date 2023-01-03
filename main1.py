import PocketBase from 'pocketbase'

client = PocketBase('http://127.0.0.1:8090')

...

user_data = client.users.auth_via_email()
