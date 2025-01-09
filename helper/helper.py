from helper.core import GetValueFromObject, IsProcessRunning, IsValueSame


def CheckIfApplicationIsRunning():
    process_name_or_id = ""
    if IsProcessRunning(process_name_or_id):
        test.passes(f"Application with Name / ID - {process_name_or_id} is running")
    else:
        test.fail(f"Application with Name / ID - {process_name_or_id} is not running")


def CheckIfValueIsSame(actual, expected) -> None:
    if IsValueSame(actual, expected):
        test.passes(f"Actual value - '{actual}' and Expected value -'{expected}' values are the same")
    else:
        test.fail(f"Actual value - '{actual}' and Expected value -'{expected}' values are NOT the same")


def CheckIfValueIsNotEmpty(obj: str) -> None:
    if GetValueFromObject(obj):
        test.passes(f"Object value is not empty")
    else:
        test.fail(f"Object value is empty")
