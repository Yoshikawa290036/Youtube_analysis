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

    def output_url_list(self):
        output = []
        if self.stream_num == 0:
            output.append("No data")
        for i in range(self.stream_num):
            output.append(f"{self.stream_url[i]}\t{self.stream_date[i]}\t{self.stream_title[i]}\t{self.stream_id[i]}\n")
        with open(self.url_list_file, 'w', encoding='utf-8') as f:
            f.writelines(output)

    def save_data(self):
        save_file = os.path.join(self.output_dir, "Liver_data.pickle")
        with open(save_file, 'wb') as f:
            pickle.dump(self, f)


class Conbined_Liver_data(object):
    def __init__(self, start_date, end_date, Liver_data_list):
        self.youtube_url = "https://www.youtube.com"
        self.start_date = int(start_date)
        self.end_date = int(end_date)
        self.ranking_file_name = os.path.join(f"{self.start_date}-{self.end_date}", "RANKING.tsv")
        self.video_directory = os.path.join(f"{self.start_date}-{self.end_date}", "videos")
        self.thumbnail_directory = os.path.join(f"{self.start_date}-{self.end_date}", "thumbnails")
        os.makedirs(self.video_directory, exist_ok=True)
        os.makedirs(self.thumbnail_directory, exist_ok=True)
        self.stream_num = 0
        self.pos = 0
        self.channel_streams_urls = []
        self.output_dirs = []
        self.c_names = []
        self.gens = []
        self.urls = []
        self.ids = []
        self.titles = []
        self.date = []
        self.chat_data_files = []
        self.chat_speed_files = []
        self.chat_speed_rank_files = []

        for liver in Liver_data_list:
            self.channel_streams_urls.extend([liver.channel_streams_url]*liver.stream_num)
            self.output_dirs.extend([liver.output_dir]*liver.stream_num)
            self.c_names.extend([liver.c_name]*liver.stream_num)
            self.gens.extend([liver.generation]*liver.stream_num)
            self.urls.extend(liver.stream_url)
            self.ids.extend(liver.stream_id)
            self.titles.extend(liver.stream_title)
            self.date.extend(liver.stream_date)
            self.chat_data_files.extend(liver.chat_data_file)
            self.chat_speed_files.extend(liver.chat_speed_file)
            self.chat_speed_rank_files.extend(liver.chat_speed_rank_file)
            self.stream_num += liver.stream_num

    def print_data(self):
        for i in range(self.stream_num):
            print(self.c_names[i],
                  self.gens[i],
                  self.urls[i],
                  self.ids[i],
                  self.titles[i],
                  self.date[i],
                  self.chat_data_files[i],
                  self.chat_speed_files[i],
                  self.chat_speed_rank_files[i]
                  )
