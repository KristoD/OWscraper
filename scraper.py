import requests, json
from lxml import html

page = requests.get('https://playoverwatch.com/en-us/career/pc/Kristo-11726 ')
tree = html.fromstring(page.content)

res = {}
no_profile = tree.xpath("//h1[@class='u-align-center']/text()")
private_profile = tree.xpath("//h3[@class='h4']/text()")
if(no_profile):
    res.error = "Profile does not exist"
elif(private_profile):
    res.error = "Profile is private. Overwatch defaults profiles to private. To make it public, in game go to Settings > Social > Set career profile to public. Exit game for changes to be made"
    print('Exit game for changes to be made')
else:
    titles = tree.xpath("//div[@data-group-id='stats'][1]//div//div[@class='card-stat-block']//table[@class='data-table']//tbody//tr//td[1]/text()")
    values = tree.xpath("//div[@data-group-id='stats'][1]//div//div[@class='card-stat-block']//table[@class='data-table'][1]//tbody//tr//td[2]/text()")
    print("Title", titles)
    print("Values", values)

    for i in range(0, len(titles)):
        res[titles[i]] = values[i]

res = json.dumps(res)
res = json.loads(res)
return res
