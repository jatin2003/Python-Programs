# Python Script to read News from BBC

# importing requests package 
import requests      
  
def News(): 
      
    # BBC news api 
    main_url = " https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=4dbc17e007ab436fb66416009dfb59a8"
  
    # fetching data in json format 
    open_bbc_page = requests.get(main_url).json() 
  
    # getting all articles in a string article 
    article = open_bbc_page["articles"] 
  
    # empty list which will  
    # contain all trending news 
    results = [] 
      
    for ar in article: 
        results.append(ar["title"]) 
          
    for i in range(len(results)): 
          
        # printing all trending news 
        print(i + 1, results[i])                  
  
# Driver Code 
if __name__ == '__main__': 
      
    # function call 
    News() 
