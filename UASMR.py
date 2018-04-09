import praw
import os 
import time 

### UnintentionalASMR bot ###

KEYWORDS = ['Unintentional', 'unintentional']
def botlogin():
	r = praw.Reddit(username = "_UASMR_",
				password = "******",
				client_id = ""******",",
				client_secret = ""******",",
				user_agent = "Reposts from /r/asmr to /r/UnintentionalASMR")

	print "Logged in.."
	return r


def runbot(r, reposts):
	for submission in r.subreddit('test').hot(limit = 100):
		if submission not in r.subreddit('tests').top('year'):
			if any(key in submission.title for key in KEYWORDS) and submission.id not in reposts and submission.score > 4:
				r.subreddit('test').submit("(xpost r/asmr) " + submission.title, url = submission.url)
				print("Post resposted!")
				with open ("reposts.txt", "a") as f:
					f.write(submission.id + "\n")

	time.sleep(10)

def get_reposts():
	if not os.path.isfile("reposts.txt"):
		reposts = []
	else:
			with open("reposts.txt", "r") as f:
				reposts = f.read()
				reposts = reposts.split("\n")
				reposts = filter(None, reposts)
	return reposts


r = botlogin()

reposts = get_reposts()
while(True):
	runbot(r, reposts)

