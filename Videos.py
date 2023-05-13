import webbrowser as wb
import csv

"open links"
def video_application(content):
    links_info = []
    with open(f"{content}.txt", 'r') as data:
        for line in data:
            info = [i.rstrip().lstrip() for i in line.split(',')]
            length = len(info)
            if length == 2 or length == 3:
                links_info.append(info)
            else:
                links_info.append(False)
    print(links_info)
    return links_info

def open_video(video_link):
    try:
        wb.open(video_link)
    except:
        print("Link Not Found")
