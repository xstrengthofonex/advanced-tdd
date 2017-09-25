class Wrapper:
    def wrap(self, s: str, width: int) -> str:
        if s is None:
            return ""
        if len(s) <= width:
            return s
        break_point = self.find_break_point(s, width)
        return s[0:break_point] + "\n" + self.wrap(s[break_point:].strip(), width)

    @staticmethod
    def find_break_point(s, width):
        break_point = width
        if s[width] != " ":
            break_point = s.find(" ")
            if break_point == -1:
                break_point = width
        return break_point