import re
from functools import total_ordering


@total_ordering
class Version:
    abbr = {'alpha': '0', 'beta': '1', 'rc': '2', 'a': '.0', 'b': '.1', '-': '.'}

    def __init__(self, version: str):
        self.version = self.get_processing_version(version)

    def get_processing_version(self, version: str) -> list:
        """Pre-processing the version"""

        for key, value in self.abbr.items():
            version = re.sub(key, value, version)
        return version.split('.')

    def __lt__(self, other):
        """Checking the version by the condition less than"""

        versions = zip(self.version, other.version)
        for i, j in versions:
            if i.isdigit() and j.isdigit() and i != j:
                return i < j
        return len(self.version) > len(other.version)

    def __gt__(self, other):
        """Checking the version by the condition more than"""

        versions = zip(self.version, other.version)
        for i, j in versions:
            if i.isdigit() and j.isdigit() and i != j:
                return i > j
        return len(self.version) < len(other.version)

    def __ne__(self, other):
        """Checking the version by the not equal condition"""

        versions = zip(self.version, other.version)
        for i, j in versions:
            if i.isdigit() and j.isdigit() and i != j:
                return True
        return len(self.version) != len(other.version)


def main():
    to_test = [
        ("1.0.0", "2.0.0"),
        ("1.0.0", "1.42.0"),
        ("1.2.0", "1.2.42"),
        ("1.1.0-alpha", "1.2.0-alpha.1"),
        ("1.0.1b", "1.0.10-alpha.beta"),
        ("1.0.0-rc.1", "1.0.0"),
    ]

    for version_1, version_2 in to_test:
        assert Version(version_1) < Version(version_2), "le failed"
        assert Version(version_2) > Version(version_1), "ge failed"
        assert Version(version_2) != Version(version_1), "neq failed"


if __name__ == "__main__":
    main()
