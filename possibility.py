import json
from datetime import datetime, timedelta

def load_schedule(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def time_range(start, end, interval_minutes=30):
    times = []
    current = start
    while current < end:
        next_time = current + timedelta(minutes=interval_minutes)
        times.append((current, next_time))
        current = next_time
    return times

def parse_time_range(time_str):
    start_str, end_str = time_str.split(" - ")
    start_time = datetime.strptime(start_str, "%H:%M")
    end_time = datetime.strptime(end_str, "%H:%M")
    return start_time, end_time

#set range jam
def find_free_slots(schedule, start_hour=7, end_hour=23):
    free_slots_per_day = {}
    
    #set range hari
    days = {"Senin", "Selasa", "Rabu", "Kamis", "Jumat","Sabtu","Minggu"}
    for day in days:
        start_day = datetime.strptime(f"{start_hour}:00", "%H:%M")
        end_day = datetime.strptime(f"{end_hour}:00", "%H:%M")
        all_intervals = time_range(start_day, end_day)
        
        booked_intervals = []
        for user, sessions in schedule.items():
            for session in sessions:
                if session["hari"] == day:
                    booked_intervals.append(parse_time_range(session["jam"]))
        
        free_intervals = []
        for interval in all_intervals:
            start, end = interval
            is_free = all(not (start < booked_end and end > booked_start) for booked_start, booked_end in booked_intervals)
            if is_free:
                free_intervals.append(interval)
        
        consolidated_free_intervals = []
        if free_intervals:
            current_start = free_intervals[0][0]
            current_end = free_intervals[0][1]
            for i in range(1, len(free_intervals)):
                next_start, next_end = free_intervals[i]
                if current_end == next_start:
                    current_end = next_end
                else:
                    consolidated_free_intervals.append((current_start, current_end))
                    current_start = next_start
                    current_end = next_end
            consolidated_free_intervals.append((current_start, current_end))
        
        free_slots = [f"{start.strftime('%H:%M')} - {end.strftime('%H:%M')}" for start, end in consolidated_free_intervals]
        free_slots_per_day[day] = free_slots
    
    return free_slots_per_day

def main():
    schedule = load_schedule("template.json")
    free_slots_per_day = find_free_slots(schedule)
    
    days_order = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat","Sabtu","Minggu"]
    
    for day in days_order:
        slots = free_slots_per_day.get(day, [])
        if slots:
            filtered_slots = [slot for slot in slots if slot != "12:00 - 12:30"]
            
            if filtered_slots:
                print(f"Jadwal kosong pada hari {day}:")
                for slot in filtered_slots:
                    print(slot)
            else:
                print(f"Tidak ada jadwal kosong pada hari {day}")
        else:
            print(f"Tidak ada jadwal kosong pada hari {day}")

if __name__ == "__main__":
    main()
