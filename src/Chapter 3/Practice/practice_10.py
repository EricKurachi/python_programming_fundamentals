"""
Imagine you work at a rehabilitation center for those that suffer from obsessive-compulsive disorders.
You have to write a program that monitors your patients by looking for key words in their daily blogs that they
are required to keep. The words are orderly, shopping, repeat, again, gamble, and bid. If any of these words appear in
their blog entry then you should print “You really need to talk to someone about this”. Otherwise you can print,
“Thanks for updating your blog”. Here is one possible interaction with this program.
"""

contains_keyword = False

keywords = ['orderly', 'shopping', 'repeat', 'again', 'gamble', 'bid']

entry = input('Please make your blog entry for today: ').lower()
blog_words = entry.split()

for word in blog_words:
    if word in keywords:
        contains_keyword = True

if contains_keyword:
    print('You really need to talk to someone about this')
else:
    print('Thanks for updating your blog')
