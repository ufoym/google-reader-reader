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
	fout.write('<html><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8" /></head><body>\n')
	for item in data['items']:
		try:
			title = item['title']
			content = item['content']['content']
		except KeyError:
			continue
		try:
			ad_start_str = config['ad'][item['origin']['title']]
			content = content.split(ad_start_str)[0]
		except KeyError:
			pass
		fout.write('<h1>%s</h1>\n' % title)
		fout.write('<div>%s</div>\n' % content)
	fout.write('</body><html>')