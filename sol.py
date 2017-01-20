def split_show_views(line):
    kv = line.split(",")
    show = kv[0]
    views = int(kv[1])
    return (show, views)

show_views = show_views_file.map(split_show_views)
show_views.collect()


def split_show_channel(line):
    kv = line.split(",")
    show = kv[0]
    channel = kv[1]
    return (show, channel)

show_channel = show_channel_file.map(split_show_channel)
show_channel.collect()


joined_dataset = show_channel.join(show_views)
joined_dataset.collect()

def extract_channel_views(show_views_channel):
    channel = show_views_channel[1][0]
    views = int(show_views_channel[1][1])
    return (channel, views)

channel_views = joined_dataset.map(extract_channel_views)
channel_views.collect()


def some_function(a, b):
    return a + b
channel_views.reduceByKey(some_function).collect()

