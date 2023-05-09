
import java.net.HttpURLConnection;
import java.net.URL;

public class BOJ7287 {
    public static void main(String args[]){
        // HttpURLConnection conn = null;
        // System.out.println("hello world");
        try {
            URL url = new URL("https://solved.ac/api/v3/user/show?handle=jquath");
            HttpURLConnection http = (HttpURLConnection)url.openConnection();
            http.setRequestProperty("Content-Type", "application/json");
            
            System.out.println(http.getResponseCode() + " " + http.getResponseMessage());
            // http.disconnect();
        } catch (Exception e) {
            System.out.println("error occured");
            //TODO: handle exception
        }
    }
    
}
