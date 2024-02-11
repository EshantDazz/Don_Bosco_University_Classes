import os
from dotenv import load_dotenv
load_dotenv('myenv\.env')
eshant=os.environ.get('a')
print(eshant)
don_bosco=os.environ.get('b')
print(don_bosco)