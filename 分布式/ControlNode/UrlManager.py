import pickle
import hashlib
class UrlManager(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()
    def has_new_url(self):
        return self.new_url_size()!=0
    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url
    def add_new_url(self,url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)
    def add_new_urls(self,urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)
    def new_url_size(self):
        return len(self.new_urls)
    def old_url_size(self):
        return len(self.old_urls)
    def save_progress(self,path,data):
        with open(path,"wb") as f:
            pickle.dump(data,f)
    def load_progress(self,path):
        print("[+]从文件加载进度：%s"%path)
        try:
            with open(path,"rb")as f:
                tmp = pickle.load(f)
                return tmp
        except:
            print("[!]无进度文件，创建：%s"%path)
        return set()
