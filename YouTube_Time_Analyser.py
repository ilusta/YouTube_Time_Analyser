import json
from pytube import YouTube 
from datetime import datetime, timedelta
from concurrent.futures import ThreadPoolExecutor


def process_video(video):
    global seconds_total, seconds, minutes, hours, days, video_counter, error_counter

    print("%.2f%%   " % ((video_counter + 1)*100/n), end="")

    try:
        video_counter += 1
        link = video['titleUrl'] 
        yt = YouTube(link)
        
        if yt.length > 86400:
            error_counter += 1
            print("Looks like stream, ignore it")
            return

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


with open('history.json', encoding='utf-8') as f:
    data = json.load(f)

seconds_total = 0
seconds = 0
minutes = 0
hours = 0
days = 0

video_counter = 0
error_counter = 0

n = len(data)

with ThreadPoolExecutor() as executor:
    executor.map(process_video, data)


print("\nDone")
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
print("Estimated total time (videos that were impossible to process are added to calculated time assuming average length) is:")
print("DAYS:HOURS:MIN:SEC")
print("%d:%d:%d:%d\n" % (days, hours, minutes, seconds))
