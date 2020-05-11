from bs4 import BeautifulSoup
import requests, os, re, boto3
from datetime import datetime
from collections import Counter

def get_amount_of_tags():
    url = input(f"Hello, {os.environ['USER']}, "
                f"please input the URL for which you would like to know the total amount of tags "
                f"as well as count of each of them: ")

    while not re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+] |[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', url):
        url = input(f"  You've inputed not URL, try again: ")

    try:
        request = requests.get(url, headers={'Accept-Language': 'En-us'})
        soup = BeautifulSoup(request.text, 'lxml')
        tags = [tag.name for tag in soup.find_all()]

        print(f'{url}:\ngeneral tags: {len(tags)}')
        print("\n".join(f"{str(item)}: {str(value)}" for item,value in Counter(tags).most_common()))

        answer_log = input('Would you like to save information in log file(logs.txt)?(yes(Y)/no(N)): ')
        while answer_log not in ['yes', 'no', 'Y', 'N']:
            answer_log = input('    wrong input, try again: ')

        if answer_log == 'Y' or answer_log == 'yes':
            with open('logs.txt', 'a') as log_file:
                log_file.write(f'{datetime.today().strftime("%Y/%m/%d %H:%M")} {url} {len(tags)}{dict(Counter(tags).most_common())}\n')

        answer_s3 = input('Would you like to copy log into a bucket?(yes(Y)/no(N)): ')
        while answer_s3 not in ['yes', 'no', 'Y', 'N']:
            answer_s3 = input('    wrong input, try again: ')

        if answer_s3 == 'yes' or answer_s3 == 'Y':
            bucket_name = input('What is the name of the bucket? ')
            s3 = boto3.client('s3')
            try:
                s3.upload_file('log.txt', bucket_name, 'logs.txt')
            except Exception as err:
                print(f'OOPS, we have an error:\n  "{err}"')

    except Exception as err:
        print(f'OOPS, we have an error:\n  "{err}"')



if __name__ == '__main__':
    pass
