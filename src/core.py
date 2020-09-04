import requests as res


class HHData:
    def __init__(self, search_keys):
        self.search_keys = search_keys
        self.urls = []
        self.moscow_ds = {}
        self.region_ds = {}
        self.from_str_to_list()
        self.get_list_of_url()
        self.get_data_from_urls()
        self.sort_dicts()
        self.cut_dicts()

    def from_str_to_list(self):
        if isinstance(self.search_keys, str):
            self.search_keys = self.search_keys.split(',')
        elif isinstance(self.search_keys, list):
            self.search_keys = self.search_keys
        else:
            self.search_keys = []

    def get_list_of_url(self):

        for key in self.search_keys:
            a = res.get('https://api.hh.ru/vacancies', params={'text': key, 'per_page': 100})
            page_count = a.json()['pages']

            for i in range(page_count):
                b = res.get('https://api.hh.ru/vacancies', params={'text': key, 'page': i, 'per_page': 100})
                for vac in b.json()['items']:
                    self.urls.append(vac['url'])
        self.urls = list(set(self.urls))

    def get_data_from_urls(self):
        for url in self.urls:
            r = res.get(url).json()
            skills = [a['name'] for a in r['key_skills']]
            if r['area']['name'] == 'Moscow' or r['area']['name'] == 'Москва':
                for skill in skills:
                    self.moscow_ds[skill] = self.moscow_ds.get(skill, 0) + 1
            else:
                for skill in skills:
                    self.region_ds[skill] = self.region_ds.get(skill, 0) + 1

    def sort_dicts(self):
        tup_msc = list(self.moscow_ds.items())
        tup_msc.sort(key=lambda i: i[1], reverse=True)
        self.moscow_ds = dict(tup_msc)
        tup_reg = list(self.region_ds.items())
        tup_reg.sort(key=lambda i: i[1], reverse=True)
        self.region_ds = dict(tup_reg)

    def cut_dicts(self):
        if len(self.region_ds) > 20:
            q = len(self.region_ds) - 21
            print(q)
            print(list(self.region_ds.keys()))
            for k in list(self.region_ds.keys())[:-q:-1]:
                self.region_ds.pop(k)
        if len(self.moscow_ds) > 20:
            q = len(self.moscow_ds) - 21
            for k in list(self.moscow_ds.keys())[:-q:-1]:
                self.moscow_ds.pop(k)



