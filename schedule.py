import json
import os
import sys
from datetime import datetime, timezone, timedelta

# 日本時間 (JST = UTC+9)
JST = timezone(timedelta(hours=9))

def load_schedules(filepath="schedule.json"):
    """schedule.json を読み込む"""
    if not os.path.exists(filepath):
        print(f"エラー: '{filepath}' が見つからないため、予定表を表示できません。", file=sys.stderr)
        sys.exit(1)
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        print(f"エラー: '{filepath}' のJSON形式が正しくありません ({e})", file=sys.stderr)
        sys.exit(1)

def filter_schedules_by_date(schedules, target_date):
    """指定した日付の予定を抽出して時刻順にソートする"""
    filtered = []
    for item in schedules:
        start = item.get("start", "")
        # start の先頭10文字 (YYYY-MM-DD) が一致するか判定
        if start.startswith(target_date):
            filtered.append(item)
    
    # 開始時刻の昇順にソート
    filtered.sort(key=lambda x: x.get("start", ""))
    return filtered

def format_schedule(item):
    """1件の予定を指定の文字列形式に変換する"""
    start_time = item.get("start", "")[11:16]
    end_time = item.get("end", "")[11:16]
    title = item.get("title", "")
    location = item.get("location")
    
    time_str = f"{start_time}-{end_time}"
    # location が空、または存在しない場合は「@(場所なし)」とする
    loc_str = f"@{location}" if location else "@(場所なし)"
    
    return f"{time_str} {title} {loc_str}"

def main():
    # コマンドライン引数から日付を取得。なければ今日の日本時間を使用
    if len(sys.argv) > 1:
        target_date = sys.argv[1]
    else:
        target_date = datetime.now(JST).strftime("%Y-%m-%d")
    
    schedules = load_schedules("schedule.json")
    target_schedules = filter_schedules_by_date(schedules, target_date)
    
    # 出力
    print(f"{target_date} の予定 {len(target_schedules)} 件")
    for item in target_schedules:
        print(format_schedule(item))

if __name__ == "__main__":
    main()