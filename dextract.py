import requests
from bs4 import BeautifulSoup
import csv
urls_and_parties = [
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-369.htm', 'BJP'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-742.htm', 'INC'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-1680.htm', 'SP'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-140.htm', 'AITC'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-582.htm', 'DMK'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-1745.htm', 'TDP'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-805.htm', 'JD(U)'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-3369.htm', 'SHSUBT'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-3620.htm', 'NCPSP'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-3529.htm', 'SHS'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-3165.htm', 'LJPRV'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-1888.htm', 'YSRCP'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-1420.htm', 'RJD'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-547.htm', 'CPI(M)'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-772.htm', 'IUML'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-1.htm', 'AAAP'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-852.htm', 'JMM'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-860.htm', 'JNP'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-545.htm', 'CPI(ML)(L)'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-804.htm', 'JD(S)'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-1847.htm', 'VCK'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-544.htm', 'CPI'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-1458.htm', 'RLD'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-834.htm', 'JKN'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-1998.htm', 'UPPL'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-83.htm', 'AGP'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-664.htm', 'HAMS'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-911.htm', 'KEC'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-1534.htm', 'RSP'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-1142.htm', 'NCP'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-3388.htm', 'VOTPP'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-2757.htm', 'ZPM'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-1584.htm', 'SAD'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-2484.htm', 'RLTP'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-3482.htm', 'BHRTADVSIP'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-1658.htm', 'SKM'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-1046.htm', 'MDMK'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-2989.htm', 'ASPKR'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-2070.htm', 'ADAL'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-160.htm', 'AJSUP'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-118.htm', 'AIMIM'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-743.htm', 'IND')
]

def fetch_and_parse(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup
    else:
        print(f"Failed to retrieve the webpage at {url}. Status code: {response.status_code}")
        return None

def extract_table_data(soup, party):
    data = []
    if soup is not None:
        tables = soup.find_all('table')
        for table in tables:
            rows = table.find_all('tr')
            for row in rows:
                header_cells = row.find_all('th')
                data_cells = row.find_all('td')
                if header_cells:
                    headers = [cell.get_text(strip=True) for cell in header_cells]
                    headers.append("Party")
                    data.append(headers)
                else:
                    row_data = [cell.get_text(strip=True) for cell in data_cells]
                    row_data.append(party)
                    data.append(row_data)
    else:
        print("No data found for the given soup.")
    return data


csv_filename = "all_table_data.csv"
headers_written = False

with open(csv_filename, mode='w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)

    for url, party in urls_and_parties:
        soup = fetch_and_parse(url)
        table_data = extract_table_data(soup, party)

        for row in table_data:
            if not headers_written:
                csv_writer.writerow(row)
                headers_written = True
            else:
                if row[0] != table_data[0][0]:  # Avoid writing the header again
                    csv_writer.writerow(row)

print(f"Data has been written to {csv_filename}")