#model.py
import csv

BB_FILE_NAME = 'umbball.csv'
FB_FILE_NAME  = 'umfootball.csv'

bb_seasons = []
fb_seasons = []

def init_fball(csv_file_name=FB_FILE_NAME):
	global fb_seasons
	with open(csv_file_name) as f:
		reader = csv.reader(f)
		next(reader) # throw away headers
		next(reader) # throw away headers
		fb_seasons = [] # reset, start clean
		for r in reader:
			# convert strings to integers, to correctly order data
			r[3] = int(r[3])
			r[4] = int(r[4])
			r[5] = float(r[6])
			fb_seasons.append(r)

def get_football_seasons(sortby='year', sortorder='desc'):
	global fb_seasons
	if sortby == 'year':
		sortcol = 1
	elif sortby == 'wins':
		sortcol = 3
	elif sortby == 'pct':
		sortcol = 6
	else:
		sortcol = 0
	rev = (sortorder == 'desc')
	sorted_list = sorted(fb_seasons, key=lambda row: row[sortcol], reverse=rev)
	return sorted_list


def init_bball(csv_file_name=BB_FILE_NAME):
	global bb_seasons
	with open(csv_file_name) as f:
		reader = csv.reader(f)
		next(reader) # throw away headers
		next(reader) # throw away headers
		global bb_seasons
		bb_seasons = [] # reset, start clean
		for r in reader:
			# convert strings to integers, to correctly order data
			r[3] = int(r[3])
			r[4] = int(r[4])
			r[5] = float(r[5])
			bb_seasons.append(r)

# after we update the seasos.html template and the app.py route, we need to update the model to handle the new data processing
# def get_bball_seasons(sortby='year', sortorder='desc'):
#     global bb_seasons
#     return bb_seasons


def get_bball_seasons(sortby='year', sortorder='desc'):
	global bb_seasons
	if sortby == 'year':
		sortcol = 1
	elif sortby == 'wins':
		sortcol = 3
	elif sortby == 'pct':
		sortcol = 5
	else:
		sortcol = 0
	rev = (sortorder == 'desc')
	sorted_list = sorted(bb_seasons, key=lambda row: row[sortcol], reverse=rev)
	return sorted_list