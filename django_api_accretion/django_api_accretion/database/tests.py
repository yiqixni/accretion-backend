# tests.py 
# testsDell returns the json data for 22 dell st property for demo 

from bs4 import BeautifulSoup 
import datetime 

def readHTML (file_path): 
    with open(file_path) as f: 
        html_file = f.read() 
        
    return html_file 

def testsDell ():
    file_path = "database/dell-street-data.html"  
    html_file = readHTML(file_path=file_path) 
    json_data = convertHTML2json(html_file=html_file) 

    return json_data 

def convertHTML2json (html_file) :         
    soup = BeautifulSoup(html_file, 'html.parser') 
    data = [] 
    
    # Find the table element with id "DocList1_GridView_Document"
    table = soup.find('table', {'id': 'DocList1_GridView_Document'})

    # Check if the table is found
    if table:
        # Iterate over each row in the table
        for row in table.find_all('tr'):
            # Extract data from each cell in the row
            cells = row.find_all('td')
            if cells:
                street_name = cells[0].text.strip()
                rec_date = cells[1].text.strip()
                book_page = cells[2].text.strip()
                type_desc = cells[3].text.strip()
                street_number = cells[4].text.strip()
                town = cells[5].text.strip()
                
                # Convert the date string to a datetime object
                date_obj = datetime.datetime.strptime(rec_date, "%m/%d/%Y")

                # Convert the datetime object to the ISO 8601 format
                iso_date = date_obj.isoformat()

                # Replace the date string in the dictionary with the ISO 8601 date
                rec_date = iso_date
                
                row_data = {
                    "street_name": street_name,
                    "date": rec_date,                    
                    "book_page": book_page,
                    "type": type_desc,
                    "street_number": street_number,
                    "town": town
                }
                
                data.append(row_data) 
                        
    else:
        print("Table with id 'DocList1_GridView_Document' not found.")        
    
    # data_json = json.dumps(data, indent=4, sort_keys=True)        
    # return data_json 
    return data

