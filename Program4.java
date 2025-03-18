public class HelloWorld {
    public static void main(String[] args) {
        // Get the message from an environment variable
        String message = System.getenv("MESSAGE");
        
        // If MESSAGE is not set, use the default message
        if (message == null) {
            message = "Hello, World!";
        }
        
        // Print the message
        System.out.println(message);
    }
}

