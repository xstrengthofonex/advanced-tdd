import re
from typing import List


class NameInverter:
    def invert_name(self, name: str) -> str:
        if name is None or len(name) <= 0:
            return ""
        return self._format_name(self._remove_honorifics(self._split_names(name)))

    def _format_name(self, names):
        if len(names) == 1:
            return names[0]
        return self._format_multi_element_name(names)

    def _remove_honorifics(self, names) -> List[str]:
        if len(names) > 1 and self._is_honorific(names[0]):
            names.pop(0)
        return names

    @staticmethod
    def _split_names(name: str) -> List:
        return re.split(r"\s+", name.strip(" "))

    def _format_multi_element_name(self, names):
        post_nominal = self._get_post_norminals(names)
        first_name = names[0]
        last_name = names[1]
        return "{}, {} {}".format(last_name, first_name, post_nominal).strip(" ")

    @staticmethod
    def _get_post_norminals(names: List[str]) -> str:
        post_nominal = ""
        if len(names) > 2:
            post_nominal = " ".join(names[2:])
        return post_nominal

    @staticmethod
    def _is_honorific(name: str) -> bool:
        honorifics = ["Mr.", "Mrs."]
        return name in honorifics
