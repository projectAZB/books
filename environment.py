from enum import IntEnum


class Environment(IntEnum):
    TESTING = 0
    DEVELOPMENT = 1
    STAGING = 2
    PRODUCTION = 3

    def __str__(self):
        if self == Environment.TESTING:
            return 'Testing'
        if self == Environment.DEVELOPMENT:
            return 'Development'
        if self == Environment.STAGING:
            return 'Staging'
        if self == Environment.PRODUCTION:
            return 'Production'
        return ''
