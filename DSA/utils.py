

# decorators
def print_line_after_block(func):
    def printer():
        func()
        print('----------------------------------------------')
    return printer
