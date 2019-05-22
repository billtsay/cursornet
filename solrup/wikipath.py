'''
Created on May 21, 2019

@author: bill
'''

class WikiPath(object):
    '''
    classdocs
    '''
    

    def __init__(self, start, end):
        '''
        Constructor
        '''
        self.start_article = start
        self.end_article = end        
        self.path = [self.start_article]
        self.articles = set(start)
        
        
    def __call__(self):
        
        
        
        pass
        
    def path(self):
        return self.path
    
    
    
    