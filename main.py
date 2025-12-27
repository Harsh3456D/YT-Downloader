import yt_dlp

def downloadVideo(url, resolution):
    
    ydl_opts = {
        'format' : f'bestvideo[height<={resolution}]+bestaudio/best[height<={resolution}]',
        'outtmpl' : 'downloads/%(title)s.%9(ext)s',
        'merge_output_format' : 'mp4',
        'progress_hooks': [progress_hook],
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Searching for {resolution}p version --")
            ydl.download([url])
            print("\nDownloaded. Kindly check the download folder.")
            
    except Exception as e:
        print("Error", e)
        
def downloadmp3(url):
    ydl_otps = {
        'format': 'bestaudio/best',
        'outtmpl' : 'music/%(title)s.%(ext)s',
        'progress_hooks': [progress_hook],
        'postprocessors' : [{
            'key': 'FFmpegExtractAudio',
            'preferrredcodec': 'mp3',
            'preferredquality': '320',
        }],
    }
    
    with yt_dlp.YoutubeDL(ydl_otps) as ydl:
        ydl.download([url])
        
def progress_hook(d):
    if d['status'] == 'downloading':
        print(f"Downloading: {d['_percent_str']} | Speed: {d['_speed_str']}")



def start():
    while True:
        downloadchoice = input("Do you want to download [V]ideo / [M]usic or [Q]uit :: ").upper()
        if downloadchoice == "V":
            url = input("Paste URL :: ")
            choice = input("Select Quality (1080, 720, 480, 360) :: ")
            downloadVideo(url,choice)
        elif downloadchoice == 'M':
            url = input("Paste URL :: ")
            downloadmp3(url)
            
        elif downloadchoice == 'Q':
            break
        
        else:
            print("Enter a valid value")
            return
    
if __name__ == "__main__":

    start()
