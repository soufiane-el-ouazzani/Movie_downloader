import requests
from bs4 import BeautifulSoup
import webbrowser


#the main function

def search_movie(title):
    #convert the title to a valid form
    New_converted_title = title.replace(" ","%20")
    
    url = f"https://thepiratebay10.org/search/{New_converted_title}"

    # Send GET request to Pirate search page
    response = requests.get(url)

    # Parse HTML content
    soup = BeautifulSoup(response.content, "html.parser")

    # Find movies list search results
    results = soup.find_all("div", class_="detName")[:5]
    desc_movie = soup.find_all('font', class_="detDesc")[:5]

    
    if results:
        print("Movies was founded:")
        i = 1
        for result in results:
            # Extract movie title and informations
            link = result.find("a")
            title = link["title"]
            desc_movie_selected = desc_movie[i-1]

            
            print(f"{i}_ TITLE: "+ title[:60]+ " ::::::::::> INFO :" +desc_movie_selected.text)
            i+=1
        
        # choose one movie from the list to download 
        nb_chosen_movie = int(input("choose an option for movie you liked :"))
        movie_chosen = results[nb_chosen_movie-1].find("a")["href"] 
        response_2 = requests.get(movie_chosen)
        soup_2 = BeautifulSoup(response_2.content, "html.parser")

        #find the link and redirect to utorrent
        results_2 = soup_2.find("div", class_="download")
        magnet_link = results_2.find("a")["href"]
        download_torrent(magnet_link)


    else:
        print("No movie options found.")


    
# Open torrent
def download_torrent(magnet_link):
    webbrowser.open(magnet_link)


# Ask the user for a movie title
movie_title = input("Enter a movie title: ")

# Search for the movie
search_movie(movie_title)