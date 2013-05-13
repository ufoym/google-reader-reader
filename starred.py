import simplejson as json, sys

reload(sys)
sys.setdefaultencoding( "utf-8" )

config = None
with open('config.json', 'r') as fin:
	config = json.load(fin)

data = None
with open('var/starred.json', 'r') as fin:
	data = json.load(fin)

with open('var/starred.html', 'w') as fout:
	fout.write('<html><head><meta charset="utf-8"><title>Google Reader Reader</title><style type=\"text/css\">article {margin: 200px auto; width: 70%;}</style></head><body>\n')
	for item in data['items']:
		try:
			title = item['title']
			content = item['content']['content']
		except KeyError:
			continue
		try:
			for ad_start_str in config['ad'][item['origin']['title']]:
				content = content.split(ad_start_str)[0]
		except KeyError:
			pass
		fout.write('<article><header><h1>%s</h1></header>' % title)
		fout.write('%s</article>\n' % content)
	fout.write('</body><html>')