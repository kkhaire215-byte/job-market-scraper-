import csv
import os
import requests

print("Connecting to the API and fetching latest jobs...")

api_url = "https://www.arbeitnow.com/api/job-board-api"

try:
  response = requests.get(api_url)
  print(f"Connection Status Code: {response.status_code}")

  if response.status_code == 200:
    api_data = response.json()
    job_list = api_data.get("data", [])

    titles = []
    companies = []
    locations = []
    links = []

    for item in job_list[:30]:
      titles.append(item.get("title"))
      companies.append(item.get("company_name"))
      locations.append(item.get("location"))
      links.append(item.get("url"))

    print(f"Successfully extracted {len(titles)} jobs!")

    # Save the file locally in the working directory to avoid Android storage restrictions
    file_name = "jobs_portfolio.csv"
    file_path = os.path.abspath(file_name)

    with open(file_path, "w", encoding="utf-8", newline="") as csv_file:
      writer = csv.writer(csv_file)
      writer.writerow(["Job Title", "Company Name", "Location", "Job URL"])

      for t, c, l, u in zip(titles, companies, locations, links):
        writer.writerow([t, c, l, u])

    print(f"File successfully saved at:\n{file_path}")
  else:
    print("Failed to retrieve data from the API source.")

except Exception as error_msg:
  print(f"An unexpected error occurred: {error_msg}")
