import static org.junit.Assert.assertEquals;

import org.junit.Test;

public class mycdTest {

  @Test
  public void testProvidedTests() {
    assertEquals("/abc", mycd.getOutputString("/", "abc"));
    assertEquals("/abc/def/ghi", mycd.getOutputString("/abc/def", "ghi"));
    assertEquals("/abc", mycd.getOutputString("/abc/def", ".."));
    assertEquals("/abc", mycd.getOutputString("/abc/def", "/abc"));
    assertEquals("/abc/klm", mycd.getOutputString("/abc/def", "/abc/klm"));
    assertEquals("/", mycd.getOutputString("/abc/def", "../.."));
    assertEquals("/", mycd.getOutputString("/abc/def", "../../.."));
    assertEquals("/abc/def", mycd.getOutputString("/abc/def", "."));
    assertEquals("..klm: No such file or directory", mycd.getOutputString("/abc/def", "..klm"));
    assertEquals("/", mycd.getOutputString("/abc/def", "//////"));
    assertEquals("......: No such file or directory", mycd.getOutputString("/abc/def", "......"));
    assertEquals("/abc/klm", mycd.getOutputString("/abc/def", "../gh///../klm/."));
  }

  @Test
  public void testNonAlphaNumericCurrentDirectoryInput() {
    assertEquals("&&&: No such file or directory (current directory input)", mycd.getOutputString("/&&&", "def"));
    assertEquals("&&&: No such file or directory (current directory input)", mycd.getOutputString("/abc/&&&", "def/ghi"));;
    assertEquals("&&&: No such file or directory (current directory input)", mycd.getOutputString("/abc/&&&/ghi", "../def"));
  }

  @Test
  public void testNonAlphaNumericNewDirectoryInput() {
    assertEquals("%: No such file or directory", mycd.getOutputString("/abc", "%"));
    assertEquals("%$&: No such file or directory", mycd.getOutputString("/abc", "%$&"));
    assertEquals("%$&: No such file or directory", mycd.getOutputString("/abc", "def/%$&"));
    assertEquals("%$&: No such file or directory", mycd.getOutputString("/abc/def", "def/%$&/ghi"));
    assertEquals("%$&: No such file or directory", mycd.getOutputString("/abc/def/ghi", "def/%$&/../ghi"));
  }
}
