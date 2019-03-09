import time

from googlesearch import search


def analyze(input):
    first_name = input['first_name']
    last_name = input['last_name']
    org = input['organization']
    location = input['location']
    tld_in = str(input['tld'])
    num_query = int(input['num_query'])
    stop_query = int(input['stop_query'])
    pause_time = int(input['pause_time'])
    extra_filter = str(input['extra_filter'])
    if input['to_file']:
        to_file = str(input['to_file']) + '.txt'

    query = first_name + ' ' + last_name + ' ' + org + ' ' + location
    print('Given Query : ', query)
    urls = []
    social_media = []
    open_source = []
    portfolio = []
    time_start = time.time()
    for j in search(query, tld=tld_in, num=num_query, stop=stop_query, pause=pause_time):
        urls.append(j)
    time_end = time.time()
    print('Time elapsed: ', time_end - time_start, ' seconds')
    print(' ')

    print(' ')
    if (extra_filter != 'False') & (extra_filter != 'false'):

        print('Applying extra filters..... ')
        

        for url in urls:
            if ('git' in url) | ('code' in url):
                open_source.append(url)

            if ('linkd' in url) | ('linkedin' in url) | ('stack' in url):
                portfolio.append(url)

            if ('fb' in url) | ('facebook' in url) | ('twitter' in url) | ('instagram' in url) | ('quora' in url) | (
                    'kaggle' in url) | ('wiki' in url):
                social_media.append(url)

        print(' ')
        print('Possible Open Source work: \n')
        for url in open_source:
            print(url)

        print(' ')
        print('Social Media: \n')
        for url in social_media:
            print(url)

        print(' ')
        print('Portfolio: \n')
        for url in portfolio:
            print(url)

        print(' ')
        print('Other: \n')
        for url in urls:
            if (url not in open_source) & (url not in social_media) & (url not in portfolio):
                print(url)
    else:

        print('Queried URLS for given person details:')
        for url in urls:
            print(url)
    print(' ')
    if input['to_file']:

        print('Writing to text file..... \n')
        f = open(to_file, "w+")

        f.write("OPEN SOURCE RELATED:" + "\n")
        f.write(" " + "\n")
        for url in open_source:
            f.write(url + "\n")
        f.write(" " + "\n")

        f.write("PORTFOLIO:" + "\n")
        f.write(" " + "\n")
        for url in portfolio:
            f.write(url + "\n")
        f.write(" " + "\n")

        f.write("SOCIAL MEDIA:" + "\n")
        f.write(" " + "\n")
        for url in social_media:
            f.write(url + "\n")
        f.write(" " + "\n")

        f.write("OTHER:" + "\n")
        f.write(" " + "\n")
        for url in urls:
            if (url not in open_source) & (url not in social_media) & (url not in portfolio):
                f.write(url + "\n")

        f.close()

        print('Written to text file successfully ! ')
        return 1;
