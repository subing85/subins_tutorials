import os

if __name__ == '__main__':
    current_path = os.path.dirname(__file__)
    pipe_path = os.path.dirname(current_path)
    show_path = os.path.dirname(pipe_path)
    print show_path, pipe_path