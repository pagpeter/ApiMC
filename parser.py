import re 

def single_parse_views(html: str) -> int:
    return int(re.search(r'>(\d+) \/', html).group(1))

def single_parse_uuid(html: str) -> str:
    return re.search(r'(.{8}-.{4}-.{4}-.{4}-.{12})', html).group(1)

def single_parse_location(html: str) -> str:
    return "None"

def single_parse_socials(html: str) -> dict:
    return {"twitter": "abc", "discord": "def"}

def single_parse_name(html: str) -> str:
    return re.search(r'<title>(.+?) |', html).group(1)

def parse_droptime(html: str) -> str:
    return html.split("Time of Availability: ")[1].split(",")[0]

def parse_searches(html: str) -> str:
    return int(html.split("Searches: ")[1].split(" /")[0])

def parse_search(html: str) -> list:
    result = []
    entries = html.split("text-left text-nowrap text-ellipsis")[2:]
    
    for entry in entries:
        doc = {}
        try:    
            doc["searches"] = entry.split('text-right text-nowrap text-ellipsis">')[1].split("</td>")[0]
            doc["name"] = entry.split('"no">')[1].split("<")[0]
            doc["droptime"] = entry.split('time datetime="')[1].split('"')[0]
            result.append(doc)
        except:
            print(entry)

    return {"count": len(entries), "names": result}

def parse_single(html: str) -> dict:
    result = {}
    if ">UUID<" in html:
        # Name is already taken
        result["status"] = "taken"
        result["views"] = single_parse_views(html)
        result["uuid"] = single_parse_uuid(html)
        result["name"] = single_parse_name(html) 
        # result["location"] = single_parse_location(html)
        # result["socials"] = single_parse_socials(html)

    elif "availability-time" in html:
        # Name is dropping
        result["droptime"] = parse_droptime(html)
        result["status"] = "dropping"
        result["searches"] = parse_searches(html)
    else:
        # Name is free, invalid or other
        result["status"] = "not taken"
        result["searches"] = parse_searches(html)
    return result
