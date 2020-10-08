# songbank
_no more downloading from sketchy websites_

![](https://giphy.com/gifs/film-vintage-color-3ohjUVaRYvIp5i9F7O)
![](http://gph.is/2B2wILM)
![](https://media.giphy.com/media/3ohjUVaRYvIp5i9F7O/giphy.gif)
----------

## Usage
```bash
$ git clone https://github.com/reidwil/songbank.git
$ pip install -r requirements.txt
# For all of my urls within ./backlog/
$ python3 app.py
# For all urls you want to feed it
$ python3 app.py yoururls.txt path/to/download/to
```

## Up next

- [x] Allow users to easily download my directory of urls
- [x] Download/clone capability
- [ ] Add cookie.txt to get rid of out country and age restricted videos
- [ ] And other things

## Bugs

- youtube-dl seems to quit the dl loop - [related](https://github.com/ytdl-org/youtube-dl/issues/22641)
  - this might just be a timeout because of too many requests... might be worth putting  `sys.sleep(n)` in the download loop