from bs4 import BeautifulSoup
import os
def generate(numsArr):
    html = []
    for i in range(len(numsArr)):
        height = numsArr[i] * 2
        html.append(f'<div class="bar" style="height: {height}px;"> </div>')
    print(html)
    insertHtml( "\n".join(html))

def insertHtml(html):
    print(html)
    try:
        with open("./visual.html", "r", encoding="utf-8") as f:
                htmlDoc = f.read()
        soup = BeautifulSoup(htmlDoc, 'lxml')
        targetDiv = soup.find(id="sortcontainer")
        if targetDiv:
            targetDiv.clear()
            
            
            new_elements_to_insert = BeautifulSoup(html, 'lxml').contents
            print(new_elements_to_insert)
            
            for element in new_elements_to_insert:
                targetDiv.append(element)
            
            with open("./visual.html", "w", encoding="utf-8") as f:
                f.write(soup.prettify())
        else:
            print("Error: Target div with ID 'sortcontainer' not found.") # Füge eine Fehlermeldung hinzu
    except FileNotFoundError:
        print("Error: The file 'sortvisual/visual.html' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    
