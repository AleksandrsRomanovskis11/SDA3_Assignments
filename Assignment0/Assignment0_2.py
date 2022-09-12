from tkinter import*
from datetime import date,datetime
from tkinter import font

root = Tk()
root.title("Assignment0_2")
#var = StringVar()
#label = Label(root, textvariable=var)

#var.set("My Countdowncalendar")

#label.pack()

c= Canvas(root, width=800, height= 300, bg="black")

c.pack()

c.create_text (100, 50 ,anchor="w", fill="orange",font= "Arial 20 bold underline", text ="My Countdowncalendar")

 
def get_events():
  list_events = []
  with open('events.txt') as file:  #opens event.txt file
    for line in file:
      line = line.rstrip('\n') #Python ignores newline which is made my pressing enter/space by the end of the line, # print(line)
      current_event = line.split(',') #splits event into two parts, # print(current_event)
      event_date = datetime.strptime(current_event[1], '%d/%m/%y').date() #converstion to the date that python can understand, # print(event_date)
      current_event[1] = event_date 
      list_events.append(current_event) #.append inserts a single element into and existing list, so that means element will be added , its name and date will be added as well
  return list_events


def days_between_dates(date1,date2):
    time_between_days = str(date1-date2)
    number_of_days = time_between_days.split (' ')
    return number_of_days[0] #value stored in position 0 

events= get_events()    
today = date.today()

vertical_space = 100

for event in events:                   # print(event)
  event_name = event[0]
  days_until = days_between_dates(event[1],today)
  display = 'It is %s days until %s' % (days_until, event_name)
  
  c.create_text(100, vertical_space ,anchor="w", fill="orange",font= "Arial 20 bold underline", text =display )
  
  vertical_space = vertical_space + 60



                        
root.mainloop ()





