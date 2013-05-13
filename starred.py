import simplejson as json, sys

reload(sys)
sys.setdefaultencoding( "utf-8" )

if len(sys.argv) < 3:
	print 'Usage: python %s [input json filename] [output html filename]' % sys.argv[0]
	sys.exit()

input_fn = sys.argv[1]
output_fn = sys.argv[2]

config = None
with open('config.json', 'r') as fin:
	config = json.load(fin)

data = None
with open(input_fn, 'r') as fin:
	data = json.load(fin)

with open(output_fn, 'w') as fout:
	fout.write('%s\n' % config['header'])
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
	fout.write(config['footer'])