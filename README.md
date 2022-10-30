# ApiMC - a simple, selfhosted NameMC api

Do you ever wanted to scrape some data from NameMC? Well, now you can.
This project features a built-in cloudflare bypass, built-in caching and has 0 dependencies. It uses bottle as a server, which is contained in a single file (no need to install anything)
Just clone the repo and run the main.py file.

! Cloudflare will still block you, if you use this on a flagged IP (most VPSs) !

```bash
$ git clone https://github.com/wwhtrbbtt/ApiMC
$ cd ApiMC
$ python3 main.py
```

## Docs

- ### GET /api/name/\<name>

Returns information about a certain name.
This can be:

- When the name drops (if it drops)
- Amount of searches (if the name isn't taken)
- Amount of views (if the name is taken)
- The UUID
- Status (dropping, taken, not taken)

- Location (not implemented)
- Socials (not implemented)
- Skins (not implemented)
- Capes (not implemented)

- ### GET /api/searches/\<minSearches>

Returns all names that will drop soon with a certain amount of searches

- ### GET /api/3chars

Returns all names that will drop soon with 3 characters

## TODO

- [ ] Fix docs.html
- [ ] Extract more information
- [ ] Make cloudflare not block you on flagged IPs (pretty much not possible, if we don't use a browser)
