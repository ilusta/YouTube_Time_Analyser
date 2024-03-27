import json
from pytube import YouTube 
from datetime import datetime, timedelta

# Opening JSON file
f = open('history.json', encoding='utf-8')

data = json.load(f)

# Closing file
f.close()

seconds_total = 0
seconds = 0
minutes = 0
hours = 0
days = 0

video_counter = 0
error_counter = 0

n = len(data)

for video in data:

    print("%.2f%%   " % ((video_counter + 1)*100/n), end="")

    try:
        video_counter += 1
        link = video['titleUrl'] 
        yt = YouTube(link)
        
        if yt.length > 86400:
            error_counter += 1
            print("Looks like stream, ignore it")
            continue

        seconds_total += yt.length
        
        seconds += yt.length
        minutes += seconds//60
        hours += minutes//60
        days += hours//24
        seconds = seconds%60
        minutes = minutes%60
        hours = hours%24

        print("%d:%d:%d:%d" % (days, hours, minutes, seconds), end="    ")

    except Exception as e:
        error_counter += 1
        print("Something went wrong")

        if type(e) == KeyboardInterrupt:
            exit(1)
    
    finally:
        print(video['title'])


print("Done")
print("You have watched %d videos" % video_counter)
print("Unable to process %d links\n" % error_counter)

print("Average video duration is:")
avg = seconds_total//(video_counter-error_counter)
d = datetime(1,1,1) + timedelta(seconds=avg)
print("HOURS:MIN:SEC")
print("%d:%d:%d\n" % (d.hour, d.minute, d.second))

print("Time you have spent watching YouTube is:")
print("DAYS:HOURS:MIN:SEC")
print("%d:%d:%d:%d\n" % (days, hours, minutes, seconds))

seconds += avg*error_counter
minutes += seconds//60
hours += minutes//60
days += hours//24
seconds = seconds%60
minutes = minutes%60
hours = hours%24
print("Estimated total time is (videos that were impossible to process are added to calculated time assuming average length):")
print("DAYS:HOURS:MIN:SEC")
print("%d:%d:%d:%d\n" % (days, hours, minutes, seconds))
