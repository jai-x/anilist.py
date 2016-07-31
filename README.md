# anilist.py

A simple python script that uses the [anilist.co](https://anilist.co) API to get information about both anime and manga.

This was made to both help myself become more profecient at python and to probably incorporate as the backend library data collector for the new [University of Warwick Anime and Manga Sociey website](https://animesoc.co.uk).

If this does get incorporated into the website, you can find the site code [here](https://github.com/WarwickAnimeSoc)

## Requirements

Uses python 3 and the [python-requests](http://docs.python-requests.org/en/master/) library.

## Setup

1. Ensure you have an account at anilist.co
2. Register an API client on the website under 'developer settings'
3. Input the clientid and secret as const variables at the top of the script

## Usage

From the terminal:

```shell
python anilist.py <id> <anime|manga>
```

id: the anilist id of the series you want info about

anime|manga: indicate wether the given id is for an anime or manga series

## Security

This script will store a generated a access token in plaintext in the same directory.

Since this is a limted access token that will expire in an hour, of someone has access to this token they will be able to use the API on your client's behalf.

Also, it's a good idea to remove your client id and secret key from the script after you are done.

It's never a good idea to store passwords in plaintext but this is simply a fun little script that shouldn't be taken too seriously. ('-')/

## License
GPLv3