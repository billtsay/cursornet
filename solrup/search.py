'''
Created on May 21, 2019

@author: bill
'''

import wikipedia
import copy
import concurrent.futures

def page_titles(pages):
    results = []
    for p in pages:
        results.append(p.title)
        
    return results

def page_gen(links):
    for l in links:
        yield wikipedia.page(l)
        
def search_links(links, e):
    results = []
    for l in links:
        done, result = do_search(links, l, e)
        if done:
            return True, result
        
        results = results + result
        
    return False, results

def do_search(links, l, e):
    results = []   
    for p in page_gen(l[-1].links):
        if p == e:
            z = copy.copy(l)
            z.append(e) 
            return True, z
            
        if p not in links:
            for x in links:
                y = copy.copy(x)
                y.append(p)
                results.append(y)
                
            print("-----")
            print(len(results))
                      
    return False, results

end_page = wikipedia.page("Tax Credit")

while True:
    done, results = search_links([[wikipedia.page("Web Bot")]], end_page) 
    if done: 
        print(page_titles(results))
        break
    else:
        search_links(results, end_page)
        
        
#search_links([[low_case("Web Bot")]], low_case("Barack Obama"))    
#search_links([[low_case("Web Bot")]], low_case("Tax Credit"))    
   
#search_links([["Web Bot"]], "Tax Credit")    


#tax = wikipedia.page("Tax Holiday")

#for n in tax.links:
#    print(wikipedia.page(n).pageid)


