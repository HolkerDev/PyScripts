from requests.exceptions import ConnectionError
import requests

'''Script automatically downloads all images using links in txt file'''

PATH_IMAGES = 'images.txt'
# start downloading images from this index
START_FROM = 11072

urls = list()

with open(PATH_IMAGES, mode='r') as file:
    for line in file:
        urls.append(line[:len(line) - 1])

# for controlling amount of images
count = 0

for url_image in urls:
    if count > START_FROM:
        try:
            file = requests.get(url_image, timeout=3).content
            # specify path
            f = open(str(count) + '.jpg', 'wb')
            f.write(file)
            f.close()
            print("saved: " + str(count))
        except ConnectionError as e:
            print("connection error: " + str(count))
        except requests.exceptions.Timeout:
            print("timeout error: " + str(count))
        except requests.exceptions.InvalidURL:
            print("url error: " + str(count))
        except requests.exceptions.TooManyRedirects:
            print("redirection error: " + str(count))
        count += 1
    else:
        print("skip: " + str(count))
        count += 1
