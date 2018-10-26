import pandas as pd
import requests
import json

class PushShift:

    def __init__(self):
        self.after = ''
        self.before = ''
        self.sub = ''
        self.query = ''

    def getPushshiftData(self,*args):
        url = 'https://api.pushshift.io/reddit/search/submission'
        #case: arg[0] = unix timestamp and arg[1] is subreddit
        if len(args) == 2 and self.representsInt(args[0]) and isinstance(args[1],str):
            after, sub = args
            endpoints = {"size":"1000", "after":str(after), "subreddit":str(sub)}
            r = requests.get(url, params=endpoints)
            data = json.loads(r.text)
            return data['data']
        #case: arg[1] = unix timestamp and arg[1] is unix timestamp and arg[2] is subreddit
        elif len(args) == 3 and self.representsInt(args[0]) and self.representsInt(args[1]) and isinstance(args[2],str):
            after, before, sub = args
            endpoints = {"size":"1000", "after":str(after), "before":str(before), "subreddit":str(sub)}
            r = requests.get(url, params=endpoints)
            data = json.loads(r.text)
            return data['data']
        else:
            raise TypeError('Parameter 1 (and parameter 2 in case of 3 parameters) should be unix timestamp in string format, while the final parameter should be the subreddit in string format')
        
    def representsInt(self,s):
        try:
            int(s)
            return True
        except ValueError:
            return False

    def setAfter(self,after):
        self.after = after

    def setBefore(self,before):
        self.before = before

    def setSub(self,sub):
        self.sub = sub

    def setQuery(self,query):
        self.query = query

    def retrievePushshiftData(self):
        post_ids = []
        if not self.after == '' and not self.sub == '' and not self.query == '':
            if not self.before == '':
                data = self.getPushshiftData(self.after,self.before,self.sub)
                while len(data) > 0:
                    for submission in data:
                        if self.query in submission['full_link']:
                            print(submission['full_link'])
                            post_ids.append(submission['id'])
                    data = self.getPushshiftData(data[-1]['created_utc'],self.before,self.sub)
            else:
                data = self.getPushshiftData(self.after,self.sub)
                while len(data) > 0:
                    for submission in data:
                        if self.query in submission['full_link']:
                            print(submission['full_link'])
                            post_ids.append(submission['id'])
                    data = self.getPushshiftData(data[-1]['created_utc'],self.sub)
        else:
            raise ValueError('self.after, self.sub, and self.query should not equal an empty string')
        return post_ids

    def createOutputJson(self,post_ids):
        obj = {}
        if not post_ids == []:
            if not self.sub == '':
                obj['sub'] = self.sub
                obj['id'] = post_ids
                if not self.before == '':
                    with open("submissions_subreddit_%s_after_%s_before_%s.json"%(self.sub,self.after,self.before),"w") as jsonFile:
                        json.dump(obj, jsonFile)
                else:
                    with open("submissions_subreddit_%s_after_%s.json"%(self.sub,self.after),"w") as jsonFile:
                        json.dump(obj, jsonFile)
            else:
                raise ValueError("self.sub should not be an empty string")
        else:
            raise ValueError('post_ids should not be an empty list')
