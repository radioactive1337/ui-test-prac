from enum import Enum


class ErrorEnums(Enum):
    ELEMENT_NOT_FOUND = "Can't find element by locator: "
    TEXT_NOT_EQUAL = "Expected text is not equal to actual"
    ATTRIBUTE_NOT_EQUAL = "Expected attribute is not equal to actual"
    ATTRIBUTE_EQUAL = "Expected attribute is equal to actual"
    URL_NOT_EQUAL = "Expected url is not equal to actual"
    PAGE_TITLE_NOT_EQUAL = "Expected page title is not equal to actual"
