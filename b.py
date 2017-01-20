show_views_file = sc.textFile("input_assign2/join2_gennum?.txt")
show_views_file.take(2)

def split_show_views(line):
   show, views = line.split(',')
   return (show, views)


#
show_views = show_views_file.flatMap(split_show_views)
show_views = show_views_file.map(split_show_views)


show_channel_file = sc.textFile("input_assign2/join2_genchan?.txt")

def split_show_channel(line):
    show, channel = line.split(',')
    return (show, channel)

show_channel = show_channel_file.map(split_show_channel)


