# Local LanguageTool check (tested 2026-10-06)

Needs Java 17+ and Maven. Downloads ~50 MB of jars from Maven Central (LanguageTool 6.8, French).

    mvn -q dependency:copy-dependencies -DoutputDirectory=lib compile
    JAVA_TOOL_OPTIONS=-Dfile.encoding=UTF-8 java -Dstdout.encoding=UTF-8 -cp "lib/*:target/classes" Check text.txt

Alternative on a normal machine: `pip install language_tool_python` (also needs Java; downloads LanguageTool itself).
Output: one line per issue: «text» -> [suggestions] | rule id | message.
