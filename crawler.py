from bs4 import BeautifulSoup
import json
import os

WEBSITE_DIR = "website"
INCLUDE_EXTENSIONS = [".html", ".htm"]
QUESTION_PREFIXES = ["what is", "what's", "where is", "where's", "how do I"]


def main():
    extracted_data = []
    searchfiles = []

    # get all the files which needs to be indexed by the bot
    for (dirpath, _, filenames) in os.walk(WEBSITE_DIR):
        files = [os.path.join(dirpath, file) for file in filenames
                 if os.path.splitext(file)[1] in INCLUDE_EXTENSIONS]
        searchfiles.extend(files)

    print(f"found {len(searchfiles)} files to index")

    # extract keywords from the meta tag
    for file in searchfiles:
        print(f"extracting information from {file}")
        with open(file, 'r') as fp:
            soup = BeautifulSoup(fp.read(), "lxml")
            meta_keywords = soup.select_one("meta[name='keywords']")
            if not meta_keywords:
                print("keywords not set - ignoring")
            else:
                data = {
                    "file": file,
                    "keywords": meta_keywords['content']
                }
                extracted_data.append(data)

    # create intents, extend the intents.base.json
    intents_json = None
    try:
        with open("intents.base.json", "r") as fp:
            intents_json = json.load(fp)
    except json.JSONDecodeError:
        print("failed to load intents.base.json")
        return

    print("extending intents.base.json")

    for page in extracted_data:
        location = page["file"]
        keywords = [prefix + " " + keyword.lower().strip()
                    for keyword in page["keywords"].split(",") for prefix in QUESTION_PREFIXES]

        intent = {
            "tag": f"page-{location}",
            "patterns": keywords,
            "responses": [f"Here's your page\n{location}", f"There you go\n{location}", f"This is what you are looking for - {location}", f"Go here {location}"]
        }

        intents_json["intents"].append(intent)

    print("creating intents.json")
    with open("intents.json", "w+") as fp:
        json.dump(intents_json, fp)


if __name__ == '__main__':
    main()
