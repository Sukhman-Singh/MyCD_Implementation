#!/usr/bin/env python

import sys


def main():
    # check that there are exactly 2 inputs (size 3 because the first item is the function name)
    if len(sys.argv) != 3:
        print("Please provide exactly two inputs: the current directory path and the new directory.")
        return

    # get the two inputs and print the expected output string
    print(getOutputString(sys.argv[1], sys.argv[2]))


# takes in the current directory path and the new directory and returns the expected output string for the cd command
def getOutputString(curr_directory, new_directory):
    parsed_new_dir = new_directory.split("/")

    # If the first character in newDirectory is "/", we should go back to the root directory
    # To go back to the root directory, we can start with an empty currDirList
    if new_directory.startswith("/"):
        parsed_curr_dir = []

    # if the first character is not "/", then we can use our parsed_curr_dir
    else:
        parsed_curr_dir = curr_directory.split("/")

        i = 0
        # check that each directory in the current directory input is valid
        while i < len(parsed_curr_dir):
            # the empty strings are created by the leading "/" or when there are multiple forward slashes
            # in a row, they do not need to be added to the list and should not cause an error
            if parsed_curr_dir[i] == "":
                parsed_curr_dir.remove("")

            # if a directory in the current directory input is invalid, print an error message
            elif not parsed_curr_dir[i].isalnum():
                return parsed_curr_dir[i] + ": No such file or directory (current directory input)"

            # else the string is a valid directory so we can keep it in the array and increment i
            else:
                i += 1

    # iterate through every directory in parsed_new_dir
    for direct in parsed_new_dir:

        # the empty strings are created by the leading "/" or when there are multiple
        # forward slashes in a row, they do not need to be added to the list
        # if the dir is ".", stay in current directory (do nothing)
        if direct == "" or direct == ".":
            continue

        # if the dir is "..", move up one directory
        # this can be done by deleting the last item in parsed_curr_dir
        elif direct == "..":
            if not len(parsed_curr_dir) == 0:
                parsed_curr_dir.pop(len(parsed_curr_dir) - 1)

        # prints error message if all characters in dir are not alphanumerics
        # the only valid non-alphanumeric characters are "." and ".." and
        # those cases are handled above
        elif not direct.isalnum():
            return direct + ": No such file or directory"

        # if the dir is a valid file name, add it to the parsed_curr_dir
        else:
            parsed_curr_dir.append(direct)

    # if parsed_curr_dir is empty, we are in the current directory
    if len(parsed_curr_dir) == 0:
        return "/"

    # else we need to build up the output string by adding in the "/" between each directory
    else:
        output_string = ""
        for direct in parsed_curr_dir:
            # removes extra forward slashes
            if direct != "":
                output_string += "/" + direct

        # print the new file path
        return output_string


if __name__ == "__main__":
    main()
