import java.util.ArrayList;

public class mycd {

  public static void main(String[] args) {

    // check that there are exactly 2 inputs
    if (args.length != 2) {
      System.out.println(
          "Please provide exactly two inputs: the current directory path and the new directory.");
      return;
    }

    // get the two inputs and uses them to print the expected output string
    System.out.println(getOutputString(args[0], args[1]));
  }

  // outputs the correct output string using the two provided inputs, current and new directory
  public static String getOutputString(String currDirectory, String newDirectory) {

    String[] parsedNewDir = newDirectory.split("/");
    ArrayList<String> parsedCurrDirList = new ArrayList<String>();

    // If the first character in newDirectory is "/", we should go back to the root directory
    // The body of this if statement adds all the items to our parsedCurrDirList, so by not
    // adding anything to it, we are setting the current position at the root directory
    if (!newDirectory.startsWith("/")) {

      String[] parsedCurrDir = currDirectory.split("/");

      // convert the parsedCurrDir array into an ArrayList so I can manipulate the size
      for (String str : parsedCurrDir) {

        // the empty strings are created by the leading "/" or when there are multiple
        // forward slashes in a row, they do not need to be added to the list and
        // should not cause an error
        if (str.equals("")) {
          continue;
        }

        // check that the string is a valid directory (only alphanumerics)
        if (isAlphaNumeric(str)) {
          parsedCurrDirList.add(str);
        }
        // if the string is not an alphanumeric, it is not a valid input
        else {
          return (str + ": No such file or directory (current directory input)");
        }
      }
    }

    // iterate through every directory in parsedNewDir
    for (String dir : parsedNewDir) {

      // the empty strings are created by the leading "/" or when there are multiple
      // forward slashes in a row, they do not need to be added to the list
      // if the dir is ".", stay in current directory (do nothing)
      if (dir.equals("") || dir.equals(".")) {
        continue;
      }

      // if the dir is "..", move up one directory
      // this can be done by deleting the last item in parsedCurrDir
      if (dir.equals("..")) {
        if (!parsedCurrDirList.isEmpty()) {
          parsedCurrDirList.remove(parsedCurrDirList.size() - 1);
        }
      }

      // prints error message if all characters in dir are not alphanumerics
      // the only valid non-alphanumeric characters are "." and ".." and
      // those cases are handled above
      else if (!isAlphaNumeric(dir)) {
        return(dir + ": No such file or directory");
      }
      // if the dir is a valid file name, add it to the parsedCurrDirList
      else {
        parsedCurrDirList.add(dir);
      }
    }

    // if parsedCurrDirList is empty, we are in the current directory
    if (parsedCurrDirList.isEmpty()) {
      return("/");
    }
    // else we need to build up the output string by adding in the "/" between each directory
    else {
      StringBuilder outputString = new StringBuilder();

      for (String dir : parsedCurrDirList) {
        outputString.append("/");
        outputString.append(dir);
      }
      // print the new file path
      return(outputString.toString());
    }
  }

  // checks whether the provided string only contains alphanumeric characters
  public static boolean isAlphaNumeric(String s) {
    return s != null && s.matches("^[a-zA-Z0-9]*$");
  }
}