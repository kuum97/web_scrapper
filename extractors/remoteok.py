from bs4 import BeautifulSoup
import requests

def extract_remoteok_jobs(keyword):
  url = f"https://remoteok.com/remote-{keyword}-jobs"
  request = requests.get(url, headers={"User-Agent": "Kimchi"})
  if request.status_code == 200:
    results = []
    soup = BeautifulSoup(request.text, "html.parser")
    jobs = soup.find_all("tr", class_="job")
    for job in jobs:
      company = job.find("h3", itemprop="name")
      position = job.find("h2", itemprop="title")
      location = job.find("div", class_="location")
      anchor = job.find("a", class_="preventLink")
      link = anchor["href"]
      if company:
        company = company.string.strip()
      if position:
        position = position.string.strip()
      if location:
        location = location.string.strip()
      if company and position and location:
        job_data = {
          'link': f"https://remoteok.com/remote-jobs{link}",
          'company': company.replace(",", " "),
          'position': position.replace(",", " "),
          'location': location.replace(",", " "),
        }
        results.append(job_data)
    return results
  else:
    print("Can't request website")