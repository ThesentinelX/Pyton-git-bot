import os
import random
from datetime import datetime, timedelta

def make_realistic_commits(weeks: int):
    today = datetime.now()

    for week in range(weeks):
        # Начало недели (в прошлом)
        week_start = today - timedelta(weeks=week+1)

        # Выбираем 2 или 5 случайных дней недели
        active_days = random.sample(range(7), random.randint(2, 5))

        for day in active_days:
            commit_day = week_start + timedelta(days=day)

            # Сколько коммитов в этот день (1–5)
            commits_today = random.randint(1, 5)

            for i in range(commits_today):
                # Случайное время между 08:00 и 23:00
                hour = random.randint(8, 22)
                minute = random.randint(0, 59)

                commit_time = commit_day.replace(hour=hour, minute=minute, second=0)
                commit_date = commit_time.strftime('%Y-%m-%d %H:%M:%S')

                filename = f"data_{commit_day.strftime('%Y%m%d')}_{i}.txt"

                with open(filename, 'w') as f:
                    f.write(f"Commit at {commit_date}\n")

                os.system(f'git add {filename}')
                os.system(f'git commit --date="{commit_date}" -m "Update logs {i+1} on {commit_day.strftime("%Y-%m-%d")}"')

    os.system('git push')

# Запускаем на последние 312 недель 6 лет
make_realistic_commits(312)
