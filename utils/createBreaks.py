def create_breaks(lesson_break, break_duration):
    resultMinutes = lesson_break.minute + int(break_duration)
    result_time = f'{lesson_break.hour}:{resultMinutes}:00'
    return result_time


