ls 20230617-20230623/*/*_speed_RANK.tsv > 20230617-20230623/RANK_list.tsv
mkdir -p 20230617-20230623/videos
python3  analysis_RANK.py  20230617-20230623/RANK_list.tsv
