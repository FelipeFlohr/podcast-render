class Parser:
    def __init__(self, file_name):
        """
        -> Constructor
        :param file_name: The name of the file you want to generate
        """
        self.file_name = file_name

    def write(self):
        """
        -> Will generate a .ini config file on the root folder. If the file already exists, nothing will happen
        :return: no return
        """
        try:
            f = open(f'{self.file_name}', 'x')
            f.write("""# ---File Configs---
frames_folder = C:\\Users\\Felipe\\Desktop\\Frames # < - String. The absolute path of the folder containing each frame.
video_path = C:\\Users\\Felipe\\Documents\\video.mp4 # <- String. The absolute path of the video.
output_video_name = output.mp4 # <- String. Video's name when it's fully rendered.
""")
            print("config.ini file created")
        except FileExistsError:
            pass

    def count_lines(self):
        """
        -> This will count how many lines there is on the file
        :return: The total amount of lines
        """
        f = open(f'{self.file_name}', 'r')
        lines = 0
        for line in f:
            if line != '\n':
                lines += 1
        f.close()
        return lines

    def lines(self):
        """
        -> This will generate a list where each index is one line of the file
        :return: Return a list where each index is one line
        """
        line = open('{}'.format(self.file_name), 'r')
        line_total = line.readlines()
        new_list = list()
        for index in line_total:
            new_line = index.replace('\n', '').strip()
            new_list.append(new_line[:])
        return new_list

    def search_parameter(self, param):
        """
        -> This will search every line trying to find the specified parameter.
        :param param: The parameter you want to search
        :return: Returns the entire string containing the parameter
        """
        lines_list = self.lines()
        line = -1
        count = 0
        while True:
            if count >= len(lines_list):
                raise IndexError("Parameter not found on the list.")
            if lines_list[count][0] == '' or lines_list[count][0] == '#' or lines_list[count][0] == ' ':
                count += 1
            elif param in lines_list[count]:
                line = count
                break
            else:
                count += 1
                pass
        return lines_list[line]

    def equal_pos(self, line_i):
        """
        -> Will find the "=" position on the line
        :param line_i: The line you want to find the "=" position
        :return: Return the index position of "="
        """
        equal_pos = -1
        for c in range(0, len(line_i)):
            if line_i[c] == '=':
                equal_pos = c
            else:
                pass
        return equal_pos

    def comment_pos(self, line):
        """
        -> Will find the "#" position on the line
        :param line: The line you want to find the "#" position
        :return: Return the index position of "#"
        """
        comment_pos = -1
        for c in range(0, len(line)):
            if line[c] == '#':
                comment_pos = c
            else:
                pass
        return comment_pos

    def argument(self, line, type):
        """
        -> Will return the value specified for the parameter :param line: The line you want to return the value
        :param type: The type you want to return the values. Currently, there are this options: 'tuple_int', 'int',
        'str', 'float'. Please, specify correctly to each one.
        :return: Will return the value for the line.
        """
        TYPES = ['tuple_int', 'int', 'str', 'float']
        arg = line[self.equal_pos(line) + 1: self.comment_pos(line)].strip()
        if type not in TYPES:
            raise TypeError('Type not available')
        if type == 'tuple_int':
            try:
                tuple_arg = arg.replace('(', '').replace(')', '').replace(' ', '').split(',')
                lst = list(tuple_arg)
                new_list = list()
                for item in lst:
                    integer = int(item)
                    new_list.append(integer)
                return tuple(new_list)
            except Exception:
                raise TypeError('Not possible to convert to the specified type.')
        elif type == 'int':
            try:
                return int(arg)
            except Exception:
                raise TypeError('Not possible to convert to the specified type.')
        elif type == 'str':
            try:
                return arg
            except Exception:
                raise TypeError('Not possible to convert to the specified type.')
        elif type == 'float':
            try:
                return float(arg)
            except Exception:
                raise TypeError('Not possible to convert to the specified type.')


class Parameters(Parser):
    """
    -> Each method in this class does the same thing. Just the parameter changes
    """
    pass

    def frames_folder(self):
        return self.argument(self.search_parameter("frames_folder"), "str")

    def video_path(self):
        return self.argument(self.search_parameter("video_path"), "str")

    def output_video_name(self):
        return self.argument(self.search_parameter("output_video_name"), "str")
