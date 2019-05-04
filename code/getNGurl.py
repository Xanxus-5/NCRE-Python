def main():
    inputfile = 'f:\\py\\ng.html'
    outputfile = 'f:\\py\\ngurls.txt'
    htmlLines = getHTMLlines(inputfile)
    imageUrls = extractImagesUrls(htmlLines)
    show(imageUrls)
    save(outputfile, imageUrls)

def getHTMLlines(path):
    f = open(path, "r", encoding = 'utf-8')
    ls = f.readlines
    f.close()
    return ls

def extractImagesUrls(list):
    urls = []
    for line in list:
        if 'img' in line:
            url = line.split('src=')[-1].split('"')[1]
            if "http" in url:
                urls.append(url)
    return urls

def show(urls):
    count = 0 
    for url in urls:
        print('第{:2}个URL:{}'.format(count, url))
        count += 1

def save(filepath, urls):
    f = open(filepath, "w")
    for url in urls:
        f.write(url + "\n")
    f.close()

main()
