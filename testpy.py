import sh
from sh import git

statusCheck = git("status")
print(statusCheck)