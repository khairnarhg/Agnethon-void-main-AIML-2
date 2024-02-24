# Load Pkgs
import feedparser
import pandas as pd

url = "https://www.factcheck.org/feed/"

f = feedparser.parse(url)

data = {}
for entry in f.entries:
    data.setdefault('title',[])
    data.setdefault('link',[])
    data['title'].append(entry.title)
    data['link'].append(entry.link)
    
# Create DataFrame from Dictionary
df = pd.DataFrame(data)
print(df)

