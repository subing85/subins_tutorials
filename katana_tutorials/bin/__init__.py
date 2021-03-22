import os

if __name__ == '__main__':
    current_path = os.path.dirname(__file__)
    show_path = os.path.dirname(current_path)
    pipe_path = os.path.join(show_path, 'pipe')
    print show_path, pipe_path    
