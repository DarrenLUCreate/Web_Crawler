import scraping_pr
import time
import asyncio
import csv


start_time = time.time()
tasks = asyncio.run(scraping_pr.scraper('sex'))
label = ['url', 'title', 'author', 'content']
results = []
for task in tasks:
    result = {'url': task.result()['url'], 'title': task.result()['title'], 'author': task.result()['author'], 'content': task.result()['content']}
    results.append(result)

with open('Ptt-Sex_info.csv', 'w', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=label)
    writer.writeheader()
    for elem in results:
        writer.writerow(elem)
            
print("花費:" + str(time.time() - start_time) + "秒")
