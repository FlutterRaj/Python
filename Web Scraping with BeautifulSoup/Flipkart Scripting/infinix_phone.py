import requests
from bs4 import BeautifulSoup
from csv import writer

url = "https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&otracker=categorytree&p%5B%5D=facets.brand%255B%255D%3DInfinix&otracker=nmenu_sub_Electronics_0_Infinix"
current = 0
next_page = 2

while True:
    response = requests.get(url).text
    soup = BeautifulSoup(response, "html.parser")

    divs = soup.select("._1-2Iqu")
    if not divs:
        break

    with open("infinix_phones.csv", "a", newline="") as file:
        csv_writer = writer(file)
        if not current:
            csv_writer.writerow(["Mobile Name", "Price"])

        for div in divs:
            mobile_name = div.select("._3wU53n")[0].get_text()
            mobile_price = div.select("._1vC4OE")[0].get_text()[1:]
            # print(f"{mobile_name} --> {mobile_price}")
            csv_writer.writerow([mobile_name, mobile_price])

        a_tags = soup.select("._2Xp0TH")

        for tag in a_tags:
            if not current:
                pass
            else:
                url = f"https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&otracker=categorytree&p%5B%5D=facets.brand%255B%255D%3DInfinix&otracker=nmenu_sub_Electronics_0_Infinix&page={next_page}"
                # print(url)
                print(f"😈 Scarping Done {next_page}😈")
                next_page += 1
                break
            current += 1
