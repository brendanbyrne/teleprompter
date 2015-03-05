
import time

class Teleprompter (object):
    def __init__ (self, script, wpm, display_dimensions):
        self.filename = script
        self.read_rate = float(wpm)

        self.screen = Display(*display_dimensions)
        
        self.script = self.parse()

    def parse (self):
        with open(self.filename, 'rb') as f:
            raw = f.read()
        return raw.split('\n')

    def start (self):
        for line in self.script:
            self.screen.add_text(line)
            self.screen.show()
            
            words = line.split(' ')
            
            time.sleep(float(len(words)) / self.read_rate)

class Display (object):
    def __init__ (self, x_size, y_size):
        self.x_lim = x_size
        self.y_lim = y_size
        self.screen = []

    def add_text (self, raw_incoming_string):
        string = raw_incoming_string.replace('\n', ' ')
        text = string.split(' ')
        
        if text == ['']: return
                
        line = []
        for word in text:
            
            length = len(' '.join([str(w) for w in line] + [str(word)]))
            
            if length > self.x_lim:
                self.screen.append(' '.join([w for w in line]))
                line = []
            else:
                line.append(word)
        self.screen.append(' '.join([w for w in line]))

    def show (self):
        if len (self.screen) > self.y_lim: print '\n'.join([ line for line in self.screen[-self.y_lim] ])
        else:
            top_space = ['' for i in xrange(self.y_lim-len(self.screen))]
            print '\n'.join([ line for line in top_space+self.screen ])
        
        
