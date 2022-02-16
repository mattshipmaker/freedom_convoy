import csv
from operator import truediv

bcPostals = ["V1A", "V2A", "V3A", "V4A", "V5A", "V6A", "V7A", "V8A", "V9A", "V1B", "V2B", "V3B", "V4B", "V5B", "V6B", "V7B", "V8B", "V9B", "V1C", "V2C", "V3C", "V4C", "V5C", "V6C", "V7C", "V8C", "V9C", "V1E", "V2E", "V3E", "V4E", "V5E", "V6E", "V7E", "V8E", "V9E", "V1G", "V2G", "V3G", "V4G", "V5G", "V6G", "V7G", "V8G", "V9G", "V1H", "V2H", "V3H", "V4H", "V5H", "V6H", "V7H", "V8H", "V9H", "V1J", "V2J", "V3J", "V4J", "V5J", "V6J", "V7J", "V8J", "V9J", "V1K", "V2K", "V3K", "V4K", "V5K", "V6K", "V7K", "V8K", "V9K", "V1L", "V2L", "V3L", "V4L", "V5L", "V6L", "V7L", "V8L", "V9L", "V1M", "V2M", "V3M", "V4M", "V5M", "V6M", "V7M", "V8M", "V9M", "V1N", "V2N", "V3N", "V4N", "V5N", "V6N", "V7N", "V8N", "V9N", "V1P", "V2P", "V3P", "V4P", "V5P", "V6P", "V7P", "V8P", "V9P", "V1R", "V2R", "V3R", "V4R", "V5R", "V6R", "V7R", "V8R", "V9R", "V1S", "V2S", "V3S", "V4S", "V5S", "V6S", "V7S", "V8S", "V9S", "V1T", "V2T", "V3T", "V4T", "V5T", "V6T", "V7T", "V8T", "V9T", "V1V", "V2V", "V3V", "V4V", "V5V", "V6V", "V7V", "V8V", "V9V", "V1W", "V2W", "V3W", "V4W", "V5W", "V6W", "V7W", "V8W", "V9W", "V1X", "V2X", "V3X", "V4X", "V5X", "V6X", "V7X", "V8X", "V9X", "V1Y", "V2Y", "V3Y", "V4Y", "V5Y", "V6Y", "V7Y", "V8Y", "V9Y", "V1Z", "V2Z", "V3Z", "V4Z", "V5Z", "V6Z", "V7Z", "V8Z", "V9Z", "V0A", "V0B", "V0C", "V0E", "V0G", "V0H", "V0J", "V0K", "V0L", "V0M", "V0N", "V0P", "V0R", "V0S", "V0T", "V0V", "V0W", "V0X", "V0Y", "V0Z"]

totalrows = 0

class Donation():
    def __init__(self, row):
        self.name = row[9]+ " " + row[10]
        self.postal = row[12]
        self.country = row[13]
        self.amount = float(row[16])
        self.comment = row[15]
        
    def isCanada(self):
        return (self.country == "CA")

    def isPG(self):
        ret = (self.postal.startswith("V2K") or  self.postal.startswith("V2L") or  self.postal.startswith("V2M") or  self.postal.startswith("V2N") )
        return ret

    def isBC(self):
        for p in bcPostals:
            if(self.postal.startswith(p)):
                return True
        return False

    def hasGod(self):
        return ("god" in self.comment.lower())

    def tostring(self):
        return self.name + "  -  " + self.amount
 
donation_list = []



with open('convoy_donations.txt', "r", encoding="UTF-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter =',')
    line_count = 0

    for row in csv_reader:
        if(line_count == 0):
            line_count = 1
            continue

        donation_list.append(Donation(row))
        totalrows = totalrows + 1

pgAmount = 0.0
canadaAmount = 0.0
godamounts = 0

for donation in donation_list:
    if(donation.hasGod()):
        godamounts = godamounts + 1

print(f"total god mentions: {godamounts} of {totalrows} = {godamounts / totalrows}")