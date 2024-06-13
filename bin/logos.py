#!/usr/bin/python3
# -*- coding: utf-8 -*-

###### Import ########

import argparse
import asyncio
import io
import os
from urllib.parse import urlparse

import favicon
import httpx

###### Variable ######

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
headers = {'User-Agent': user_agent}
folder = "../static/assets/images/logos/"
w, h = 128, 128

###### Function ######

def get_args():
    """
    Parse command line arguments for downloading favicon from a website.

    Returns:
        argparse.Namespace: An object containing the parsed command line arguments.
    """
    parser = argparse.ArgumentParser(description='Download favicon from a website')
    parser.add_argument('-d', '--download', help='URL for direct download', required=False)
    parser.add_argument('-u', '--url', help='URL of the website', required=False)
    parser.add_argument('-s', '--s2p', help='SVG to PNG', required=False)
    parser.add_argument('-o', '--output', help='Output file', required=False)
    return parser.parse_args()

def get_filename(folder, format, args, url=""):
    """
    Get the filename for a given URL and extension.

    Args:
        url (str): The URL of the file.
        ext (str): The desired file extension.
        folder (str): The folder to save the file in.
        args (Namespace): The command-line arguments.

    Returns:
        str: The generated filename.

    """
    if args.output:
        if has_extension(args.output):
            return os.path.join(folder,args.output)
        else:
            output = args.output
    else:
        output = urlparse(args.url).netloc.split('.')[-2]
    return os.path.join(folder,output + "." + format)

def get_format(url):
    """
    Get the file format from a URL.

    Args:
        url (str): The URL of the file.

    Returns:
        str: The file format.

    """
    _, file_extension = os.path.splitext(url)
    return file_extension[1:]

def has_extension(file_name):
    _, file_extension = os.path.splitext(file_name)
    return file_extension != ""

def menu(logos):
    """
    Displays a menu of logos and prompts the user to choose one.

    Args:
        logos (list): A list of icon objects.

    Returns:
        Icon: The selected icon object.

    """
    print("Choose an icon:\n")
    for i, logo in enumerate(logos):
        print(f"{i+1}. {logo.url}")
    print("\n0. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 0: exit()
    return logos[choice-1]

def save_icon(data_picture, args, folder, format, url=""):
    """
    Save the icon image from the response to the specified filename.

    Args:
        data_picture (bytes): The response object containing the icon image.
        filename (str): The path and filename to save the icon image to.

    Returns:
        None
    """
    filename = get_filename(folder, format, args, url)
    with open(filename, 'wb') as file:
        file.write(data_picture)

def svg2png(data_picture, width, height):
    """
    Convert an SVG image to a PNG image.

    Args:
        args (Namespace): The command-line arguments.
        data_picture (bytes): The SVG image data.
        format (str): The file format of the image.
        width (int): The desired width of the PNG image.
        height (int): The desired height of the PNG image.

    Returns:
        bytes: The PNG image data.
    """
    import cairosvg
    png_output = io.BytesIO()
    if type(data_picture) == "str":
        data_picture = data_picture.encode('utf-8')
    cairosvg.svg2png(bytestring=data_picture, output_width=width, output_height=height, write_to=png_output)
    png_data = png_output.getvalue()
    png_output.close()
    return png_data

async def main():
    format = 'png'
    args = get_args()
    client = httpx.AsyncClient(http2=True)
    
    if args.s2p:
        filename = os.path.join(folder,args.s2p)
        with open(filename, 'r') as f:
            svg_data = f.read()
        data_picture = svg2png(svg_data, w, h)
        save_icon(data_picture, args, folder, format)
        exit(0)
    elif args.url:
        logos = favicon.get(args.url, headers=headers)
        choice = menu(logos)
        url = choice.url
        format = choice.format
    elif args.download:
        url = args.download 
        format = get_format(url)
    
    response = await client.get(url, headers=headers)
    data_picture = response.content
    
    if url.endswith('.svg'):
        format = 'svg'
        # save_icon(data_picture, args, folder, format, url)
        # data_picture = svg2png(data_picture, w, h)
        # format = 'png'
        
    save_icon(data_picture, args, folder, format, url)

###### Program #######

if __name__ == '__main__':
    asyncio.run(main())

