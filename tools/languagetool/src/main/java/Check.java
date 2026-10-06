import org.languagetool.*; import org.languagetool.language.*; import org.languagetool.rules.*;
import java.nio.file.*; import java.util.*;
public class Check { public static void main(String[] a) throws Exception {
  String t = Files.readString(Path.of(a[0]));
  JLanguageTool lt = new JLanguageTool(Languages.getLanguageForShortCode("fr"));
  for (RuleMatch m : lt.check(t)) {
    System.out.println("«" + t.substring(m.getFromPos(), m.getToPos()) + "» -> " + m.getSuggestedReplacements().stream().limit(3).toList() + " | " + m.getRule().getId() + " | " + m.getMessage().replaceAll("<[^>]+>",""));
  }}}
