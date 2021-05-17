import re
from itertools import zip_longest


class Version:
    abbr = {'alpha': '0', 'beta': '1', 'rc': '2', 'a': '.0', 'b': '.1', '-': '.'}

    def __init__(self, version: str):
        self.version = self.get_processing_version(version)

    def get_processing_version(self, version: str) -> list:
        """Pre-processing the version"""
        cmp = 0
        for num in version.split('.'):
            if not num.isdigit():
                cmp = 1
        for key, value in self.abbr.items():
            version = re.sub(key, value, version)
        return cmp, version

    def __lt__(self, other):
        """Checking the version by the condition less than"""
        if self.version[0] > other.version[0]:
            return True
        versions = zip_longest(self.version[1], other.version[1], fillvalue='0')
        for i, j in versions:
            if i.isdigit() and j.isdigit() and i != j:
                return i < j
        return len(self.version[1]) > len(other.version[1])

    def __gt__(self, other):
        """Checking the version by the condition more than"""

        if self.version[0] < other.version[0]:
            return True
        versions = zip_longest(self.version[1], other.version[1], fillvalue='0')
        for i, j in versions:
            if i.isdigit() and j.isdigit() and i != j:
                return i > j
        return len(self.version[1]) < len(other.version[1])

    def __ne__(self, other):
        """Checking the version by the not equal condition"""
        if self.version[0] != other.version[0]:
            return True
        versions = zip_longest(self.version[1], other.version[1], fillvalue='0')
        for i, j in versions:
            if i.isdigit() and j.isdigit() and i != j:
                return True
        return len(self.version[1]) != len(other.version[1])


def main():
    to_test = [
        ("1.0.0", "2.0.0"),
        ("1.0.0", "1.42.0"),
        ("1.2.0", "1.2.42"),
        ("1.1.0-alpha", "1.2.0-alpha.1"),
        ("1.0.1b", "1.0.10-alpha.beta"),
        ("1.0.0-rc.1", "1.0.0"),
        ("1.0.0", '1')
    ]

    for version_1, version_2 in to_test:
        assert Version(version_1) < Version(version_2), "le failed"
        assert Version(version_2) > Version(version_1), "ge failed"
        assert Version(version_2) != Version(version_1), "neq failed"


if __name__ == "__main__":
    main()
