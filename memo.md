・文字列の変数
41行目 time_str = f"{start_time}-{end_time}"
43行目 loc_str = f"@{location}" if location else "@(場所なし)"
45行目 return f"{time_str} {title} {loc_str}"py schedule.py 2026-10-02
52行目 target_date = datetime.now(JST).strftime("%Y-%m-%d")

・数の変数 なし

・リストの変数 なし

■関数1 
名前:load_schedules(filepath="schedule.json") 
受け取るもの:schedule.json を読み込む  
返すもの:return json.load(f)  
役割: JSONファイルの中身を読み込み、Pythonでそのまま扱えるデータに変換している

■関数2 
名前:filter_schedules_by_date(schedules, target_date): 
受け取るもの:指定した日付の予定を抽出して時刻順にソートする  
返すもの:return filtered  
役割: 開始時刻の昇順にソート

■関数3 
名前:format_schedule(item) 
受け取るもの:1件の予定を指定の文字列形式に変換する  
返すもの: return f"{time_str} {title} {loc_str}"py schedule.py 2026-10-02  
役割: f 文字列を使って、時刻・タイトル・場所の変数を一つの文字列にまとめて出力する