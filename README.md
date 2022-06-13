# ApiMC - a simple, selfhosted NameMC api

Do you ever wanted to scrape some data from NameMC? Well, now you can.
This project features a built-in cloudflare bypass, built-in caching and has 0 dependencies. Just clone the repo and run the main.py file.

! Cloudflare will still block you, if you use this on a flagged IP (most VPSs) !

```bash
$ git clone https://github.com/wwhtrbbtt/ApiMC
$ cd ApiMC 
$ python3 main.py 
```

## TODO
 - [] Extract socials, if present 
 - [] Extract location, if present
 - [] Make cloudflare not block you on flagged IPs (pretty much not possible, if we don't use a browser)
