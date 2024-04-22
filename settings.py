from dotenv import dotenv_values

# app_settings = load_dotenv('.env')
config = dotenv_values('.env')

print(config)