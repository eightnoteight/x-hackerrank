from os import getcwd
with open('src/.cached_api', "r") as f:
	cached_key = f.readline()
with open('src/.cached_lang', "r") as f:
	cached_lang = int(f.readline())