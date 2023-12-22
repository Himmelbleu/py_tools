package org.example.copyer;

import java.text.SimpleDateFormat;
import java.util.Date;

public class DateUtil {

    public static String format(String pattern){
        SimpleDateFormat dateFormat = new SimpleDateFormat(pattern);
        return dateFormat.format(new Date());
    }

}
