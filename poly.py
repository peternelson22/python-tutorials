class NetFlix:
    def watch(self):
        print('Watching movies')

class Apple:
    def watch(self):
        print('Watching movies')
        print('Stream movies')


class Computer:
    def enjoy(self, service):
        service.watch()

serve = Apple()

con = Computer()
con.enjoy(serve)
