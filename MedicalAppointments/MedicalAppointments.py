import csv
import time
import os
filename = 'Database2PostNote.csv'

class Methods():
    
    def __init__(self):
        '''init master_list and self.master_list to store the file in'''
        master_list=[]
        self.master_list = master_list
        master_list2 = []
        self.master_list2 = master_list2
    def add(self):
        ''' Add a new line with csv writer to the file tmp.txt'''
        with open(filename,'w') as f:
            writer= csv.writer(f)
            
            row = ['Date: ','Time: ','Name: ', 'Note: ', 'Post Note: ']
            row[0] = 'Date: ' + input('Date: ')
            row[1] = 'Time: ' + input('Time: ')
            row[2] = 'Name: ' + input('Name: ')
            row[3] = 'Note: ' + input('Note: ')
           
            #self.load()
            
            for ro in self.master_list:
                writer.writerow(ro)
            writer.writerow(row)
            f.close()
            
    def load(self):
        ''' initializing master_list with a list of lists that are each an eantry line'''
        self.master_list = []
        print(' -----------------------------------------------------------')
        print('|           Loading Database File..                         |')
        print(' -----------------------------------------------------------')
        time.sleep(1)
            
        with open(filename) as p:
            reader = csv.reader(p)
            for row in reader:
                self.master_list.append(row)
        print(' -----------------------------------------------------------')
        print('|               Database has been loaded successfully..     |')
        print(' -----------------------------------------------------------')
        time.sleep(2.5)
    def after_load(self):
        ''' Adding a Post Note after the visit'''
        self.load()
        c = 1        
        for row in self.master_list:
            print(row)
            c = c + 1
        c = c - 1
        print('There are ' + str(c) + ' rows')
        a = input('Which row is the one you want to modify. Top down?  ')
        if int(a) <= 0:
            print('Error number to small')
        elif int(a) >= 1:
            list = self.master_list[int(a)-1]
            b = input('Modifying Post-Visit Note Type it here:  ')
            list[4] = 'Post Note: ' + str(b)
            print(list[4])
         
            for row in self.master_list:
                if row == self.master_list[int(a)-1]:
                    self.master_list[int(a)-1][4] = 'Post Note: ' + str(b)
                    self.master_list2.append(row)
                else:
                    self.master_list2.append(row)
            self.master_list = self.master_list2
            
            print(self.master_list)
            with open(filename,'w') as f:
                writer = csv.writer(f)
                for row in self.master_list:
                    writer.writerow(row)
                f.close()
        else:
            print('Error invalid input enter a number')
    def search(self,phrase):
        with open(filename, "r") as f:
            searchlines = f.readlines()
        for i, line in enumerate(searchlines):
            if phrase in line: 
                for l in searchlines[i:i+3]: print(l),
                print
    
    def delete(self,entry):
        '''Delete a line out of the file and rewrite it with out that line'''
        lines = open(filename, 'r').readlines()
        for line in lines:
            if entry not in line:
                open(filename, 'w').writelines(line)
                
            else:
                continue
    def printer(self, format=''):
        ''' Prints the database in a friendly format 
        and that pretty much covers this program '''
        if format == 'data':
            with open(filename,'r') as f:
                reader = csv.reader(f)
                for row in reader:
                    print(row)
            f.close()
        elif format == 'friendly':
            with open(filename,'r') as f:
                reader = csv.reader(f)
                for row in reader:
                    print(row[0] + '\n' + row[1] + '\n' + \
                         row[2] + '\n' + row[3] + '\n' + row[4] + '\n' \
                         '-----------------------------------' + '\n')
            f.close
                    

class Menu():
    def __init__(self,ainstance):
        print('Program 2.0')
        self.ainstance = ainstance
    def loop(self):
        ''' Runs the menu over in a loop '''
        self.ainstance.load()
        print('________________________________________________________________________________________________________________')
        option = input('(s)Search for word\n\n(a)Add a entry to database\n\n(rd) Read database without formatted text OR \n\n(r) Read human readable text formatted\n\n(d) Delete a entry from database\n\n(p) Add a post note [after the visit]\n\nHotkeys are in parenthesis\n________________________________________________________________________________________________________________\n>>')
        if option == 'a':
            self.ainstance.add()
            self.loop()
        elif option == 'd':
            print('________________________________________________________________________________________________________________')
            a = input('A string that matches the entry to delete: ')
            print('________________________________________________________________________________________________________________')
            self.ainstance.delete(a)
            self.loop()
        elif option == 'p':
            self.ainstance.after_load()
            self.loop()
        elif option == 'rd':
            self.ainstance.printer('data')
            self.loop()
        elif option == 'r':
            self.ainstance.printer('friendly')
            #Menu.loop(ainstance)
            self.loop()
        elif option == 's':
            phrase = input('Search for this phrase exactly how it appears in (rd) output\nOr just search by word: ')
            self.ainstance.search(phrase)
            self.loop()
        else:
            print('________________________________________________________________________________________________________________')
            print('Invalid option back to the main menu...')
            print('________________________________________________________________________________________________________________')
            self.loop()
            
def main():            
    ''' Load is the most important it loads the database
        into a list of lists '''
    y = Methods()
    a = Methods()
    b = Menu(y)
    b.loop()

    
    
    

main()


#--------------------------------------------------------------only have to ...
# check delete... add search... printer (human readable) and bug test
#------------------------------------------------------------------------------
