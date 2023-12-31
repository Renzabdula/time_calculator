def add_time(start, duration, day_of_week = False):
  days_of_the_week_array = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
  days_of_the_week_index = {"monday" : 0,"tuesday" : 1,"wednesday" : 2,"thursday" : 3, "friday" : 4, "saturday" : 5, "sunday" : 6}
  
  duration_tuple = duration.partition(":")
  duration_hour = int(duration_tuple[0])
  duration_minutes = int(duration_tuple[2] )

  start_tuple = start.partition(":")
  start_hour = int(start_tuple[0])
  start_minutes_tuple = start_tuple[2].partition(" ")
  start_minutes = int(start_minutes_tuple[0])
  am_or_pm = start_minutes_tuple[2]
  am_or_pm_flip = {"AM":"PM","PM":"AM"}
 
  amount_of_days = int(duration_hour / 24)
  
  end_minutes = start_minutes + duration_minutes
  if(end_minutes >= 60):
    start_hour += 1
    end_minutes = end_minutes % 60
    
  amount_am_or_pm_flips = int((start_hour + duration_hour)/12)
  end_hour = (start_hour + duration_hour) % 12

  end_minutes = end_minutes if end_minutes > 9 else "0" + str(end_minutes)
  end_hour = end_hour = 12 if end_hour == 0 else end_hour
  if(am_or_pm == "PM" and start_hour + (duration_hour % 12 ) >= 12):
    amount_of_days += 1

  am_or_pm = am_or_pm_flip[am_or_pm] if amount_am_or_pm_flips % 2 == 1 else am_or_pm

  returnTime = str(end_hour) + ":" + str(end_minutes) + " " + am_or_pm
  if(day_of_week):
    day_of_week = day_of_week.lower()
    index = int((days_of_the_week_index[day_of_week]) + amount_of_days) % 7
    new_day = days_of_the_week_array[index]
    returnTime += ", " + new_day

  if(amount_of_days == 1):
    return returnTime + " " + "(next day)"
  elif(amount_of_days > 1):
    return returnTime + " (" + str(amount_of_days) + " days later)"
  
  return returnTime
