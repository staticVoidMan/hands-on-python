import os

DEVELOPMENT = "development"
STAGING = "staging"
PRODUCTION = "production"
CODE_SPACE = "code_space"
LOCAL = "local"

current_env = os.environ.get("ENV_NAME", DEVELOPMENT)

if current_env == DEVELOPMENT:
  print("Dev environment")
elif current_env == STAGING:
  print("Stg environment")
elif current_env == PRODUCTION:
  print("Prod environment")
elif current_env in [CODE_SPACE, LOCAL]:
  print("Local environment")
else:
  print("Unknown environment")