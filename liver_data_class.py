import os
import pickle

class Liver_data(object):
    def __init__(self, c_name, generation, start_date, end_date):
        self.youtube_url = "https://www.youtube.com"
        self.c_name = c_name
        self.generation = generation
        self.start_date = int(start_date)
        self.end_date = int(end_date)
        self.channel_streams_url = os.path.join(self.youtube_url, self.c_name, 'streams')
        self.output_dir = os.path.join(f"{self.start_date}-{self.end_date}", f"{generation}_{c_name}")
        os.makedirs(self.output_dir, exist_ok=True)
        self.url_list_file = os.path.join(self.output_dir, "URL_list.tsv")
        self.log = os.path.join(self.output_dir, ".log")
        self.pos = 0
        self.stream_num = 0
        self.stream_url = []
        self.stream_id = []
        self.stream_title = []
        self.stream_date = []

        self.chat_data_file = []
        self.chat_speed_file = []
        self.chat_speed_rank_file = []
        self.chat_data = []

    def output_url_list(self):
        output = []
        for i in range(self.stream_num):
            output.append(f"{self.stream_url[i]}\t{self.stream_date[i]}\t{self.stream_title[i]}\t{self.stream_id[i]}\n")
        with open(self.url_list_file, 'w', encoding='utf-8') as f:
            f.writelines(output)
            
    def save_data(self):
        save_file = os.path.join(self.output_dir, "Liver_data.pickle")
        with open(save_file, 'wb') as f:
            pickle.dump(self, f)
